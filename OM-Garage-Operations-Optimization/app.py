import streamlit as st
import streamlit.components.v1 as components

# Make the app use the full screen width
st.set_page_config(layout="wide", page_title="Car Detailing Operations Simulator")

# Read your HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the HTML dashboard
components.html(html_content, height=1200, scrolling=True)
