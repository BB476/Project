# importing libraries
import gspread
import pandas
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

