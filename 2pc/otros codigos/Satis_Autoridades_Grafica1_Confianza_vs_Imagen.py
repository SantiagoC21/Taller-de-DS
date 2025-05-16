import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Leer los datos del archivo Excel
file_path = "/storage/emulated/0/Taller/Sistema de satisfacion de autoridades - Datos.xlsx"
df = pd.read_excel(file_path, sheet_name="Hoja1")

# Función para mostrar las gráficas
def mostrar_graficas():
    # Limpiar la ventana actual
    for widget in ventana.winfo_children():
        widget.destroy()

    # Crear un frame para las gráficas
    frame_graficas = tk.Frame(ventana)
    frame_graficas.pack(pady=20)

    # Gráfica 1: Confianza pública vs Imagen pública (Como es realmente)
    years = list(range(2015, 2027))
    confianza = [0.50, 0.48, 0.47, 0.46, 0.42, 0.43, 0.40, 0.39, 0.38, 0.36, 0.35, 0.33]
    imagen = [1.00, 0.95, 0.88, 0.90, 0.85, 0.82, 0.78, 0.80, 0.75, 0.72, 0.69, 0.65]

    fig1, ax1 = plt.subplots(figsize=(6, 6))
    ax1.plot(years, confianza, label="Confianza pública", color="blue")
    ax2 = ax1.twinx()
    ax2.plot(years, imagen, label="Imagen pública", color="red")
    ax1.set_xlabel("Año")
    ax1.set_ylabel("Confianza pública", color="blue")
    ax2.set_ylabel("Imagen pública", color="red")
    ax1.set_title("Confianza pública vs Imagen pública (Escenario Inestable)")

    # Mostrar la gráfica 1
    canvas1 = FigureCanvasTkAgg(fig1, master=frame_graficas)  
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Gráfica 2: Confianza pública vs Imagen pública (Como debería ser)
    fig2, ax1 = plt.subplots(figsize=(6, 6))
    ax1.plot(df["Time"], df["Confianza pública"], label="Confianza pública", color="blue")
    ax2 = ax1.twinx()
    ax2.plot(df["Time"], df["Imagen pública de autoridades"], label="Imagen pública", color="red")
    ax1.set_ylabel("Confianza pública", color="blue")
    ax2.set_ylabel("Imagen pública", color="red")
    ax1.set_xlabel("Año")
    ax1.set_title("Confianza pública vs Imagen pública (Mejorado)")

    # Mostrar la gráfica 2
    canvas2 = FigureCanvasTkAgg(fig2, master=frame_graficas)  
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Botón para regresar a las tablas
    boton_tablas = tk.Button(ventana, text="Ver Tablas Ordenadas", command=mostrar_tablas)
    boton_tablas.pack(pady=20)

# Función para mostrar las tablas ordenadas
def mostrar_tablas():
    # Limpiar la ventana actual
    for widget in ventana.winfo_children():
        widget.destroy()

    # Crear un frame para mostrar las tablas
    frame_tablas = tk.Frame(ventana)
    frame_tablas.pack(pady=20)

    # Crear un Text widget con barra de desplazamiento para las tablas
    texto_tablas = tk.Text(frame_tablas, wrap=tk.WORD, height=20, width=80)
    texto_tablas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_tablas, command=texto_tablas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    texto_tablas.config(yscrollcommand=scrollbar.set)

    # Formato de texto para las tablas
    texto_tablas.insert(tk.END, "Tabla Real:\n")
    texto_tablas.insert(tk.END, f"{'Año':<10}{'Confianza pública':<20}{'Imagen pública':<20}\n")
    texto_tablas.insert(tk.END, "-"*50 + "\n")

    # Crear la tabla real
    data_real = {
        "Año": list(range(2015, 2027)),
        "Confianza pública": [0.50, 0.48, 0.47, 0.46, 0.42, 0.43, 0.40, 0.39, 0.38, 0.36, 0.35, 0.33],
        "Imagen pública": [1.00, 0.95, 0.88, 0.90, 0.85, 0.82, 0.78, 0.80, 0.75, 0.72, 0.69, 0.65]
    }
    df_real = pd.DataFrame(data_real)
    df_real_sorted = df_real.sort_values(by=["Confianza pública"], ascending=False)
    
    for index, row in df_real_sorted.iterrows():
        texto_tablas.insert(tk.END, f"{row['Año']:<10}{row['Confianza pública']:<20}{row['Imagen pública']:<20}\n")

    texto_tablas.insert(tk.END, "\nTabla Mejorada:\n")
    texto_tablas.insert(tk.END, f"{'Año':<10}{'Confianza pública':<20}{'Imagen pública':<20}\n")
    texto_tablas.insert(tk.END, "-"*50 + "\n")

    # Crear la tabla mejorada
    for index, row in df.iterrows():
        texto_tablas.insert(tk.END, f"{row['Time']:<10}{row['Confianza pública']:<20}{row['Imagen pública de autoridades']:<20}\n")
    
    # Botón para regresar a las gráficas
    boton_graficas = tk.Button(ventana, text="Ver Gráficas", command=mostrar_graficas)
    boton_graficas.pack(pady=20)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Análisis de Sistema de Satisfacción")

# Crear botón para mostrar las gráficas
boton_graficas = tk.Button(ventana, text="Mostrar Gráficas", command=mostrar_graficas)
boton_graficas.pack(pady=20)

# Iniciar la interfaz gráfica
ventana.mainloop()
