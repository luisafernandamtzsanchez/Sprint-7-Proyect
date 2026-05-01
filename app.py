import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# -----------------------------
# Configuración de la página
# -----------------------------
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

# -----------------------------
# Título y descripción
# -----------------------------
st.title('🚗 Análisis de anuncios de vehículos en EE.UU.')
st.write('Explora cómo el kilometraje afecta el precio de los vehículos.')

# -----------------------------
# Cargar datos
# -----------------------------
car_data = pd.read_csv('vehicles_us.csv')

# Limpieza básica
car_data = car_data.dropna(subset=['price', 'odometer', 'type'])

# -----------------------------
# Filtro interactivo
# -----------------------------
st.sidebar.header('🔍 Filtros')

vehicle_types = sorted(car_data['type'].unique())
selected_type = st.sidebar.selectbox(
    'Selecciona tipo de vehículo', vehicle_types)

filtered_data = car_data[car_data['type'] == selected_type]

# -----------------------------
# Mostrar datos
# -----------------------------
if st.checkbox('Mostrar datos'):
    st.dataframe(filtered_data.head(100))

# -----------------------------
# Métricas (Insights rápidos)
# -----------------------------
st.subheader('📊 Insights rápidos')

col1, col2 = st.columns(2)

with col1:
    st.metric('Precio promedio', f"${int(filtered_data['price'].mean())}")

with col2:
    st.metric('Odómetro promedio',
              f"{int(filtered_data['odometer'].mean())} millas")

# -----------------------------
# Gráficas
# -----------------------------
st.subheader('📈 Visualizaciones')

col1, col2 = st.columns(2)

# Histograma
with col1:
    if st.checkbox('Mostrar histograma'):
        fig_hist = go.Figure(data=[
            go.Histogram(x=filtered_data['odometer'])
        ])
        fig_hist.update_layout(
            title='Distribución del odómetro',
            xaxis_title='Odómetro',
            yaxis_title='Frecuencia'
        )
        st.plotly_chart(fig_hist, use_container_width=True)

# Scatter
with col2:
    if st.checkbox('Mostrar scatter'):
        fig_scatter = go.Figure(data=[
            go.Scatter(
                x=filtered_data['odometer'],
                y=filtered_data['price'],
                mode='markers',
                marker=dict(
                    color=filtered_data['price'],
                    showscale=True
                )
            )
        ])
        fig_scatter.update_layout(
            title='Precio vs Odómetro',
            xaxis_title='Odómetro',
            yaxis_title='Precio'
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

# -----------------------------
# Footer
# -----------------------------
st.write('---')
st.write('Proyecto de análisis de datos con Streamlit 🚀')
