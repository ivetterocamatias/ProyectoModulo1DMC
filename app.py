import streamlit as st

st.title("Proyecto Módulo 1 Fundamentals")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("Python_logo.png", width=600)

# Menú lateral
modulo = st.sidebar.selectbox(
    "Menú",
    ("Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4")
)
if modulo == "Home":

    st.title("☕ Coffee Shop Manager")
    col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("Coffee shop_logo.png", width=600)

    st.subheader(Datos generales de autora)

    st.write("
    **Estudiante:** Ivette Roca Matias
    
    **Módulo:** Módulo 1 – Python Fundamentals
    
    **Información general de la estudiante:** Ingeniera Pesquera cursando una maestría en Ciencia y Tecnología de Alimentos
    
    **Año:** 2026
    ")

    st.markdown("""
    
    # Descripción del proyecto

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

elif modulo == "Ejercicio 1":

    st.header("Ejercicio 1 - Flujo de caja con listas")

    st.markdown("""
    En este ejercicio se registran movimientos financieros utilizando listas.
    Cada movimiento puede ser un ingreso o un gasto y posteriormente se calcula
    el saldo final.
    """)

    # Crear la lista una sola vez
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Entrada de datos
    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0)

    # Botón
    if st.button("Agregar movimiento"):

        movimiento = {
            "Concepto": concepto,
            "Tipo": tipo,
            "Valor": valor
        }

        st.session_state.movimientos.append(movimiento)

        st.success("Movimiento agregado correctamente.")

    # Mostrar tabla
    st.subheader("Movimientos registrados")

    st.dataframe(st.session_state.movimientos)

    # Cálculos
    total_ingresos = 0
    total_gastos = 0

    for movimiento in st.session_state.movimientos:

        if movimiento["Tipo"] == "Ingreso":
            total_ingresos += movimiento["Valor"]

        else:
            total_gastos += movimiento["Valor"]

    saldo = total_ingresos - total_gastos

    # Métricas
    st.metric("Total ingresos", total_ingresos)
    st.metric("Total gastos", total_gastos)
    st.metric("Saldo final", saldo)

    # Resultado
    if saldo >= 0:
        st.success("El flujo de caja está a favor.")
    else:
        st.error("El flujo de caja está en contra.")



  
valor_inicial = st.number_input("Ingrese el valor inicial", value = 0)
valor_final = st.number_input("Ingrese el valor final", value = 1)

lista_numerica = list(range(valor_inicial,valor_final))

st.write(lista_numerica)
