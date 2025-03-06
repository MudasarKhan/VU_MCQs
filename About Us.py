import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="About Us", page_icon=":tada:")

# Title
st.title("About Us")

# Subtitle
st.subheader("Welcome to Our Amazing Platform!")

# Description
st.write("""
Hello! We're glad you're here. Our mission is to provide you with the best services and experiences. Whether you're here to learn, explore, or just have fun, we've got something for you.

### Our Story
Our journey began with a simple idea: to make a difference in the world. With a team of dedicated professionals, we've grown into a community that values innovation, collaboration, and excellence.

### Our Vision
We envision a world where everyone has access to the tools and resources they need to thrive. Our platform is designed to empower individuals, foster creativity, and drive progress.

### Meet the Team
Our team is composed of talented individuals from diverse backgrounds. Together, we bring a wealth of knowledge and expertise to the table.

- **John Doe**: Founder & CEO
- **Jane Smith**: Chief Technology Officer
- **Bob Brown**: Head of Marketing

### Get in Touch
We'd love to hear from you! If you have any questions, feedback, or just want to say hello, feel free to reach out to us at [contact@ourplatform.com](mailto:contact@ourplatform.com).
""")

# Add a custom footer
st.markdown("""
<style>
footer {
    background-color: #f5f5f5;
    padding: 10px;
    text-align: center;
    color: #333333;
    font-size: 12px;
}
</style>
<footer>
    &copy; 2025 Our Amazing Platform. All rights reserved.
</footer>
""", unsafe_allow_html=True)
from PIL import Image
file_path = r"Logo.PNG"
try:
    logo = Image.open(file_path)
    st.sidebar.image(logo, use_column_width=True)
except FileNotFoundError:
    st.error(f"File '{file_path}' Path Dont Find.")