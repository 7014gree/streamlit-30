import streamlit as st
# from datetime import time, datetime
import numpy as np
# import altair as alt
import pandas as pd


st.header('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)