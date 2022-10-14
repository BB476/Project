# importing libraries
import streamlit as st
import gspread
import pandas
import pandas as pd
from gspread_pandas import Spread, Client
from google.oauth2 import service_account

# setting page config
st.set_page_config(
    page_title="Latest Reading",
    page_icon="🕐",
    layout = "wide"
)

st.title("Here you can view the latest data recorded:")

#fetching data from google sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"], scopes=scope)
client = Client(scope=scope, creds=credentials)
spreadsheetname = "CapStone"
spread = Spread(spreadsheetname, client=client)
sh = client.open("CapStone")
wks = sh.worksheet("Sheet1")

# creating a df from sheet
df = pd.DataFrame(wks.get_all_records())

# Viewing last row
lastrow = df.iloc[-1:]
st.dataframe(lastrow, width= int("2000"), height = int("50"))

# success message after every rerun/run
st.success("Renewed All Data")

# reload button
col1, col2, col3 = st.columns(3)
if col2.button(label="Click Here To Refresh"):
    st.experimental_rerun()

# hiding streamlit watermark
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
