import streamlit as st
# from datetime import time, datetime
import numpy as np
# import altair as alt
import pandas as pd


st.header('st.selectbox')

option = st.selectbox(
    "What is your favourite colour:",
    ('Red', 'Blue', 'Green')
)

st.write("Your favourite colour is ", option)