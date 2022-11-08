# importing libraries
import streamlit as st
import gspread
import pandas
import pandas as pd
from gspread_pandas import Spread, Client
from google.oauth2 import service_account
import smtplib, ssl
from email.message import EmailMessage

# setting page config
st.set_page_config(
    page_title="Latest Reading",
    page_icon="🕐",
    layout="wide"
)

st.title("Latest data:")

# fetching data from google sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"], scopes=scope)
client = Client(scope=scope, creds=credentials)
spreadsheetname = "yarab"
spread = Spread(spreadsheetname, client=client)
sh = client.open("yarab")
wks = sh.worksheet("Sheet1")

# creating a df from sheet
df = pd.DataFrame(wks.get_all_records())
temp_last = df.iloc[-1, 1]
temp_last2 = str(temp_last)
Humid_last = df.iloc[-1, 2]
Humid_last2 = str(Humid_last)
# Viewing last row
col11, col22 = st.columns(2)
col11.metric(label="Temperature", value= temp_last2 + "°C")
col22.metric(label= "Humidity", value= Humid_last2 + "%")

# warning for high temp and humidity

temp22 = int(temp_last)
humid22 = int(Humid_last)
if temp22 > 45 and humid22 > 60:
 st.error("Temperature and Humidty levels might be harmfull to Hypericum Sinaicum")
   
# last 3 days average
average3 = df.tail(3)
average3.drop(columns=average3.columns[0], axis=1, inplace=True)
df3 = average3.mean(axis=0)
temp_last_3_avg = df.iloc[-1, 1]
temp_last_3_avg_2 = str(temp_last_3_avg)
Humid_last_3_avg = df.iloc[-1, 2]
Humid_last_3_avg_2 = str(Humid_last_3_avg)
st.title("Last 3 days average:")

# Viewing last 3 days average
col111, col222 = st.columns(2)
col111.metric(label="Temperature", value= temp_last_3_avg_2 + "°C")
col222.metric(label= "Humidity", value= Humid_last_3_avg_2 + "%")


# last 7 days average
average = df.tail(7)
average.drop(columns=average.columns[0], axis=1, inplace=True)
df2 = average.mean(axis=0)
st.title("Last 7 days average:")
temp_last_7_avg = df.iloc[-1, 1]
temp_last_7_avg_2 = str(temp_last_7_avg)
Humid_last_7_avg = df.iloc[-1, 2]
Humid_last_7_avg_2 = str(Humid_last_7_avg)


# Viewing last 7 days average
col1111, col2222 = st.columns(2)
col1111.metric(label="Temperature", value= temp_last_3_avg_2 + "°C")
col2222.metric(label= "Humidity", value= Humid_last_3_avg_2 + "%")

# reload button
col4, col5, col6 = st.columns(3)
if col5.button(label="Click Here To Refresh", key = "as"):
    st.experimental_rerun()

# success message after every rerun/run
st.success("Renewed All Data") 

# hiding streamlit watermark
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

