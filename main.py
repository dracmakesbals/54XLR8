import streamlit as st
import requests
import json
from datetime import datetime

# Set page config
st.set_page_config(page_title="ETA Calculator", layout="centered")

# Custom CSS for better styling
st.markdown("""
<style>
    .big-font {
        font-size: 20px !important;
    }
    .result-box {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 15px;
        margin-top: 20px;
        background-color: #f9f9f9;
    }
    .highlight {
        color: #2e86de;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# API endpoint
API_URL = "your api here"

# App title
st.title("🚗 Travel Time Calculator")
st.markdown("Get accurate ETAs based on current traffic conditions")

# Input form
with st.form("eta_form"):
    col1, col2 = st.columns(2)
    with col1:
        pickup = st.text_input("Pickup Location", placeholder="e.g., Indiranagar")
    with col2:
        drop = st.text_input("Drop Location", placeholder="e.g., Whitefield")

    # Optional day/hour selection
    with st.expander("Advanced Options"):
        day_input = st.selectbox(
            "Day of Week",
            options=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            index=datetime.today().weekday() if datetime.today().weekday() < 7 else 0
        )
        hour_input = st.selectbox(
            "Hour of Day",
            options=[f"{i:02d}" for i in range(24)],
            index=datetime.now().hour
        )

    submitted = st.form_submit_button("Calculate ETA")

# Handle form submission
if submitted:
    if not pickup or not drop:
        st.warning("Please enter both pickup and drop locations")
    else:
        with st.spinner("Calculating best route..."):
            try:
                # Prepare payload
                payload = {
                    "pickup": pickup,
                    "drop": drop,
                    "day": day_input,
                    "hour": hour_input
                }

                # Make API call
                response = requests.post(API_URL, json=payload)

                if response.status_code == 200:
                    data = response.json()

                    if data['success']:
                        result = data['data']

                        # Display results in a clean layout
                        with st.container():
                            st.markdown("### 📊 Journey Details")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Standard ETA", result['eta'])
                            with col2:
                                st.metric("Adjusted ETA", f"{result['adjusted_eta']} min")
                            with col3:
                                st.metric("Distance", result['distance'])

                            st.divider()

                            st.markdown("#### Route Information")
                            st.info(result['route_info'])

                            st.markdown("#### Traffic Details")
                            st.progress(min(result['traffic_multiplier'] / 3, 1.0))
                            st.caption(f"Traffic multiplier: {result['traffic_multiplier']:.2f}x")

                            # Show raw JSON in expander
                            with st.expander("View Raw API Response"):
                                st.json(data)
                    else:
                        st.error(f"API Error: {data.get('error', 'Unknown error')}")
                else:
                    st.error(f"API Request Failed (Status {response.status_code})")
                    st.json(response.json())

            except requests.exceptions.RequestException as e:
                st.error(f"Connection Error: {str(e)}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Add some instructions
st.markdown("---")
st.markdown("""
**How to use:**
1. Enter your pickup and drop locations
2. Optionally adjust day/time for traffic predictions
3. Click 'Calculate ETA' to get your journey details
""")
