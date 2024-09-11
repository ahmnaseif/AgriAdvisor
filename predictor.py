import streamlit as st
from model import predict_price
from weather import get_weather
from llm import get_llm_response, translate_to_sinhala
from crop_data import generate_sentences
import datetime

# Streamlit app
st.set_page_config(page_title="AI-Powered Agricultural Advisor", page_icon='')

# Add a floating "Predictor" button in the bottom-right corner
st.markdown(
    """
    <style>
    /* Floating button */
    .float-button {
        position: fixed;
        width: 80px;
        height: 60px;
        bottom: 40px;
        right: 40px;
        background-color: #4CAF50;
        color: white;
        border-radius: 60px;
        text-align: center;
        font-size: 18px;
        box-shadow: 2px 2px 3px #999;
        z-index: 100;
    }

    /* Button hover effect */
    .float-button:hover {
        background-color: #45a049;
        color: white;
    }

    /* Link for floating button */
    .float-button a {
        color: white;
        text-decoration: none;
        line-height: 60px;
        display: block;
    }
    </style>

    <div class="float-button">
        <a href="/predictor">Advisor</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Predict the price and weather!")

#question = st.text_area("Ask your question about agriculture...", height=300)
crop = st.selectbox("Select a crop", options=['Carrot', 'Leeks', 'Beetroot', 'Brinjal', 'Ladies Finger'])
date = st.date_input("Select a date", datetime.date.today())
location = st.text_input("Enter your location (optional):")
details = ""

if st.button("Get Prediction"):        

    predicted_price = predict_price(crop, date, location)
    price_te = f"Predicted Price for {crop} on {date}: LKR {predicted_price:.2f}"
    st.session_state['price_info'] = price_te
    details += f"Predicted Price for {crop} on {date}: LKR {predicted_price:.2f}"
    

        # Fetch weather information if location provided
    if location:
            weather_data = get_weather(location)
            if weather_data:
                weather_info = f"Weather in {location}: {weather_data['weather'][0]['description']}, Temp: {weather_data['main']['temp']}°C"
                st.session_state['weather_info'] = weather_info  # Store weather info in session state
                details += f"Weather in {location}: {weather_data['weather'][0]['description']}, Temp: {weather_data['main']['temp']}°C"
                       

    get_llm = get_llm_response("Act as an agricultural expert. I am Sri Lankan. Give in detail for the following content: " + details) 
    st.session_state['get_llm'] = get_llm 
    price_info = st.session_state.get('predicted_price')
    weather_info = st.session_state.get('weather_info')
    predicted_prices = st.session_state.get('price_info')
    st.info(get_llm)
    st.success(predicted_prices)
    st.info(weather_info) 
    
    
        
        
