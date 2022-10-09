import streamlit as st


st.set_page_config(
    page_title="-projectname- HomePage",
    page_icon="🏠",
)
st.title("**-projectname- v0.1**")
st.text("This website was made by Group (), Ismailia stem school, 2022/2023 ")
st.text("Use the sidebar to navigate")




hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



