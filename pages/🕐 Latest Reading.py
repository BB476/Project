# importing libraries
import streamlit as st
import pandas as pd
from gspread_pandas import Spread, Client
from google.oauth2 import service_account


# setting page config
st.set_page_config(
    page_title="Latest Reading",
    page_icon="🕐",
    layout="wide"
)

st.title("Latest data:")

#-------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------

# creating a df from sheet
df = pd.DataFrame(wks.get_all_records())
dft = df[['Temperature(°C)']].copy()
dfh = df[['Humidity(%)']].copy()
dfs = df[['Soil Moisture(PPM)']].copy()

#--------------------------------------------------------------------------

# Viewing last row
temp_last = df.iloc[-1, 1]
temp_last2 = str(temp_last)
Humid_last = df.iloc[-1, 2]
Humid_last2 = str(Humid_last)
soil_last = df.iloc[-1, 3]
soil_last2 = str(soil_last)
col11, col22, col33 = st.columns(3)
col11.metric(label="Temperature", value= temp_last2 + "°C")
col22.metric(label= "Humidity", value= Humid_last2 + "%")
col33.metric(label="Soil Moisture", value= soil_last2 + " PPM")

# warning for high temp and humidity
temp22 = int(temp_last)
humid22 = int(Humid_last)
if temp22 > 25 or humid22 > 60:
 st.error("Temperature and Humidty levels might be harmfull to Hypericum Sinaicum")
 
#-------------------------------------------------------------------------------------
   
#  last 3 days average temperature
dft3 = dft.tail(3)
dft3 = dft3.mean(axis = 0)
dft3 = dft3.iloc[0]
dft3 = round(dft3, 1)
dft3 = str(dft3)

# last 3 days average humidity
dfh3 = dfh.tail(3)
dfh3 = dfh3.mean(axis = 0)
dfh3 = dfh3.iloc[0]
dfh3 = round(dfh3, 1)
dfh3 = str(dfh3)

# last 3 days average soil moisture
dfs3 = dfs.tail(3)
dfs3 = dfs3.mean(axis = 0)
dfs3 = dfs3.iloc[0]
dfs3 = round(dfs3, 1)
dfs3 = str(dfs3)

# -----------------------------------------------------------------

#  last 7 days average temperature
dft7 = dft.tail(7)
dft7 = dft7.mean(axis = 0)
dft7 = dft7.iloc[0]
dft7 = round(dft7, 1)
dft7 = str(dft7)

# last 7 days average humidity
dfh7 = dfh.tail(7)
dfh7 = dfh7.mean(axis = 0)
dfh7 = dfh7.iloc[0]
dfh7 = round(dfh7, 1)
dfh7 = str(dfh7)

# last 7 days average soil moisture
dfs7 = dfs.tail(7)
dfs7 = dfs7.mean(axis = 0)
dfs7 = dfs7.iloc[0]
dfs7 = round(dfs7, 1)
dfs7 = str(dfs7)

#Viewing last 3 and 7 days average 
Choice = st.selectbox("Choose Species", ["Last 3 Days", "Last 7 Days"], index = 0 ) 
if Choice == 'Last 7 Days' :
 st.title('Last 7 days average')
 col111, col222, col333 = st.columns(3)
 col111.metric(label="Temperature", value= dft3 + "°C")
 col222.metric(label= "Humidity", value= dfh3 + "%")
 col333.metric(label= "Soil Moisture", value= dfs3 + " PPM")

if Choice == 'Last 3 Days':
 st.title('Last 3 days average')
 col111, col222, col333 = st.columns(3)
 col111.metric(label="Temperature", value= dft3 + "°C")
 col222.metric(label= "Humidity", value= dfh3 + "%")
 col333.metric(label= "Soil Moisture", value= dfs3 + " PPM")
#-----------------------------------------------------------------------------------

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

