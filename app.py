import streamlit as st
from model import predict_price
from weather import get_weather
from llm import get_llm_response, translate_to_sinhala
from crop_data import generate_sentences
import datetime

st.set_page_config(page_title="AI-Powered Agricultural Advisor", page_icon='')


st.markdown(
    """
    <style>
    /* Floating button */
    .float-button {
        position: fixed;
        width: 100px;
        height: 60px;
        bottom: 40px;
        right: 60px;
        background-color: #4CAF50;
        color: white;
        border-radius: 20px;
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
        <a href="/predictor">Predictor</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Ask the Agricultural Advisor!")

question = st.text_area("Ask your question about agriculture...", height=200)
# crop = st.selectbox("Select a crop", options=['Carrot', 'Leeks', 'Beetroot', 'Brinjal', 'Ladies Finger'])
# date = st.date_input("Select a date", datetime.date.today())
# location = st.text_input("Enter your location (optional):")



if st.button("Get Advice"):
        date = datetime.date.today()
        crops = ['Carrot', 'Leeks', 'Beetroot', 'Brinjal', 'Ladies Finger']
        details = ""
        for cr in crops:
            if cr.lower() in question.lower():
                details += generate_sentences(cr)

        # LLM
        get_llm = get_llm_response("Act as an agricultural expert. I am Sri Lankan. " + question + ". modify and include following " + details) 
        st.session_state['get_llm'] = get_llm
        st.info(get_llm) 


if st.session_state.get('get_llm'):
    if st.button("Translate to Sinhala"):
        get_llm = st.session_state.get('get_llm')


        combined_text = f"{get_llm}"

        translated_text = translate_to_sinhala(combined_text)
        st.session_state['translated_text'] = translated_text 
        st.info(st.session_state.get('translated_text'))
