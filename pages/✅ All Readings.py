
# importing libraries
import gspread
import pandas
import streamlit as st
import pandas as pd
from gspread_pandas import Spread, Client
from google.oauth2 import service_account
# setting page config
st.set_page_config(
    page_title="All Readings",
    page_icon="✅",
    layout='wide', )
st.title("Previously Recorded Data")

# importing the Google sheet
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"], scopes=scope)
client = Client(scope=scope, creds=credentials)
spreadsheetname = "yarab"
spread = Spread(spreadsheetname, client=client)
sh = client.open("yarab")
wks = sh.worksheet("Sheet1")

# creating a pandas dataframe using the Google sheet
df = pd.DataFrame(wks.get_all_records())

# making the part where the user chooses which data to view
cols = df.columns.tolist()
cols.remove("Date")
choice = st.multiselect("Choose Data type", cols, default="Temperature(°C)")
datas = df[choice + ["Date"]]


# plotting the choice on a line chart
st.line_chart(datas, x="Date", y=choice)

# success message after every rerun/run
st.success("Renewed All Data")

# reload button
col1, col2, col3 = st.columns(3)
if col2.button(label="Click Here To Refresh"):
    st.experimental_rerun()

st.title("Full Table:")
#view data in table
st.dataframe(df, width= int("2000"), height=int("500"))

# hiding the streamlit watermark
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# making teh last row dataframe
lastrow = df.iloc[-1:]
