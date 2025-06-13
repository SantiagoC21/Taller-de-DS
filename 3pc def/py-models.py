import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para cargar los datos desde la base de datos SQLite
def cargar_datos(modelo, submodelo):
    conn = sqlite3.connect('BD_OG-TRANSPORTE-MUNICIPAL.db')
    query = f"SELECT * FROM {modelo};"
    data = pd.read_sql(query, conn)
    conn.close()

    # Verificar las columnas disponibles
    print(f"Columnas disponibles en la tabla {modelo}: {data.columns.tolist()}")

    # Verificar si el submodelo existe en las columnas
    if submodelo not in data.columns:
        print(f"Submodelo '{submodelo}' no encontrado en las columnas del modelo {modelo}.")
        return pd.DataFrame()  # Retornar un DataFrame vacío si no se encuentra el submodelo

    # Asignar los años desde 2025 hasta 2036, de forma ordenada
    num_filas = len(data)
    años = list(range(2025, 2036+1))

    if num_filas == len(años):
        data['Año'] = años  # Añadir la columna 'Año' si la cantidad de filas es correcta
    else:
        print(f"Error: El número de filas ({num_filas}) no coincide con el número de años ({len(años)}).")
        return pd.DataFrame()  # Retornar un DataFrame vacío si no coinciden los tamaños

    # Filtrar las columnas necesarias
    data = data[['Año', submodelo]]
    data = data.dropna()  # Eliminar filas con datos nulos
    return data

# Función para actualizar la tabla y la gráfica
def actualizar():
    modelo = modelo_combobox.get()
    submodelo = submodelo_combobox.get()

    datos = cargar_datos(modelo, submodelo)

    # Actualizar la tabla
    for widget in tabla_frame.winfo_children():
        widget.destroy()

    # Crear encabezados de la tabla
    for i, column in enumerate(datos.columns):
        label = tk.Label(tabla_frame, text=column)
        label.pack(side="top", padx=5, pady=5)

    # Rellenar la tabla con datos
    for i, row in enumerate(datos.itertuples()):
        for j, value in enumerate(row[1:]):
            label = tk.Label(tabla_frame, text=value)
            label.pack(side="top", padx=5, pady=5)

    # Mostrar gráfica
    mostrar_grafica(datos, submodelo)

# Función para mostrar la gráfica
def mostrar_grafica(datos, submodelo):
    plt.figure(figsize=(10, 6))

    # Grafica de los datos, con el eje X como los años
    plt.plot(datos['Año'], datos[submodelo], marker='o', linestyle='-', color='b')
    plt.xlabel('Año')
    plt.ylabel(submodelo)
    plt.title(f'Gráfica de {submodelo}')

    # Mostrar la gráfica en la ventana de Tkinter
    canvas = FigureCanvasTkAgg(plt.gcf(), master=ventana)  
    canvas.draw()
    canvas.get_tk_widget().pack(side="top", padx=5, pady=5)  # Colocar la gráfica en la ventana

# Función para terminar el proceso y cerrar la aplicación
def terminar():
    ventana.quit()  # Cerrar la ventana y terminar el proceso

# Crear la interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Visualización de Modelos de Transporte Municipal")

# Modelo y submodelo
modelos = ['Frecuencia_de_mantenimiento', 'Satisfaccion_de_autoridades', 'Satisfaccion_de_usuario', 'Seguridad_vial', 'Eficiencia_de_movilidad']
submodelos = {
    'Frecuencia_de_mantenimiento': ['Disponibilidad_de_la_flot', 'Cantidad_de_fallas_mecanicas', 'Cantidad_de_vehiculos_en_operacion', 'Disponibilidad_de_talleres'],
    'Satisfaccion_de_autoridades': ['Inversion_en_infraestructura', 'Calidad_de_infraestructura_vial', 'Confianza_publica', 'Imagen_publica_de_autoridades'],
    'Satisfaccion_de_usuario': ['Total_de_vehiculos_en_buen_estado', 'Total_de_vehiculos_de_transporte_publico_en_buen_estado', 'Total_de_conductores_con_consumo_de_alcohol', 'Extorsiones_a_transportistas', 'Nivel_de_satisfaccion_de_usuarios', 'Total_de_accidentes_de_transporte'],
    'Seguridad_vial': ['Infraestructura_seguridad_vial', 'Dispositivos_viales_operativos', 'Infraestructura_en_mantenimiento', 'Presupuesto_mantenimiento_de_infraestructura'],
    'Eficiencia_de_movilidad': ['Poblacion_que_utiliza_aplicaciones_de_transporte', 'Total_de_vehiculos_en_circulacion', 'Extorsiones_a_transportistas', 'Total_de_infracciones', 'Eficiencia_de_movilidades']
}

# Selección de modelo
tk.Label(ventana, text="Selecciona un modelo:").pack()
modelo_combobox = ttk.Combobox(ventana, values=modelos)
modelo_combobox.set(modelos[0])
modelo_combobox.pack()

# Selección de submodelo
tk.Label(ventana, text="Selecciona un submodelo:").pack()
submodelo_combobox = ttk.Combobox(ventana, values=submodelos[modelos[0]])
submodelo_combobox.set(submodelos[modelos[0]][0])
submodelo_combobox.pack()

# Actualizar submodelos según el modelo seleccionado
def actualizar_submodelos(event):
    modelo = modelo_combobox.get()
    submodelo_combobox['values'] = submodelos[modelo]
    submodelo_combobox.set(submodelos[modelo][0])

modelo_combobox.bind('<<ComboboxSelected>>', actualizar_submodelos)

# Frame para la tabla de datos
tabla_frame = tk.Frame(ventana)
tabla_frame.pack()

# Botón para cargar datos y gráfica
cargar_button = tk.Button(ventana, text="Cargar datos y mostrar gráfica", command=actualizar)
cargar_button.pack()

# Botón para terminar el proceso y cerrar la aplicación
terminar_button = tk.Button(ventana, text="Terminar", command=terminar)
terminar_button.pack()

# Iniciar la interfaz gráfica
ventana.mainloop()
