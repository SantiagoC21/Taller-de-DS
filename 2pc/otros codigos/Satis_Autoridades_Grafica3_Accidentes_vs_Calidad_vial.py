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

    # Gráfica 3: Accidentes vs Calidad de infraestructura vial (Como es realmente)
    years = list(range(2015, 2027))
    accidentes = [600, 610, 650, 700, 730, 770, 800, 850, 890, 930, 960, 1000]
    calidad = [85, 82, 80, 78, 75, 73, 70, 67, 63, 60, 58, 55]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    ax1.set_xlabel('Año')

    # Eje y1 (Accidentes)
    color_acc = 'tab:blue'
    ax1.set_ylabel('Accidentes', color=color_acc)
    ax1.plot(years, accidentes, color=color_acc, marker='o', label='Accidentes')
    ax1.tick_params(axis='y', labelcolor=color_acc)
    ax1.set_ylim([500, 1050])  # Ajusta para visualizar el rango

    # Eje y2 (Calidad vial)
    ax2 = ax1.twinx()
    color_cal = 'tab:red'
    ax2.set_ylabel('Calidad vial', color=color_cal)
    ax2.plot(years, calidad, color=color_cal, marker='s', label='Calidad vial')
    ax2.tick_params(axis='y', labelcolor=color_cal)
    ax2.set_ylim([50, 90])  # Ajusta para ver la caída

    # Título y ajuste
    plt.title('Accidentes de tránsito vs Calidad de infraestructura vial (Escenario Inestable)')
    fig.tight_layout()
    plt.savefig('accidentes_vs_calidad_inestable.png', dpi=150)
    plt.show()

    # Gráfica 3: Accidentes vs Calidad de infraestructura vial (Como debería ser)
    fig3, ax1 = plt.subplots(figsize=(6, 6))
    ax1.plot(df["Time"], df["Accidentes de tránsito"], label="Accidentes de tránsito", color="blue")
    ax2 = ax1.twinx()
    ax2.plot(df["Time"], df["Calidad de infraestructura vial"], label="Calidad vial", color="red")
    ax1.set_ylabel("Accidentes", color="blue")
    ax2.set_ylabel("Calidad vial", color="red")
    ax1.set_xlabel("Año")
    ax1.set_title("Accidentes de tránsito vs Calidad de infraestructura vial")
    ax1.grid(True)
    plt.tight_layout()
    plt.savefig("grafica3_accidentes_vs_calidad.png")

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
    texto_tablas.insert(tk.END, f"{'Año':<10}{'Accidentes':<20}{'Calidad vial':<20}\n")
    texto_tablas.insert(tk.END, "-"*50 + "\n")

    # Crear la tabla real
    data_real = {
        "Año": list(range(2015, 2027)),
        "Accidentes": [600, 610, 650, 700, 730, 770, 800, 850, 890, 930, 960, 1000],
        "Calidad vial": [85, 82, 80, 78, 75, 73, 70, 67, 63, 60, 58, 55]
    }
    df_real = pd.DataFrame(data_real)
    df_real_sorted = df_real.sort_values(by=["Accidentes"], ascending=False)
    
    for index, row in df_real_sorted.iterrows():
        texto_tablas.insert(tk.END, f"{row['Año']:<10}{row['Accidentes']:<20}{row['Calidad vial']:<20}\n")

    texto_tablas.insert(tk.END, "\nTabla Mejorada:\n")
    texto_tablas.insert(tk.END, f"{'Año':<10}{'Accidentes':<20}{'Calidad vial':<20}\n")
    texto_tablas.insert(tk.END, "-"*50 + "\n")

    # Crear la tabla mejorada
    for index, row in df.iterrows():
        texto_tablas.insert(tk.END, f"{row['Time']:<10}{row['Accidentes de tránsito']:<20}{row['Calidad de infraestructura vial']:<20}\n")
    
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
