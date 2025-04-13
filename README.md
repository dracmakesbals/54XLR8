## ETA Calculator
## Features
- ✨ **Modern UI** with gradient background and card-based design
- 📍 **Location input** for pickup and drop points
- ⏱️ **Traffic-adjusted ETAs** with multiplier visualization
- 📊 **Route information** display
- ⚙️ **Advanced options** for day/time selection
- 📱 **Fully responsive** layout
- 🔄 **Real-time API integration**
## Requirements
- Python 3.7+
- Streamlit
- Requests
## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/eta-calculator.git
cd eta-calculator 
```
2. Install dependencies:
```bash 
pip install streamlit requests
```
## Usage
Run the application:
```bash
streamlit run eta_calculator.
```
## Configuration
Edit these variables in the code:
```bash
API_URL = "your_api_endpoint_here"
```
## How It Works
1. User enters pickup and drop locations
2. Optionally adjusts day/time parameters
3. Application sends request to the ETA API
4. Displays results with traffic-adjusted ETAs

## Customization
Modify:

- Color scheme in the CSS section
- API endpoint
- Layout components

## Troubleshooting
If issues occur:

- Verify API endpoint
- Check internet connection
- Ensure dependencies are installed
