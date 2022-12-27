import streamlit as st
from streamlit_lottie import st_lottie
import json
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(
    page_title="Group 17318 HomePage",
    page_icon="🏠",
    layout="centered",
)
st.title("Analyzing the impacts of climate change on the endangered species *Silene Schimperiana* in the St. Catherine region in Sinai")
st.caption("V. 1.0")
st.markdown("This project was created by group 17318, Ismailia STEM, for the school year 2022/2023.")
st.markdown("This project aims to help in reducing the effects of climate change and saving endangered plants that are endemic to Sinai, such as the *Silene Schimperiana* species and many others.")

st.text("Use the sidebar to navigate")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_plant = load_lottiefile("plant.json")
st_lottie(lottie_plant)

# -------------------------------

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

data = pd.DataFrame([[22.7, 49.9, 44], [22.3, 50.6, 45], [23, 52.7, 44.6], [24, 52, 45], [23.2, 51.6, 44.2], [23, 51, 44.7], [24, 49, 44.2], [22, 52, 44.7], [21, 52, 44.6], [20.9, 53, 44.1]],
                    columns=['x', 'y', 'z'])
ax.scatter(data['x'], data['y'], data['z'], c='blue')

# Linear regression
X = data[['x', 'y', 'z']].values
Xlen = X.shape[0]
avgPointCloud = 1 / Xlen * np.array([np.sum(X[:, 0]), np.sum(X[:, 1]), np.sum(X[:, 2])])
Xmean = X - avgPointCloud

cov = 1 / Xlen * X.T.dot(Xmean)

t = np.arange(-5, 5, 1)
linearReg = avgPointCloud + cov[:, 0] * np.vstack(t)

ax.plot(linearReg[:, 0], linearReg[:, 1], linearReg[:, 2], 'r', label='Linear Regression')
ax.legend()

plt.show()
# -------------------------------------




hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



