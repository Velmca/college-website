import streamlit as st
import streamlit.components.v1 as components

# Configure page layout
st.set_page_config(
    page_title="College Portal",
    page_icon="🎓",
    layout="wide"
)

# Function to read local HTML file
def render_html_page(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Load and render your HTML file
try:
    html_data = render_html_page("index.html")
    components.html(html_data, height=1000, scrolling=True)
except FileNotFoundError:
    st.error("Error: 'index.html' not found. Please ensure it is placed in the same folder as app.py.")
