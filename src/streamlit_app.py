import streamlit as st
import pandas as pd

st.write(
    """
# GECI
Hello world
V3
"""
)
df = pd.read_csv("tests/data/estaciones_guadalupe.csv")
st.line_chart(df, x="Time", y="Temp_Out")
