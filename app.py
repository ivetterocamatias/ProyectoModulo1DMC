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

# Información en sección Home

if modulo == "Home":

    st.title("☕ Coffee Shop Manager")
    col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("Coffee shop_logo.png", width=600)

    st.subheader("Datos generales de autora")

    st.write("""
    **Estudiante:** Ivette Roca Matias
    
    **Módulo:** Módulo 1 – Python Fundamentals
    
    **Información general de la estudiante:** Ingeniera Pesquera cursando una maestría en Ciencia y Tecnología de Alimentos
    
    **Año:** 2026
    """)

    st.markdown("""
    
    # Descripción del proyecto

    Coffee Shop Manager es una aplicación interactiva desarrollada en Streamlit
    para apoyar la gestión básica de una cafetería. A través de distintos módulos,
    el usuario podrá registrar ingresos y gastos, administrar productos,
    realizar cálculos y gestionar información mediante una interfaz sencilla.
    """)

    st.markdown("""
    ### Tecnologías utilizadas

    - 🐍 Python
    - 🎈 Streamlit
    - 📊 NumPy
    - 🐼 Pandas
    """)

# Información en Ejercicio 1

    elif modulo == "Ejercicio 1":

    st.header("☕ Flujo diario de caja")

    st.markdown("""
    Registre las ventas y los gastos de la cafetería durante la jornada.
    El sistema calculará automáticamente el total de ingresos, el total de
    gastos y el saldo disponible al finalizar el día.
    """)

    # Crear la lista de movimientos la primera vez
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Entrada de datos
    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor (s/.)", min_value=0.0)

    # Botón para registar el movimiento
    if st.button("Registrar movimiento"):

        movimiento = {
            "Concepto": concepto,
            "Tipo": tipo,
            "Valor": valor
        }

        st.session_state.movimientos.append(movimiento)

        st.success("Movimiento registrado correctamente.")

    # Mostrar los movimientos registrados
    st.subheader("Movimientos registrados")

    st.dataframe(st.session_state.movimientos)

    # Cálculos
    total_ingresos = 0
    total_gastos = 0

    for movimiento in st.session_state.movimientos:

        if movimiento["Tipo"] == "Ingreso":
            total_ingresos = movimiento["Valor"]

        else:
            total_gastos = movimiento["Valor"]

    saldo = total_ingresos - total_gastos

    # Métricas

    st.metric("Total ingresos", f"s/ {total_ingresos:.2f}")
    st.metric("Total gastos", f"s/ {total_gastos:.2f}")
    st.metric("Saldo final", f"s/ {saldo:.2f}")

    # Resultado
    if saldo >= 0:
        st.success("El flujo de caja está a favor.")
    else:
        st.error("El flujo de caja está en contra.")



  
valor_inicial = st.number_input("Ingrese el valor inicial", value = 0)
valor_final = st.number_input("Ingrese el valor final", value = 1)

lista_numerica = list(range(valor_inicial,valor_final))

st.write(lista_numerica)
