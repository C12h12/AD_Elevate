import streamlit as st
st.set_page_config(layout="wide")

from pages.navbar import render_navbar
from pages.enhance import enhance_func
render_navbar()

st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important;
            margin-top: 0rem !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; margin-top: 20px; margin-bottom: 0px !important;">
        <h1 style="color: #ffffff; font-size: 40px;">Enhance your campaign with AdElevate AI</h1>
        <p style="color: #ffffff; font-size: 20px;">Enter your ideas and texts to refine, our AI turns them into compelling,<br> high-converting content in seconds.</p>
    </div>
""", unsafe_allow_html=True)


# Custom CSS for styling
st.markdown("""
<style>
    html, body, .main, .block-container {
    padding-top: 0rem !important;
    margin-top: 0rem !important;
}
            
/* Text area styling */
textarea {
    margin-top: 0px !important;
    min-height: 60px;
    max-height: 300px;
    padding: 12px;
    font-size: 16px;
    border-radius: 8px;
    border: 1px solid #ccc;
    resize: vertical;
    width: 100%;
}

/* Button styling */
.stButton > button {
    height: 44px;
    padding: 0 30px;
    font-size: 16px;
    border: none;
    background-color: #10a37f;
    color: white;
    border-radius: 6px;
    cursor: pointer;
    margin: 0 auto;
    display: block;
}

.stButton > button:hover {
    background-color: #0e8a6a;
    font-weight: bold;
    color: #ffffff;
}

/* Add top margin for spacing */
.top-margin {
    margin-top: 1px;
}
</style>
""", unsafe_allow_html=True)

#st.markdown('<div class="top-margin"></div>', unsafe_allow_html=True)

# Create a 3-column layout with the middle column for content
col1, col2, col3 = st.columns([1, 2, 1])

# Place the text area in the middle column
with col2:
    enhance_func()
    