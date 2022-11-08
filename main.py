import streamlit as st


st.set_page_config(
    page_title="-projectname- HomePage",
    page_icon="🏠",
    layout="centered",
)
st.title("**-projectname- v0.2**")
st.text("This website was made by Group (), Ismailia stem school, 2022/2023 ")
st.text("Use the sidebar to navigate")
st.text("This project is aimed to help in reducing the effects of climate change ")
st.text("and saving endangered Plants that are endemic to Sinai")




hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



