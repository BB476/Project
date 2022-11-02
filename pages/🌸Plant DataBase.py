# importing libraries
import gspread
import streamlit as st
import pandas as pd
from gspread_pandas import Spread, Client
from google.oauth2 import service_account

# setting page config
st.set_page_config(
    page_title="Plant Database",
    page_icon="🌸",
    layout='wide', )
st.title("Data For Endemic Plants")

# hiding streamlit watermark
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
