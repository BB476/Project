import gspread
import streamlit as st
import pandas as pd
from gspread_pandas import Spread,Client
from google.oauth2 import service_account


st.set_page_config(
    page_title="All Readings",
    page_icon="✅",
    layout='wide', )
st.title("All Previously Recorded Data")
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_info(
                st.secrets["gcp_service_account"], scopes = scope)
client = Client(scope=scope,creds=credentials)
spreadsheetname = "CapStone"
spread = Spread(spreadsheetname,client = client)
sh = client.open("CapStone")

wks= sh.worksheet("Sheet1")
df = pd.DataFrame(wks.get_all_records())
df.set_index("date")



list = df.columns.tolist()

choice = st.multiselect("Choose Data type", list, default="Temperature")

datas = df[choice]
st.line_chart(datas)



st.success("Renewed All Data")
col1, col2, col3 = st.columns(3)
if col2.button(label = "Click Here To Refresh"):
    st.experimental_rerun()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)




