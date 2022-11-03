# importing libraries
import streamlit as st
import gspread
import pandas
import pandas as pd
from gspread_pandas import Spread, Client
from google.oauth2 import service_account
import smtplib, ssl

# setting page config
st.set_page_config(
    page_title="Latest Reading",
    page_icon="🕐",
    layout="wide"
)

st.title("latest data:")

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

# Viewing last row
lastrow = df.iloc[-1:]
st.dataframe(lastrow, width=int("2000"), height=int("50"))

# success message after every rerun/run
st.success("Renewed All Data")

# reload button
col1, col2, col3 = st.columns(3)
if col2.button(label="Click Here To Refresh"):
    st.experimental_rerun()

# last 3 days average
average3 = df.tail(3)
average3.drop(columns=average3.columns[0], axis=1, inplace=True)
df3 = average3.mean(axis=0)
st.title("Last 3 days average:")
st.dataframe(df3, width=2000, height=100)

# last 7 days average
average = df.tail(7)
average.drop(columns=average.columns[0], axis=1, inplace=True)
df2 = average.mean(axis=0)
st.title("Last 7 days average:")
st.dataframe(df2, width=2000, height=100)

# reload button
col4, col5, col6 = st.columns(3)
if col5.button(label="Click Here To Refresh", key = "as"):
    st.experimental_rerun()

# hiding streamlit watermark
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#sending the warning by email
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "ammar25257@gmail.com"
receiver_email = "ammar25257@gmail.com"
password = "@ammar25257@gmail.com"
message = """\
Subject: Altert regarding the state of Hypericum Sinaicum

An alarming rise in temperature and humidty was detected, Taking the required actions in preserving the species is urgent"""
temp_last = df.iloc[0, df.columns.get_loc('Temperature(°C)')]
Humid_last = df.iloc[0, df.columns.get_loc('Humidity(%)')]
context = ssl.create_default_context()
if temp_last > 45 and Humid_last > 60:
 with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)