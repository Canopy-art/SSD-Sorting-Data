import streamlit as st

#Home Page Button
st.page_link("Home_Page.py", label="🔙 Home")

# Diversity Image
st.image("data/Network-Diversity.png", caption="Scource: sinch.com", width=680)

#About Page text
st.markdown("# About our website:")
st.markdown("""WebPopulus records how diverse the Internet is. This website uses global data on Internet usage per location and PCI (Income Per Person) to develop graphs that reveal how much the Internet is utilized all over the world. During this research, we found that most of the internet’s users are located in North America and Europe, with the majority of the planet having (in comparasion) minimal access or usage of the internet. With how much the Internet is used nowadays from communication to entertainment, this lack of connection with the greater world can hinder the development of underdeveloped areas around the planet. This website is designed as a tool 


People in these areas might have harder times getting well paying jobs, sharing information about what might be happening in their countries, and gaining further information about the outside world. This lack of communication would effectively isolate them (in a sense) from the rest of the world. Using the global data, WebPopulus looks for possible reasons and solutions to the world's unequal access to the Internet. Further diversifying the Internet would allow for more job opportunities globally and more voices to be heard around the planet, raising global awareness of possible human rights violations happening all over the world.
 """)