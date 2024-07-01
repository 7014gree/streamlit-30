import streamlit as st
# from datetime import time, datetime
import numpy as np
# import altair as alt
import pandas as pd


st.header('st.checkbox')

st.write('What would you like to order?')

icecream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("Great! Here's some more :icecream:")

if coffee:
    st.write("Okay, here's some coffee :coffee:")

if cola:
    st.write("Here you go :cup_with_straw:")