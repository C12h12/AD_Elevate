import streamlit as st
st.set_page_config(layout="wide")

from pages.navbar import render_navbar
render_navbar()

st.markdown("""
    <div style="text-align: center; margin-top: 60px;">
        <h1 style="color: #ffffff; font-size: 40px;">Get Performance Prediction</h1>
        <p style="color: #ffffff; font-size: 20px;">Simply enter your campaign text and we will analyze and predict how well your campaign can do based on <br> our high-tech machine learnings model and neatly gathered data.</p>
    </div>
""", unsafe_allow_html=True)


# Custom CSS for styling
st.markdown("""
<style>
/* Text area styling */
textarea {
    margin-top: 20px;
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
    margin-top: 80px;
}
</style>
""", unsafe_allow_html=True)

# Add top margin
st.markdown('<div class="top-margin"></div>', unsafe_allow_html=True)

# Create a 3-column layout with the middle column for content
col1, col2, col3 = st.columns([1, 2, 1])

# Place the text area in the middle column
with col2:
    query = st.text_area("Search", label_visibility="collapsed", 
                         placeholder="Enter your campaign text...", 
                         key="search_input")
    
    # Button placed in same column for alignment
    submitted = st.button("Enter")
    
    # Handling results
    if submitted and query:
        st.success(f"Searching for: {query}")
    elif submitted:
        st.warning("Please enter a message.")