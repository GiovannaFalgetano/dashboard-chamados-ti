import pandas as pd
import streamlit as st

st.title("Dashboard de Chamados de TI")

df = pd.read_csv("chamados_ficticios.csv")

st.write(df.head())