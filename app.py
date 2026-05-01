import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Título de la app
st.header('Análisis de anuncios de venta de coches')

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Checkbox histograma
hist_checkbox = st.checkbox('Mostrar histograma del odómetro')

if hist_checkbox:
    st.write('Distribución del odómetro')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title='Histograma del odómetro')

    st.plotly_chart(fig, use_container_width=True)

# Checkbox scatter
scatter_checkbox = st.checkbox(
    'Mostrar gráfico de dispersión precio vs odómetro')

if scatter_checkbox:
    st.write('Relación entre precio y odómetro')

    fig2 = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers'
    )])

    fig2.update_layout(title='Precio vs Odómetro')

    st.plotly_chart(fig2, use_container_width=True)
