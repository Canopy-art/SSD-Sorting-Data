import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Link Data
url = "https://psychic-space-funicular-gj57pww75gxfwv4v-5000.app.github.dev/income_per_person"
response = requests.get(url)

# Title
st.title("Internet Usage Based on Income per Person")
st.page_link("Home_Page.py", label="🔙 Home")

#import API
@st.cache_data
def fetch_data(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()
try:
    data = fetch_data(url)
except Exception as e:
    st.error(f"Error fetching data: {e}")
    st.stop()

#Transform the JSON API into a dataframe
#st.write(f"Type of countries for {continent}: {type(countries)}")
#for countries in data.items():
records = []
for country, value in data.items():
        # Skip missing or invalid values
        if value is not None and not (isinstance(value, float) and np.isnan(value)):
            records.append({
                "Country": country,
                "Income": value })
df = pd.DataFrame(records)

# Remove NaN and missing values
dataframe_clean = df.dropna(subset=["Income"])

# Show data preview
if st.checkbox("Show data table"):
    st.dataframe(dataframe_clean)

# Create plot
fig, ax = plt.subplots()
ax.scatter(dataframe_clean['Income'], dataframe_clean['Country'])  # Adjust 'x' and 'y' to match your actual column names
ax.set_xlabel("Income-per-Person")
ax.set_ylabel("Countries")
ax.set_title("API Internet per Income Data Scatterplot")

# Show in Streamlit
st.pyplot(fig)

# Explain Data
st.markdown(""" This figure is a scatterplot on the Internet usage based on PCI(Income per Person).


""")