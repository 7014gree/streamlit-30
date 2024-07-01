import streamlit as st
# from datetime import time, datetime
import numpy as np
# import altair as alt
import pandas as pd


st.header('st.multiselect')

options = st.multiselect(
    "What are your favourite colours:",
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write("You selected:", ', '.join(options))