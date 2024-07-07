import streamlit as st
from PIL import Image

hide_menu = """ 
<style>
#MainMenu{
    visibility:hidden;
    background-color: #1c1c1c;
    color: #ffffff;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('icons/logo.png')


st.set_page_config(page_title = "Hate Speech Detection", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.markdown("<h1 style='text-align: center; font-size: 24px;'>Cyberbullying and Hate Speech Detection in Social Media platforms - Defend against cyberbullying in the Social Media</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2024 | Hate Speech Detection </h1>", unsafe_allow_html=True)

st.image(image , use_column_width=True)
