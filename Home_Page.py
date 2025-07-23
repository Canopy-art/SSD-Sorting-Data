import streamlit as st
import pandas as pd

# Home page setup
st.set_page_config(page_title="WebPopulus") # Formating

st.set_page_config(
    page_title="WebPopulus",
    layout="centered",
    initial_sidebar_state="collapsed"
)

#Importing Logo
# Place image at the top as your title
st.image("data/Logo.png", width=420)  # Adjust width as needed
st.write("Welcome to WebPopulus were you can learn about the diversity of the internet!")

# Dynamic UI
page = st.selectbox("Use this to navigate our website to learn more about the world's internet usage!", ["WebPopulus", "Internet per Continent", "About", "Internet Usage Based on Income per Person"])

#if page == "WebPopulus":

if page == "Internet per Continent":
    st.switch_page("pages/Internet-per-Continent.py")
elif page == "About":
    st.switch_page("pages/About.py")
elif page == "Internet Usage Based on Income per Person":
    st.switch_page("pages/Income_Scatterplot.py")