import streamlit as st
import numpy as np
import pandas as pd

st.write('# Sample App')
left_column, right_column = st.columns(2)

with left_column:
    number = st.slider("Pick a number", 0, 100)
    file = st.file_uploader("Pick a file")

with right_column:
    pet = st.radio("Pick a pet", ['Dog', 'Cat', 'Bird'])
    date = st.date_input("Pick a date")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.area_chart(chart_data)