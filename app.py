import streamlit as st

st.title("Proyecto Módulo 1 Fundamentals")
st.sidebar.title("Parámetros")

st.image("Python_logo.png")
st.sidebar.image("DMC.png")

modulo = st.sidebar.selectbox(
    "Menú",
    ("Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4")
)
if modulo == "Home":

    st.title("🐍 Python Fundamentals – Streamlit Project")

    st.subheader("Proyecto Aplicado en Streamlit")

    st.write("""
    **Estudiante:** Ivette Roca Matias
    **Módulo:** Módulo 1 – Python Fundamentals
    **Información general del estudiante:** Ingeniera Pesquera, cursando una maestría en Ciencia y Tecnología de Alimentos
    **Año:** 2026
    """)

    st.markdown("""
    ### Descripción del proyecto

    Esta aplicación fue desarrollada como parte del Proyecto 1 del módulo
    **Python Fundamentals**. Su objetivo es integrar los conceptos
    fundamentales de programación en Python mediante una interfaz interactiva
    creada con Streamlit.

    En la aplicación se presentan cuatro ejercicios que abarcan el uso de
    listas, estructuras de datos, NumPy, funciones, programación orientada a
    objetos (POO) y operaciones CRUD.
    """)

    st.markdown("""
    ### Tecnologías utilizadas

    - 🐍 Python
    - 🎈 Streamlit
    - 📊 NumPy
    - 🐼 Pandas
    """)

    st.image("Python_logo.png", width=200)



  
valor_inicial = st.number_input("Ingrese el valor inicial", value = 0)
valor_final = st.number_input("Ingrese el valor final", value = 1)

lista_numerica = list(range(valor_inicial,valor_final))

st.write(lista_numerica)
