import pysd
import matplotlib.pyplot as plt
model = pysd.read_vensim('frecuencia de mantenimiento.mdl')
results = model.run()
disponibilidad_de_la_flota = results["Disponibilidad de la flota"]
objetivo_disponibilidad_de_la_flota = 30
discrepancia_disponibilidad_de_la_flota = 30 - disponibilidad_de_la_flota

# Crear la figura
plt.figure(figsize=(10, 6))

# Graficar la Disponibilidad de la Flota
plt.plot(disponibilidad_de_la_flota, label='Disponibilidad de la Flota', color='blue')

# Graficar la Discrepancia de la Flota
plt.plot(discrepancia_disponibilidad_de_la_flota, label='Discrepancia de la Flota', color='green')

# Graficar el objetivo (constante)
plt.axhline(y=objetivo_disponibilidad_de_la_flota, color='red', linestyle='--', label='Objetivo (30)')

# Añadir título y etiquetas
plt.title('Disponibilidad y Discrepancia de la Flota')
plt.xlabel('Semanas')
plt.ylabel('Valor')

# Activar la cuadrícula
plt.grid(True)

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
