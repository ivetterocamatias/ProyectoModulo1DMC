import streamlit as st
import numpy as np
import pandas as pd

st.title("Proyecto Módulo 1 Fundamentals")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("Coffee shop_logo.png", width=600)

# Menú lateral

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.sidebar.image("Python_logo.png", width=600)
    
modulo = st.sidebar.selectbox(
    "Menú",
    ("Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4")
)

# Información en sección Home

if modulo == "Home":

    st.title("☕ Coffee Shop Manager")
    
    st.subheader("Datos generales de autora")

    st.write("""
    **Estudiante:** Ivette Roca Matias
    
    **Módulo:** Módulo 1 – Python Fundamentals
    
    **Información general de la estudiante:** Ingeniera pesquera cursando una maestría en Ciencia y Tecnología de Alimentos
    
    **Año:** 2026
    """)

    st.markdown("""
    
    ### Descripción del proyecto

    Coffee Shop Manager es una aplicación interactiva desarrollada en Streamlit
    para apoyar la gestión básica de una cafetería. A través de las distintas secciones,
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

# Ejercicio 1

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
    valor = st.number_input("Valor (s/)", min_value=0.0)

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
            total_ingresos += movimiento["Valor"]

        else:
            total_gastos += movimiento["Valor"]

    saldo = total_ingresos - total_gastos

    # Eliminar movimiento

    if st.button("Eliminar último movimiento"):
        if len(st.session_state.movimientos) > 0:
            st.session_state.movimientos.pop()
            st.success("Último movimiento eliminado.")
            
    # Métricas
    
    st.subheader("Resumen")

    st.metric("Total ingresos", f"s/ {total_ingresos:.2f}")
    st.metric("Total gastos", f"s/ {total_gastos:.2f}")
    st.metric("Saldo final", f"s/ {saldo:.2f}")

    # Resultado
    
    if saldo >= 0:
        st.success("El flujo de caja está a favor.")
    else:
        st.error("El flujo de caja está en contra.")


# Ejercicio 2

elif modulo == "Ejercicio 2":

    st.header("☕ Registro de inventario")

    st.markdown("""
    Registre los productos disponibles en la cafetería.
    Para cada producto se ingresará el nombre, la categoría y el precio de venta.
    Posteriormente, el sistema mostrará la lista de productos registrados.
    """) 

    # Crear arrays vacíos de NumPy para almacenar datos
    
    if "nombres" not in st.session_state:
        st.session_state.nombres = np.array([])

    if "categorias" not in st.session_state:
        st.session_state.categorias = np.array([])

    if "precios" not in st.session_state:
        st.session_state.precios = np.array([])

    if "cantidades" not in st.session_state:
        st.session_state.cantidades = np.array([])

    if "totales" not in st.session_state:
        st.session_state.totales = np.array([])

    # Crear formulario para ingresar productos
    
    st.subheader("Ingresar nuevo producto")

    nombre = st.text_input("Nombre del producto")
    
    categoria = st.selectbox(
        "Categoría",
        ["Café", "Postre", "Bebida fría", "Snack"]
    )
    
    precio = st.number_input(
        "Precio",
        min_value=0.0,
        step=0.5
    )
    
    cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        step=1
    )

    # Botón para registrar producto
    
    if st.button("Registrar producto"):
    
        # Calcular total automáticamente
        total = precio * cantidad
    
    
        # Agregar cada dato al array correspondiente
        nombres = np.append(nombres, nombre)
        categorias = np.append(categorias, categoria)
        precios = np.append(precios, precio)
        cantidades = np.append(cantidades, cantidad)
        totales = np.append(totales, total)
    
    
        st.success("Producto registrado correctamente")

    # Crear DataFrame usando los arrays de NumPy

    df = pd.DataFrame(
        {
            "Producto": nombres,
            "Categoría": categorias,
            "Precio": precios,
            "Cantidad": cantidades,
            "Total": totales
        }
    )

    # Mostrar tabla final

    st.subheader("Registro de productos")
    st.dataframe(df)

# Ejercicio 3

elif modulo == "Ejercicio 3":
    
    # Importar la función desde la librería funciones
    
    from libreria_funciones_proyecto1 import calcular_dpmo
    
    # Aplicación al área de calidad 
    
    st.title("Evaluación de calidad de proceso productivo")
    
    # Creación de histórico
    
    if "historial" not in st.session_state:
    
        st.session_state.historial = pd.DataFrame(
            columns=[
                "Defectos",
                "Unidades producidas",
                "Oportunidades por unidad",
                "DPMO",
                "Rendimiento (%)"
            ]
        )
    
    # Selección de función
    
    st.header("Parámetro a evaluar")
    
    
    funcion = st.selectbox(
        "Seleccione una función",
        [
            "Calcular DPMO"
        ]
    )
    
    # Widgets para ingresar parámetros
    
    st.header("Ingresar datos del proceso")
    
    
    defectos = st.number_input(
        "Número de defectos encontrados",
        min_value=0,
        step=1
    )
    
    
    unidades = st.number_input(
        "Número de unidades producidas",
        min_value=1,
        step=1
    )
    
    
    oportunidades = st.number_input(
        "Oportunidades de defecto por unidad",
        min_value=1,
        step=1
    )
    
    # Ejecutar función
    
    if st.button("Evaluar calidad"):
    
        try:
    
            resultado = calcular_dpmo(
                defectos,
                unidades,
                oportunidades
            )
    
            # Mostrar resultado
    
            st.success("Cálculo realizado correctamente")
    
    
            st.write(
                "DPMO:",
                resultado["dpmo"]
            )
    
            st.write(
                "Rendimiento del proceso:",
                resultado["rendimiento_pct"],
                "%"
            )
    
            # Guardar histórico
    
            nuevo = pd.DataFrame(
                {
                    "Defectos": [defectos],
                    "Unidades producidas": [unidades],
                    "Oportunidades por unidad": [oportunidades],
                    "DPMO": [resultado["dpmo"]],
                    "Rendimiento (%)": [round(resultado["rendimiento_pct"],2)]
                }
            )
    
            st.session_state.historial = pd.concat(
                [
                    st.session_state.historial,
                    nuevo
                ],
                ignore_index=True
            )
    
        except ValueError as error:
    
            st.error(error)
    
    # Mostrar histórico
    
    st.header("Histórico de evaluaciones")
    st.dataframe(st.session_state.historial)


# Ejercicio 4

elif modulo == "Ejercicio 4":

    import pandas as pd
    from libreria_clases_proyecto1 import calcular_ticket_promedio


    st.header("☕ Gestión de ventas - CRUD")

    st.markdown("""
    Registre las ventas de la cafetería para 
    calcular el ticket promedio y administrar los registros.
    """)

# Uso de clase

    class Venta:

        def __init__(self, producto, ventas_totales, clientes):
            
            self.producto = producto
            self.ventas_totales = ventas_totales
            self.clientes = clientes


        def calcular(self):

            resultado = calcular_ticket_promedio(
                self.ventas_totales,
                self.clientes
            )

            return resultado["ticket_promedio"]

# Creación de almacenamiento

    if "ventas" not in st.session_state:

        st.session_state.ventas = []

    st.subheader("Crear registro")


    producto = st.text_input(
        "Producto vendido"
    )

# Formulario

    ventas_totales = st.number_input(
        "Ventas totales ($)",
        min_value=0.0,
        step=1.0
    )

# Actualizar

    st.subheader("Registros actuales")


    if len(st.session_state.ventas) > 0:

        df = pd.DataFrame(
            st.session_state.ventas
        )


        st.dataframe(df)


    else:

        st.info(
            "No existen registros todavía"
        )

    clientes = st.number_input(
        "Número de clientes",
        min_value=1,
        step=1
    )


    if st.button("Agregar venta"):


        nueva_venta = Venta(
            producto,
            ventas_totales,
            clientes
        )


        ticket = nueva_venta.calcular()


        registro = {

            "Producto": producto,
            "Ventas totales": ventas_totales,
            "Clientes": clientes,
            "Ticket promedio": ticket

        }


        st.session_state.ventas.append(registro)


        st.success(
            "Venta registrada correctamente"
        )

# Eliminar

    st.subheader("Eliminar registro")


    if len(st.session_state.ventas) > 0:


        eliminar = st.number_input(

            "Número de registro a eliminar",
            min_value=0,
            max_value=len(st.session_state.ventas)-1,
            step=1

        )


        if st.button("Eliminar"):


            st.session_state.ventas.pop(
                eliminar
            )


            st.success(
                "Registro eliminado"
            )
