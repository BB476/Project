import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(
    page_title="All Readings",
    page_icon="✅",
    layout='wide', )

st.title("All Previously Recorded Data")
data = pd.read_csv("Data.csv")

list = data.columns.tolist()
choice = st.multiselect("Choose Data type", list, default="Volatile Materials")
ddata = data[choice]
st.line_chart(ddata)








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




