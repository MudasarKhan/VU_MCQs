import streamlit as st
from st_social_media_links import SocialMediaIcons

social_media_links = [
    "https://www.youtube.com/@comtechmentor9117",
    "https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F",
    "https://www.instagram.com/"
    "https://www.whatsapp.com/"
]

social_media_icons = SocialMediaIcons(social_media_links)
social_media_icons.render()

st.title("Feel Free to Call Us")
st.subheader("03283254308")


from PIL import Image
file_path = r"Logo.PNG"
try:
    logo = Image.open(file_path)
    st.sidebar.image(logo, use_column_width=True)
except FileNotFoundError:
    st.error(f"File '{file_path}' Path Dont Find.")

