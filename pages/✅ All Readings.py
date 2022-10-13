import gspread
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


st.set_page_config(
    page_title="All Readings",
    page_icon="✅",
    layout='wide', )
st.title("All Previously Recorded Data")
sa = gspread.service_account()
sh = sa.open("CapStone")
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




