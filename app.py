import pandas as pd
import streamlit as st

st.title("Dashboard de Chamados de TI")

df = pd.read_csv("chamados_ficticios.csv")

total = len(df)
tempo_medio = df["horas_resolucao"].mean()

st.metric("Total de chamados", total)
st.metric("Tempo médio (h)", round(tempo_medio, 1))