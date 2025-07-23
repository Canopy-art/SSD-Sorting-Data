import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Link data
url = "https://psychic-space-funicular-gj57pww75gxfwv4v-5000.app.github.dev/gapminder"

# Set page title
st.title("Internet usage per continent")
st.page_link("Home_Page.py", label="🔙 Home")

# Import API
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

# Transform the JSON structure into a DataFrame
records = []
for continent, countries in data.items():
    for country, value in countries.items():
        # handle NaN string and None
        if value is not None and not (isinstance(value, float) and np.isnan(value)):
            records.append({"Continent": continent, "Country": country, "Value": value})
df = pd.DataFrame(records)

# Remove NaN and missing values
df = df.dropna(subset=["Value"])

# Show data preview
if st.checkbox("Show data table"):
    st.dataframe(df)

# Draw the box plot
fig, ax = plt.subplots(figsize=(10, 6))
df.boxplot(column="Value", by="Continent", ax=ax)
plt.title("Internet Usage by Continent")
plt.suptitle("")  # Remove the default subtitle
plt.ylabel("Internet Usage (%)")
plt.xlabel("Continent")
plt.xticks(rotation=45)
st.pyplot(fig)

# Explain Data
st.markdown(""" This graph shows the range of how much each continent uses the Internet. One can easily see that Europe and North America use the Internet the most, followed by South America and Asia. This makes sense because most content on the Internet is from North America (America and Canada), (Western)Europe, and East Asia.

### Possible Reasons For This
This lack of Internet usage in Africa, Oceania, and other locations like Central Asia and Eastern Europe is possilbly due to the lack of fiber optics cables in these regions.  Fiber optic cables are underwater cables that allow for information (the Internet) to travel between different continents. These cables are heavily focused in North America, Western Europe, and East Asia.

Source: Kentik.com

### Solutions
Possible solutions to this problem could be to lay down more of these cables in these other regions. This solution, although it appears most logical, could harm the underwater environment in these regions. A better solution could actually be to find an alternative to getting Internet access to these locations. Satellites or Fixed Wireless (Internet transmitted over radio) are possible solutions.

Source: Eufy.com
""")