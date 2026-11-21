import os
import streamlit as st

# Get the exact directory where app.py is located
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()
