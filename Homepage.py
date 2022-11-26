import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json

st.set_page_config(
    page_title="Group 17318 HomePage",
    page_icon="🏠",
    layout="centered",
)
st.title("Analyzing the impacts of climate change on the endangered species *Hypericum Sinaicum*")
st.caption("V. 1.0")
st.markdown("This project was created by group 17318, Ismailia STEM, for the school year 2022/2023.")
st.markdown("This project aims to help in reducing the effects of climate change and saving endangered plants that are endemic to Sinai, such as the *Hypericum Sinaicum* species.")

st.text("Use the sidebar to navigate")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_plant = load_lottiefile("plant.json")
st_lottie(lottie_plant)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



