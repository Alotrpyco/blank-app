import streamlit as st
add_selectbox = st.sidebar.selectbox(
    'O quanto você gosta de estar conectado?',
    ('Email','Home phone', 'Mobile phone')

)

add_slider = st.sidebar.slider(
    'select a range of values', 
    0.0, 100.0, (25.0, 75.0)
)