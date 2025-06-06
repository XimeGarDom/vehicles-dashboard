import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de vehículos en venta - Dashboard')

# Casilla de verificación para histograma
build_histogram = st.checkbox('Mostrar histograma del odómetro')

if build_histogram:
    st.write('Histograma del kilometraje (odómetro)')

    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.hist(car_data['odometer'].dropna(), bins=30, color='skyblue', edgecolor='black')
    ax1.set_title('Histograma del Odómetro')
    ax1.set_xlabel('Kilometraje')
    ax1.set_ylabel('Frecuencia')
    ax1.grid(True)

    st.pyplot(fig1)

# Casilla de verificación para gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión (odómetro vs precio)')

if build_scatter:
    st.write('Gráfico de dispersión: Kilometraje vs Precio')

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.scatter(car_data['odometer'], car_data['price'], alpha=0.3, color='green')
    ax2.set_title('Kilometraje vs Precio')
    ax2.set_xlabel('Odómetro')
    ax2.set_ylabel('Precio')
    ax2.grid(True)

    st.pyplot(fig2)
