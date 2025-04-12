import streamlit as st
import requests
import json
from datetime import datetime

# Set page config for full-width layout
st.set_page_config(
    page_title="🚀 Advanced ETA Calculator",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    /* Main container */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Headers */
    h1, h2, h3 {
        color: #2a3f5f !important;
    }

    /* Cards */
    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 25px 15px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
        border-left: 5px solid #4e73df;
        transition: transform 0.3s ease;
    }

    .metric-card:hover {
        transform: translateY(-5px);
    }

    /* Metric values */
    .metric-value {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        color: #4e73df !important;
        margin-bottom: 5px !important;
    }

    /* Metric labels */
    .metric-label {
        font-size: 1rem !important;
        color: #6c757d !important;
        font-weight: 500 !important;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #4e73df 0%, #224abe 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        border: none !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15) !important;
    }

    /* Input fields */
    .stTextInput>div>div>input {
        border-radius: 8px !important;
        padding: 10px 15px !important;
    }

    /* Progress bar */
    .stProgress>div>div>div {
        background: linear-gradient(90deg, #4e73df 0%, #224abe 100%) !important;
    }

    /* Expander */
    .stExpander {
        background: white !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
        margin-bottom: 20px !important;
    }

    /* Info boxes */
    .info-box {
        background: rgba(78, 115, 223, 0.1) !important;
        border-radius: 8px !important;
        padding: 20px !important;
        border-left: 5px solid #4e73df !important;
        margin-bottom: 20px !important;
    }

    /* Divider */
    .stDivider {
        margin: 30px 0 !important;
    }

    /* Responsive columns */
    @media (max-width: 768px) {
        .metric-card {
            margin-bottom: 15px;
        }
    }
</style>
""", unsafe_allow_html=True)

# API endpoint
API_URL = "https://00af-2401-4900-6403-4591-5929-c28-9e1c-17f5.ngrok-free.app/api/calculate_eta"

# Main header
st.markdown("""
<div style="text-align: center; margin-bottom: 40px;">
    <h1 style="font-size: 2.8rem; color: #2a3f5f; margin-bottom: 10px;">🚀 Advanced ETA Calculator</h1>
    <p style="font-size: 1.1rem; color: #6c757d;">Get precise travel time estimates with real-time traffic analysis</p>
</div>
""", unsafe_allow_html=True)

# Create two columns for input form
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    # Input form in a card-like container
    with st.container():
        st.markdown("""
        <div style="background: white; border-radius: 12px; padding: 25px; box-shadow: 0 6px 18px rgba(0,0,0,0.1);">
            <h2 style="color: #2a3f5f; margin-bottom: 20px;">📍 Trip Details</h2>
        """, unsafe_allow_html=True)

        with st.form("eta_form"):
            pickup = st.text_input("Pickup Location", placeholder="e.g., Indiranagar, Bangalore")
            drop = st.text_input("Drop Location", placeholder="e.g., Whitefield, Bangalore")

            # Advanced options in expander
            with st.expander("⚙️ Advanced Settings", expanded=False):
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

            submitted = st.form_submit_button("🚀 Calculate ETA", use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

# Handle form submission
if submitted:
    if not pickup or not drop:
        st.warning("Please enter both pickup and drop locations")
    else:
        with st.spinner("🚦 Analyzing traffic patterns..."):
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

                        with col2:
                            # Display results in a beautiful card layout
                            with st.container():
                                st.markdown("""
                                <div style="background: white; border-radius: 12px; padding: 25px; box-shadow: 0 6px 18px rgba(0,0,0,0.1);">
                                    <h2 style="color: #2a3f5f; margin-bottom: 20px;">📊 Journey Analysis</h2>
                                """, unsafe_allow_html=True)

                                # Metrics in a grid
                                m1, m2, m3 = st.columns(3)
                                with m1:
                                    st.markdown(f"""
                                    <div class="metric-card">
                                        <div class="metric-value">{result['eta']}</div>
                                        <div class="metric-label">Standard ETA</div>
                                    </div>
                                    """, unsafe_allow_html=True)

                                with m2:
                                    st.markdown(f"""
                                    <div class="metric-card">
                                        <div class="metric-value">{result['adjusted_eta']} min</div>
                                        <div class="metric-label">Adjusted ETA</div>
                                    </div>
                                    """, unsafe_allow_html=True)

                                with m3:
                                    st.markdown(f"""
                                    <div class="metric-card">
                                        <div class="metric-value">{result['distance']}</div>
                                        <div class="metric-label">Distance</div>
                                    </div>
                                    """, unsafe_allow_html=True)

                                # Traffic visualization
                                st.markdown("""
                                <div style="margin: 25px 0;">
                                    <h4 style="color: #2a3f5f; margin-bottom: 10px;">🚦 Traffic Conditions</h4>
                                """, unsafe_allow_html=True)

                                # Progress bar with custom styling
                                progress_html = f"""
                                <div style="margin-bottom: 10px;">
                                    <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                                        <span>Traffic Intensity</span>
                                        <span>{result['traffic_multiplier']:.2f}x</span>
                                    </div>
                                    <div style="height: 10px; background: #e9ecef; border-radius: 5px; overflow: hidden;">
                                        <div style="height: 100%; width: {min(result['traffic_multiplier'] / 3 * 100, 100)}%; 
                                            background: linear-gradient(90deg, #4e73df 0%, #224abe 100%);"></div>
                                    </div>
                                </div>
                                """
                                st.markdown(progress_html, unsafe_allow_html=True)

                                # Route information
                                st.markdown("""
                                <div style="margin: 25px 0;">
                                    <h4 style="color: #2a3f5f; margin-bottom: 10px;">🗺 Route Information</h4>
                                    <div class="info-box">
                                        {route_info}
                                    </div>
                                </div>
                                """.format(route_info=result['route_info']), unsafe_allow_html=True)

                                # Raw JSON in expander
                                with st.expander("🔍 View Raw API Response"):
                                    st.json(data)

                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.error(f"🚨 API Error: {data.get('error', 'Unknown error')}")
                else:
                    st.error(f"🚨 API Request Failed (Status {response.status_code})")
                    with st.expander("Show Error Details"):
                        st.json(response.json())

            except requests.exceptions.RequestException as e:
                st.error(f"🌐 Connection Error: {str(e)}")
            except Exception as e:
                st.error(f"⚠️ An unexpected error occurred: {str(e)}")

# Add some instructions in the sidebar
with st.sidebar:
    st.markdown("""
    <div style="padding: 20px;">
        <h2 style="color: #2a3f5f;">ℹ️ How to Use</h2>
        <ol style="color: #6c757d; padding-left: 20px;">
            <li style="margin-bottom: 10px;">Enter pickup & drop locations</li>
            <li style="margin-bottom: 10px;">Adjust day/time if needed</li>
            <li style="margin-bottom: 10px;">Click "Calculate ETA"</li>
            <li>View detailed traffic analysis</li>
        </ol>

        <div style="margin-top: 30px; padding: 15px; background: rgba(78, 115, 223, 0.1); border-radius: 8px;">
            <p style="font-weight: 600; color: #2a3f5f;">💡 Pro Tip:</p>
            <p style="color: #6c757d;">Use the advanced settings to see how traffic varies by time of day and week.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px; color: #6c757d;">
    <hr style="border-top: 1px solid #e9ecef; margin-bottom: 15px;">
    <p>Powered by Streamlit • Real-time Traffic Analysis</p>
</div>
""", unsafe_allow_html=True)