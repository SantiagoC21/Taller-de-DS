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

    # Gráfica 2: Imagen pública vs Inversión en infraestructura (Como es realmente)
    years = list(range(2015, 2027))
    imagen = [0.50, 0.48, 0.47, 0.45, 0.46, 0.44, 0.42, 0.41, 0.40, 0.39, 0.37, 0.35]
    inversion = [10000, 9990, 9985, 9978, 9980, 9972, 9965, 9958, 9950, 9944, 9936, 9930]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    ax1.set_xlabel('Año')

    # Eje y1 (Imagen pública)
    color_imagen = 'tab:blue'
    ax1.set_ylabel('Imagen pública', color=color_imagen)
    ax1.plot(years, imagen, color=color_imagen, marker='o', label='Imagen pública')
    ax1.tick_params(axis='y', labelcolor=color_imagen)
    ax1.set_ylim([0.30, 0.55])  # Ajusta para resaltar la bajada

    # Eje y2 (Inversión en miles USD)
    ax2 = ax1.twinx()
    color_inversion = 'tab:red'
    ax2.set_ylabel('Inversión (miles)', color=color_inversion)
    ax2.plot(years, inversion, color=color_inversion, marker='s', label='Inversión')
    ax2.tick_params(axis='y', labelcolor=color_inversion)
    ax2.set_ylim([9920, 10010])  # Ajusta para mostrar variaciones

    # Título y leyenda
    plt.title('Imagen pública vs Inversión en infraestructura (Escenario Inestable)')
    fig.tight_layout()
    plt.savefig('imagen_vs_inversion_inestable.png', dpi=150)
    plt.show()

    # Gráfica 2: Imagen pública vs Inversión en infraestructura (Como debería ser)
    fig2, ax1 = plt.subplots(figsize=(6, 6))
    ax1.plot(df["Time"], df["Imagen pública de autoridades"], label="Imagen pública", color="blue")
    ax2 = ax1.twinx()
    ax2.plot(df["Time"], df["Inversion en infraestructura"], label="Inversión en infraestructura", color="red")
    ax1.set_ylabel("Imagen pública", color="blue")
    ax2.set_ylabel("Inversión (miles)", color="red")
    ax1.set_xlabel("Año")
    ax1.set_title("Imagen pública vs Inversión en infraestructura")
    ax1.grid(True)
    plt.tight_layout()
    plt.savefig("grafica2_imagen_vs_inversion.png")

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
    texto_tablas.insert(tk.END, f"{'Año':<10}{'Imagen pública':<20}{'Inversión (miles)':<20}\n")
    texto_tablas.insert(tk.END, "-"*50 + "\n")

    # Crear la tabla real
    data_real = {
        "Año": list(range(2015, 2027)),
        "Imagen pública": [0.50, 0.48, 0.47, 0.45, 0.46, 0.44, 0.42, 0.41, 0.40, 0.39, 0.37, 0.35],
        "Inversión (miles)": [10000, 9990, 9985, 9978, 9980, 9972, 9965, 9958, 9950, 9944, 9936, 9930]
    }
    df_real = pd.DataFrame(data_real)
    df_real_sorted = df_real.sort_values(by=["Imagen pública"], ascending=False)
    
    for index, row in df_real_sorted.iterrows():
        texto_tablas.insert(tk.END, f"{row['Año']:<10}{row['Imagen pública']:<20}{row['Inversión (miles)']:<20}\n")

    texto_tablas.insert(tk.END, "\nTabla Mejorada:\n")
    texto_tablas.insert(tk.END, f"{'Año':<10}{'Imagen pública':<20}{'Inversión (miles)':<20}\n")
    texto_tablas.insert(tk.END, "-"*50 + "\n")

    # Crear la tabla mejorada
    for index, row in df.iterrows():
        texto_tablas.insert(tk.END, f"{row['Time']:<10}{row['Imagen pública de autoridades']:<20}{row['Inversion en infraestructura']:<20}\n")
    
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
