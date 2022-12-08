# importing libraries
import gspread
import streamlit as st
import pandas as pd
from gspread_pandas import Spread, Client
from google.oauth2 import service_account
from PIL import Image

# setting page config
st.set_page_config(
    page_title="Plant Database",
    page_icon="🌸",
    layout='wide', )
st.title("Data For Endemic Plants")

# hiding streamlit watermark
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Creating the plant data viewing feature
Choice = st.selectbox("Choose Species", ["Rosa Arabica", "Primula Boveana", "Bufonia Multiceps", "Silene Schimperiana", "Hypericum Sinaicum"], index = 3 ) 

if Choice == "Hypericum Sinaicum":
  Hyper_Image = Image.open('Images/hyper.jpeg')
  col1, col2, col3 = st.columns(3)
  with col1:
      st.markdown('*Hypericum Sincaicum*  is found in the Sinai Peninsula, This endangered plant is very special due to it’s Anti-inflammatory and antioxidant activity, a study conducted was analyzed for its phenolic compounds profiling using HPLC and colorimetric methods. The total phenol content of ME was 158.60 ± 0.74 (μg GAE/mg D.E.), while the total flavonoid content was 70.91 ± 0.01 (μg QE/mg D.E.). phenol is primarily indicated for minor sore throat pain, sore mouth, minor mouth irritation, and pain associated with canker sores, this makes protection of *Hypericum Sinaicum* very important to support the  pharmaceutical  sector.')
  with col2: 
   st.image(Hyper_Image, width= 750)
   
if Choice == "Rosa Arabica":
  Rosa_Image = Image.open('Images/rosa.jpg')
  col1, col2, col3 = st.columns(3)
  with col1:
      st.markdown('*Rosa Arabica* is a species of rose in the plant family of the Rosaceae, endemic to the Mount Catherine region in the south of the Sinai in Egypt.[2] The species is considered critically endangered, as the total global count was only 90 specimen in 2015, Rosa Arabica has many uses, the flowers and leaves are used to reduce mensturial pain, and the whole plant is used to cure reproduction trouble in donkeys, sheep and camels.')
  with col2: 
   st.image(Rosa_Image, width= 750)
   
if Choice == "Primula Boveana":
    Primula_Image = Image.open('Images/primula.jpg')
    col1, col2, col3 = st.columns(3)
    with col1:
      st.markdown('*Primula Boveana*, also known as the Sinai primrose, is a species of flowering plant within the family Primulaceae. Primula Boveana qualifies as Critically Endangered because it is endemic to a tiny area (with an EOO of 13 km2 and AOO of less than 6 km2), The number of mature specimen was 137 in 2020, The species is not commercially or traditionally used in Sinai, but it has been collected for pharmacological testing by various scientific research centers.')
    with col2: 
      st.image(Primula_Image, width= 750)
      
if Choice == "Bufonia Multiceps":
    Bufonia_Image = Image.open('Images/bufonia.jpg')
    col1, col2, col3 = st.columns(3)
    with col1:
      st.markdown('*Bufonia Multiceps* qualifies as Endangered because it is endemic to a tiny area (with an EOO of 337 km² and an AOO of 120 km²) of the high mountain area of the St. Katherine Protectorate in southern Sinai, Egypt. The species is distributed in just two locations; based on the consequences of climate change specifically sudden flooding and long lasting drought, The total population size is less than 2500, and the number of mature individuals in each subpopulation is less than 250. This species has a ethnoveterinary use, defined as an indigenous animal healthcare system that includes the traditional beliefs, knowledge, skills, methods and practices of a given society')
    with col2: 
      st.image(Bufonia_Image, width= 500)
      
if Choice == "Silene Schimperiana":
    Silene_Image = Image.open('Images/silene.jpg')
    col1, col2, col3 = st.columns(3)
    with col1:
      st.markdown('*Silene Schimperiana* is a perennial herb endemic to Sinai. Both have economic importance as fodder for domestic animal beside the medical significance. This plant grows in very narrow microhabitats inside the study area (the only site for this species all over the world) with estimated EOO less than 300 km2. This species is severely threatened by both natural (aridity of the area and climate change) and human factors (Over collection, scientific research, and over-grazing). All these factors are pushing it to the brink of extinction, however the plant has many medical uses due to it containing flavanoids that  showed significant antioxidant activity, anticancer and antitumor activity, hepatoprotective activity, anti-inflammatory activity, anti-diabetes activity, antiviral activity, antibacterial and antifungal activity, and other biological effects. ')
    with col2: 
      st.image(Silene_Image, width= 550)