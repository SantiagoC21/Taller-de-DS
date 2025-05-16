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

    # Gráfica adicional: Satisfacción de usuarios vs Calidad de infraestructura vial (Como es realmente)
    years = list(range(2015, 2027))
    satisfaccion = [3.50, 3.45, 3.40, 3.30, 3.20, 3.10, 2.90, 2.70, 2.50, 2.40, 2.20, 2.00]
    calidad_vial = [80, 78, 76, 74, 72, 70, 67, 65, 62, 60, 58, 55]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    ax1.set_xlabel('Año')

    # Eje Y1 -> Satisfacción de usuarios
    color_sat = 'tab:blue'
    ax1.set_ylabel('Satisfacción de usuarios', color=color_sat)
    ax1.plot(years, satisfaccion, color=color_sat, marker='o', label='Satisfacción')
    ax1.tick_params(axis='y', labelcolor=color_sat)
    ax1.set_ylim([1.5, 4.0])  # Ajusta para ver mejor la tendencia descendente

    # Eje Y2 -> Calidad de infraestructura
    ax2 = ax1.twinx()
    color_cal = 'tab:red'
    ax2.set_ylabel('Calidad de infraestructura vial', color=color_cal)
    ax2.plot(years, calidad_vial, color=color_cal, marker='s', label='Calidad vial')
    ax2.tick_params(axis='y', labelcolor=color_cal)
    ax2.set_ylim([50, 85])  # Ajusta para ver la caída desde ~80

    # Título y guardado
    plt.title('Satisfacción de usuarios vs Calidad de infraestructura vial (Escenario Inestable)')
    fig.tight_layout()
    plt.savefig('satisfaccion_vs_calidad_inestable.png', dpi=150)
    plt.show()

    # Gráfica adicional: Satisfacción de usuarios vs Calidad de infraestructura vial (Como debería ser)
    fig4, ax1 = plt.subplots(figsize=(6, 6))
    ax1.plot(df["Time"], df["Satisfaccion de usuarios"], label="Satisfacción de usuarios", color="blue")
    ax2 = ax1.twinx()
    ax2.plot(df["Time"], df["Calidad de infraestructura vial"], label="Calidad vial", color="red")
    ax1.set_ylabel("Satisfacción de usuarios", color="blue")
    ax2.set_ylabel("Calidad de infraestructura vial", color="red")
    ax1.set_xlabel("Año")
    ax1.set_title("Satisfacción de usuarios vs Calidad de infraestructura vial")
    ax1.grid(True)
    plt.tight_layout()
    plt.savefig("grafica4_satisfaccion_vs_calidad.png")

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
    texto_tablas.insert(tk.END, f"{'Año':<10}{'Satisfacción de usuarios':<25}{'Calidad de infraestructura vial':<30}\n")
    texto_tablas.insert(tk.END, "-"*70 + "\n")

    # Crear la tabla real
    data_real = {
        "Año": list(range(2015, 2027)),
        "Satisfacción de usuarios": [3.50, 3.45, 3.40, 3.30, 3.20, 3.10, 2.90, 2.70, 2.50, 2.40, 2.20, 2.00],
        "Calidad de infraestructura vial": [80, 78, 76, 74, 72, 70, 67, 65, 62, 60, 58, 55]
    }
    df_real = pd.DataFrame(data_real)
    df_real_sorted = df_real.sort_values(by=["Satisfacción de usuarios"], ascending=False)
    
    for index, row in df_real_sorted.iterrows():
        texto_tablas.insert(tk.END, f"{row['Año']:<10}{row['Satisfacción de usuarios']:<25}{row['Calidad de infraestructura vial']:<30}\n")

    texto_tablas.insert(tk.END, "\nTabla Mejorada:\n")
    texto_tablas.insert(tk.END, f"{'Año':<10}{'Satisfacción de usuarios':<25}{'Calidad de infraestructura vial':<30}\n")
    texto_tablas.insert(tk.END, "-"*70 + "\n")

    # Crear la tabla mejorada
    for index, row in df.iterrows():
        texto_tablas.insert(tk.END, f"{row['Time']:<10}{row['Satisfaccion de usuarios']:<25}{row['Calidad de infraestructura vial']:<30}\n")
    
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
