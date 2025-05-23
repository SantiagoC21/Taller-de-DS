import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pysd
import sys

modelo_path = 'FORRESTER-Satisfaccion_autoridades.mdl'


def get_num_filas():
    try:
        n = int(entrada_filas.get())
        if 1 <= n <= 100:
            return n
        else:
            raise ValueError
    except:
        messagebox.showwarning("Valor inválido", "Por favor ingresa un número entre 1 y 100.")
        return 6 


def mostrar_resultado(nombre_variable, titulo, num_filas):
    try:
        modelo = pysd.read_vensim(modelo_path)
        valores = modelo.run(return_columns=[nombre_variable])
        tabla_datos = valores.head(num_filas)

     
        ventana_res = tk.Toplevel()
        ventana_res.title(titulo)
        ventana_res.geometry("900x500")

     
        frame_grafico = tk.Frame(ventana_res)
        frame_grafico.pack(side='left', fill='both', expand=True)

    
        fig, ax = plt.subplots(figsize=(5, 4))
        tabla_datos.plot(ax=ax)
        ax.set_title(f"{titulo} (primeros {num_filas} puntos)")
        ax.set_xlabel("Años")
        ax.set_ylabel("Cantidad")

        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

        
        frame_tabla = tk.Frame(ventana_res)
        frame_tabla.pack(side='right', fill='y')

        tk.Label(frame_tabla, text="Primeros Valores", font=('Helvetica', 12, 'bold')).pack(pady=5)

        tree = ttk.Treeview(frame_tabla)
        tree.pack(expand=True, fill='y')

        tree['columns'] = ('Tiempo', 'Valor')
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Tiempo", anchor=tk.CENTER, width=100)
        tree.column("Valor", anchor=tk.CENTER, width=120)

        tree.heading("Tiempo", text="Tiempo", anchor=tk.CENTER)
        tree.heading("Valor", text=nombre_variable, anchor=tk.CENTER)

        for index, row in tabla_datos.iterrows():
            tree.insert("", "end", values=(round(index, 2), round(row[0], 2)))

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el modelo o variable:\n{e}")


def accidentes_transito():
    mostrar_resultado('Accidentes de tránsito', 'Accidentes de Tránsito', get_num_filas())

def cantidad_accidentes():
    mostrar_resultado('Cantidad de accidentes', 'Cantidad de Accidentes', get_num_filas())

def accidentes_prevenidos():
    mostrar_resultado('Accidentes prevenidos', 'Accidentes Prevenidos', get_num_filas())

def discrepancia():
    mostrar_resultado('Discrepacia', 'Discrepancia', get_num_filas())

def congestion_vehicular():
    mostrar_resultado('Porcentaje de congestion vehicular', 'Congestión Vehicular', get_num_filas())

def fluidez_trafico():
    mostrar_resultado('Tasa de fluidez del trafico', 'Fluidez del Tráfico', get_num_filas())

def regulaciones_viales():
    mostrar_resultado('Total regulaciones viales', 'Regulaciones Viales', get_num_filas())

def salir():
    ventana.destroy()
    sys.exit()


ventana = tk.Tk()
ventana.title("Módulo: Satisfacción de Autoridades (PySD)")
ventana.geometry("400x500")

tk.Label(ventana, text="Menú Principal", font=('Helvetica', 14, 'bold')).pack(pady=10)

tk.Label(ventana, text="Filas a mostrar en tabla y gráfico (1-100):").pack(pady=(10, 0))
entrada_filas = tk.Entry(ventana, justify='center')
entrada_filas.insert(0, "11") 
entrada_filas.pack()

botones = [
    ("Accidentes de Tránsito", accidentes_transito),
    ("Cantidad de Accidentes", cantidad_accidentes),
    ("Accidentes Prevenidos", accidentes_prevenidos),
    ("Discrepancia", discrepancia),
    ("Congestión Vehicular", congestion_vehicular),
    ("Fluidez del Tráfico", fluidez_trafico),
    ("Regulaciones Viales", regulaciones_viales),
    ("Salir", salir)
]

for texto, comando in botones:
    tk.Button(ventana, text=texto, command=comando, width=35, height=2).pack(pady=5)


ventana.mainloop()
