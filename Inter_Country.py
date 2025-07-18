import streamlit as st
import pandas as pd
import requests

# Link data
url = "https://psychic-space-funicular-gj57pww75gxfwv4v-5000.app.github.dev/gapminder"

# Set page title
st.title("Internet usage per continent")
st.page_link("Home_Page.py", label="⬅️ Back to Home", icon="🏠")

# Import API
try:
    response = requests.get(url)
    response.raise_for_status()
    st.components.v1.html(response.text, height=100, scrolling=True)
except Exception as e:

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
