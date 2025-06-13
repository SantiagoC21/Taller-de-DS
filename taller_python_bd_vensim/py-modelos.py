import sqlite3                   
import pysd                        
import matplotlib.pyplot as plt     
import pandas as pd  

connection = sqlite3.connect("BD_INFRAESTRUCTURA_NUEVA.db")
cur = connection.cursor()

print("* Conectando a la Base de Datos: DB_Infraestructura","\n")
print("\t\t\tSUBSISTEMA DE INFRAESTRUCTURA","\n")
    
tabla1 = "SELECT * FROM Veredas"
tabla2 = "SELECT * FROM Pistas"
tabla3 = "SELECT * FROM LosasDeportivas"
tabla4 = "SELECT * FROM Puentes"
tabla5 = "SELECT * FROM AlumbradoPublico"

submodelo1 = "Veredas"
submodelo2 = "Pistas"
submodelo3 = "Losas"
submodelo4 = "Puentes"
submodelo5 = "Alumbrado publico"
    
print("Número de Submodelos:",5,"\n")

print(" - Submodelo 1:",submodelo1)
print(" - Submodelo 2:",submodelo2)
print(" - Submodelo 3:",submodelo3)
print(" - Submodelo 4:",submodelo4)
print(" - Submodelo 5:",submodelo5)
print("\n")

def Mostrar_Registros():
    i = 1
    for num in range(1, 6):
        print("-" * 30)
        if i == 1:
            print("SUBMODELO", i, ":", submodelo1)  # Veredas
            print("\t-------")
            for row in cur.execute(tabla1):
                print("\t*****")
                print("\tAño:", row[0])
                print("\tVeredas Construidas:", row[1])
                print("\tVeredas en construccion:", row[2])
                print("\tVeredas obsoletas:", row[3])
                print("\tMantenimiento Veredas:", row[4])
                print("\tGastos Totales Veredas:", row[5])
                print("\tTasa Veredas Construccion:", row[6])
                print("\tDemanda de veredas:", row[7])
                print("\tUso de veredas:", row[8])
                print("\tTasa Veredas Obsoletas:", row[9])
                #print("\tFactor de desgaste natural:", row[10], "\n")

        elif i == 2:
            print("SUBMODELO", i, ":", submodelo2)  # Pistas
            print("\t-------")
            for row in cur.execute(tabla2):
                print("\t*****")
                print("\tAño:", row[0])
                print("\tPistas Construidas:", row[1])
                print("\tPistas en construccion:", row[2])
                print("\tPistas obsoletas:", row[3])
                print("\tPistas en mantenimiento:", row[4])
                print("\tPistas reparadas:", row[5])
                print("\tPistas retiradas para mantenimiento:", row[6])
                print("\tFondos para mantenimiento:", row[7])
                print("\tFondos asignados para mantenimiento:", row[8])
                print("\tGastos en mantenimiento:", row[9])
                print("\tMonto Total Pistas:", row[10])
                print("\tCantidad de litros de pintura:", row[11])
                print("\tPistas asfaltadas:", row[12])
                print("\tCantidad de mano de obra persona:", row[13])
                print("\tCantidad de maquinarias total:", row[14])
                print("\tCantidad de maquinas asfaltos:", row[15])
                print("\tTasa Pistas Construccion:", row[16])
                print("\tTasa Pistas Obsoletas:", row[17])
                print("\tTasa de retiro de pistas para mantenimiento:", row[18])
                print("\tTasa de reparacion de pistas:", row[19])
                print("\tTasa de mantenimiento:", row[20])


        elif i == 3:
            print("SUBMODELO", i, ":", submodelo3)  # Losas
            print("\t-------")
            for row in cur.execute(tabla3):
                print("\t*****")
                print("\tAño:", row[0])
                print("\tLosas Deportivas Construidas:", row[1])
                print("\tLosas en contrucción:", row[2])
                print("\tLosas obsoletas:", row[3])
                print("\tMantenimiento Losas:", row[4])
                print("\tGastos Totales Losas:", row[5])
                print("\tPresupuesto disponible:", row[6])
                print("\tTasa Losas Construcción:", row[7])
                print("\tTasa Losas Obsoletas:", row[8])
                print("\tTasa de desgaste por clima:", row[9])
                print("\tParticipación ciudadana:", row[10])
                print("\tCapacidad de técnicos de construcción:", row[11])
                print("\tDemanda de espacios deportivos:", row[12])
                print("\tFactor de obsolescencia por uso:", row[13])

        elif i == 4:
            print("SUBMODELO", i, ":", submodelo4)  # Puentes
            print("\t-------")
            for row in cur.execute(tabla4):
                print("\t*****")
                print("\tAño:", row[0])
                print("\tPuentes Construidos:", row[1])
                print("\tPuentes en Construcción:", row[2])
                print("\tPuentes Obsoletos:", row[3])
                print("\tMantenimiento:", row[4])
                print("\tGastos Totales:", row[5])
                print("\tCosto Unitario de Mantenimiento:", row[6])
                print("\tFactor de Uso:", row[7])
                print("\tTasa de calidad de mantenimiento:", row[8])
                print("\tTasa Puentes Construcción:", row[9])
                print("\tTasa de terminación:", row[10])
                print("\tTasa Puentes Obsoletos:", row[11])

        elif i == 5:
            print("SUBMODELO", i, ":", submodelo5)  # Alumbrado publico
            print("\t-------")
            for row in cur.execute(tabla5):
                print("\t*****")
                print("\tAño:", row[0])
                print("\tAlumbrado Público Construidos:", row[1])
                print("\tAlumbrado público en construcción:", row[2])
                print("\tAlumbrado público obsoletas:", row[3])
                print("\tAlumbrado en mantenimiento:", row[4])
                print("\tGastos Totales Alumbrado Público:", row[5])
                print("\tPuntos instalados nuevos:", row[6])
                print("\tPuntos luminarios operativos:", row[7])
                print("\tPuntos retirados por falla:", row[8])
                print("\tMaquinaria comprada:", row[9])
                print("\tPago por técnicos contratados:", row[10])
                print("\tTasa Alumbrado Público Construcción:", row[11])
                print("\tTasa Alumbrado Público Obsoletas:", row[12])
                print("\tTasa de reparación de unidades:", row[13])
                print("\tTasa de retiro de unidades de alumbrado:", row[14])
                print("\tTasa de mantenimiento:", row[15])
                print("\tTasa de instalación de nuevos puntos:", row[16])
                print("\tTasa de retiro de puntos por falla:", row[17])

        i += 1
    return

print("*" * 13, "MENÚ PRINCIPAL", "*" * 13)
print("1. Mostrar registro de todos los submodelos")
print("2. Elegir registro de un submodelo")
print("3. Ver tablas y gráficas")
print("*" * 42, "\n")

# Mostrar todos los registros de las tablas    
numero = input("Elegir la opción: ")
if numero == '1':
    Mostrar_Registros()

# Mostrar los registros de una tabla    
if numero == '2':
    print("-" * 40)
    j = input("-> Ver submodelo: ")
    print("")
    if j == '1':
        print("SUBMODELO", j, ":", submodelo1)  # Veredas
        print("\t-------")
        for row in cur.execute(tabla1):
            print("\tAño:", row[0])
            print("\tVeredas Construidas:", row[1])
            print("\tVeredas en construccion:", row[2])
            print("\tVeredas obsoletas:", row[3])
            print("\tMantenimiento Veredas:", row[4])
            print("\tGastos Totales Veredas:", row[5])
            print("\tTasa Veredas Construccion:", row[6])
            print("\tDemanda de veredas:", row[7])
            print("\tUso de veredas:", row[8])
            print("\tTasa Veredas Obsoletas:", row[9])


    elif j == '2':
        print("SUBMODELO", j, ":", submodelo2)  # Pistas
        print("\t-------")
        for row in cur.execute(tabla2):
            print("\t*******")
            print("\t*******")
            print("\tAño:", row[0])
            print("\tPistas Construidas:", row[1])
            print("\tPistas en construccion:", row[2])
            print("\tPistas obsoletas:", row[3])
            print("\tPistas en mantenimiento:", row[4])
            print("\tPistas reparadas:", row[5])
            print("\tPistas retiradas para mantenimiento:", row[6])
            print("\tFondos para mantenimiento:", row[7])
            print("\tFondos asignados para mantenimiento:", row[8])
            print("\tGastos en mantenimiento:", row[9])
            print("\tMonto Total Pistas:", row[10])
            print("\tCantidad de litros de pintura:", row[11])
            print("\tPistas asfaltadas:", row[12])
            print("\tCantidad de mano de obra persona:", row[13])
            print("\tCantidad de maquinarias total:", row[14])
            print("\tCantidad de maquinas asfaltos:", row[15])
            print("\tTasa Pistas Construccion:", row[16])
            print("\tTasa Pistas Obsoletas:", row[17])
            print("\tTasa de retiro de pistas para mantenimiento:", row[18])
            print("\tTasa de reparacion de pistas:", row[19])
            print("\tTasa de mantenimiento:", row[20])


    elif j == '3':
        print("SUBMODELO", j, ":", submodelo3)  # Losas
        print("\t-------")
        for row in cur.execute(tabla3):
            print("\t*******")
            print("\tAño:", row[0])
            print("\tLosas Deportivas Construidas:", row[1])
            print("\tLosas en construcción:", row[2])
            print("\tLosas obsoletas:", row[3])
            print("\tMantenimiento Losas:", row[4])
            print("\tGastos Totales Losas:", row[5])
            print("\tPresupuesto disponible:", row[6])
            print("\tTasa Losas Construcción:", row[7])
            print("\tTasa Losas Obsoletas:", row[8])
            print("\tTasa de desgaste por clima:", row[9])
            print("\tParticipación ciudadana:", row[10])
            print("\tCapacidad de técnicos de construcción:", row[11])
            print("\tDemanda de espacios deportivos:", row[12])
            print("\tFactor de obsolescencia por uso:", row[13])
  

    elif j == '4':
        print("SUBMODELO", j, ":", submodelo4)  # Puentes
        print("\t-------")
        for row in cur.execute(tabla4):
            print("\t*******")
            print("\tAño:", row[0])
            print("\tPuentes Construidos:", row[1])
            print("\tPuentes en Construcción:", row[2])
            print("\tPuentes Obsoletos:", row[3])
            print("\tMantenimiento:", row[4])
            print("\tGastos Totales:", row[5])
            print("\tCosto Unitario de Mantenimiento:", row[6])
            print("\tFactor de Uso:", row[7])
            print("\tTasa de calidad de mantenimiento:", row[8])
            print("\tTasa Puentes Construcción:", row[9])
            print("\tTasa de terminación:", row[10])
            print("\tTasa Puentes Obsoletos:", row[11])


    elif j == '5':
        print("SUBMODELO", j, ":", submodelo5)  # Alumbrado publico
        print("\t-------")
        for row in cur.execute(tabla5):
            print("\t*******")
            print("\tAño:", row[0])
            print("\tAlumbrado Público Construidos:", row[1])
            print("\tAlumbrado público en construcción:", row[2])
            print("\tAlumbrado público obsoletas:", row[3])
            print("\tAlumbrado en mantenimiento:", row[4])
            print("\tGastos Totales Alumbrado Público:", row[5])
            print("\tPuntos instalados nuevos:", row[6])
            print("\tPuntos luminarios operativos:", row[7])
            print("\tPuntos retirados por falla:", row[8])
            print("\tMaquinaria comprada:", row[9])
            print("\tPago por técnicos contratados:", row[10])
            print("\tTasa Alumbrado Público Construcción:", row[11])
            print("\tTasa Alumbrado Público Obsoletas:", row[12])
            print("\tTasa de reparación de unidades:", row[13])
            print("\tTasa de retiro de unidades de alumbrado:", row[14])
            print("\tTasa de mantenimiento:", row[15])
            print("\tTasa de instalación de nuevos puntos:", row[16])
            print("\tTasa de retiro de puntos por falla:", row[17])

if numero == '3':
    pd.options.display.max_rows = None        # Visualizar todas las filas
    pd.options.display.max_columns = None     # Visualizar todas las columnas
    print("-" * 40)
    j = input("-> Submodelo: ")
    print("")
    if j == '1':
        print("SUBMODELO", j, ":", submodelo1, "\n")  # Veredas
        modelo = pysd.read_vensim('Forrester - Veredas.mdl')
        valores = modelo.run(return_columns=[
            'Veredas Construidas',
            'Veredas en construccion',
            'Veredas obsoletas',
            'Mantenimiento Veredas',
            'Gastos Totales Veredas',
            'Tasa Veredas Construccion',
            'Demanda de veredas',
            'Uso de veredas',
            'Tasa Veredas Obsoletas',
            'Factor de desgaste natural'
        ])
        tabla = valores.head(20)
        print(tabla)

        valores1 = modelo.run(return_columns=[
            'Veredas Construidas',
            'Veredas en construccion',
            'Veredas obsoletas'
        ])
        valores1.plot()
        plt.ylabel('Veredas (Unidades)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()

        valores2 = modelo.run(return_columns=[
            'Gastos Totales Veredas',
            'Mantenimiento Veredas'
        ])
        valores2.plot()
        plt.ylabel('Soles (S/.)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()

    elif j == '2':
        print("SUBMODELO", j, ":", submodelo2, "\n")  # Pistas
        modelo = pysd.read_vensim('Forrester - Pistas.mdl')
        valores = modelo.run(return_columns=[
            'Pistas Construidas',
            'Pistas en construccion',
            'Pistas obsoletas',
            'Pistas en mantenimiento',
            'Pistas reparadas',
            'Pistas retiradas para mantenimiento',
            'Fondos para mantenimiento',
            'Fondos asignados para mantenimiento',
            'Gastos en mantenimiento',
            'Monto Total Pistas',
            'Cantidad de litros de pintura',
            'Pistas asfaltadas',
            'Cantidad de mano de obra persona',
            'Cantidad de maquinarias total',
            'Cantidad maquinas asfaltos',
            'Tasa Pistas Construccion',
            'Tasa Pistas Obsoletas',
            'Tasa de retiro de pistas para mantenimiento',
            'Tasa de reparación de pistas',
            'Tasa de mantenimiento',
            'Costo promedio por mantenimiento'
        ])
        tabla = valores.head(20)
        print(tabla)

        valores1 = modelo.run(return_columns=[
            'Pistas Construidas',
            'Pistas en construccion',
            'Pistas obsoletas',
            'Pistas asfaltadas'
        ])
        valores1.plot()
        plt.ylabel('Pistas (Unidades)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()

        valores2 = modelo.run(return_columns=[
            'Cantidad de litros de pintura',
            'Cantidad maquinas asfaltos',
            'Cantidad de mano de obra persona',
            'Cantidad de maquinarias total'
        ])
        valores2.plot()
        plt.ylabel('Unidades')
        plt.xlabel('Años')
        plt.legend(loc='upper left')
        plt.show()

        valores3 = modelo.run(return_columns=['Monto Total Pistas'])
        valores3.plot()
        plt.ylabel('Soles (S/.)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()

    elif j == '3':
        print("SUBMODELO", j, ":", submodelo3, "\n")  # Losas
        modelo = pysd.read_vensim('Forrester - Losas.mdl')
        valores = modelo.run(return_columns=[
            'Losas Deportivas Construidas',
            'Losas en contruccion',
            'Losas obsoletas',
            'Mantenimiento Losas',
            'Gastos Totales Losas',
            'Presupuesto disponible',
            'Tasa Losas Construccion',
            'Tasa Losas Obsoletas',
            'Tasa de desgaste por clima',
            'Participacion ciudadana',
            'Capacidad de tecnicos de construccion',
            'Demanda de espacios deportivos',
            'Factor de obsolencia por uso',
            'Factor de envejecimiento'
        ])
        tabla = valores.head(20)
        print(tabla)

        valores1 = modelo.run(return_columns=[
            'Losas Deportivas Construidas',
            'Losas en contruccion',
            'Losas obsoletas'
        ])
        valores1.plot()
        plt.ylabel('Losas (Unidades)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()

        valores2 = modelo.run(return_columns=[
            'Gastos Totales Losas',
            'Mantenimiento Losas'
        ])
        valores2.plot()
        plt.ylabel('Soles (S/.)')
        plt.xlabel('Años')
        plt.legend(loc='upper center')
        plt.show()

    elif j == '4':
        print("SUBMODELO", j, ":", submodelo4, "\n")  # Puentes
        modelo = pysd.read_vensim('Forrester - Puentes.mdl')
        valores = modelo.run(return_columns=[
            'Puentes Construidos',
            'Puentes en Construccion',
            'Puentes Obsoletos',
            'Mantenimiento',
            'Gastos Totales',
            'Costo Unitario de Mantenimiento',
            'Factor de Uso',
            'Tasa de calidad de matenimiento',
            'Tasa Puentes Construccion',
            'Tasa de terminacion',
            'Tasa Puentes Obsoletos',
            'Tasa de demolicion'
        ])
        tabla = valores.head(20)
        print(tabla)

        valores1 = modelo.run(return_columns=[
            'Puentes Construidos',
            'Puentes en Construccion',
            'Puentes Obsoletos'
        ])
        valores1.plot()
        plt.ylabel('Puentes (Unidades)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()

        valores2 = modelo.run(return_columns=[
            'Gastos Totales',
            'Mantenimiento'
        ])
        valores2.plot()
        plt.ylabel('Soles (S/.)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()

    elif j == '5':
        print("SUBMODELO", j, ":", submodelo5, "\n")  # Alumbrado público
        modelo = pysd.read_vensim('Forrester - Alumbrado publico.mdl')
        valores = modelo.run(return_columns=[
            'Alumbrado Publico Construidos',
            'Alumbrado publico en construccion',
            'Alumbrado publico obsoletas',
            'Alumbrado en mantenimiento',
            'Unidades retiradas para mantenimiento',
            'Unidades reparadas',
            'Presupuesto mantenimiento',
            'Fondos asignados para mantenimiento',
            'Gastos en mantenimiento',
            'Gastos Totales Alumbrado Publico',
            'Puntos instalados nuevos',
            'Puntos luminarios operativos',
            'Puntos retirados por falla',
            'Maquinaria comprada',
            'Pago por tecnicos contratados',
            'Tasa Alumbrado Publico Construccion',
            'Tasa Alumbrado Publico Obsoletas',
            'Tasa de reparación de unidades',
            'Tasa de retiro de unidades de alumbrado',
            'Tasa de mantenimiento',
            'Tasa de instalación de nuevos puntos',
            'Tasa de retiro de puntos por falla',
            'Costo promedio mantenimiento'
        ])
        tabla = valores.head(20)
        print(tabla)

        valores1 = modelo.run(return_columns=[
            'Alumbrado Publico Construidos',
            'Alumbrado publico en construccion',
            'Alumbrado publico obsoletas'
        ])
        valores1.plot()
        plt.ylabel('Alumbrado público (Unidades)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()

        valores2 = modelo.run(return_columns=[
            'Gastos Totales Alumbrado Público',
            'Alumbrado en mantenimiento',
            'Pago por tecnicos contratados'
        ])
        valores2.plot()
        plt.ylabel('Soles (S/.)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()

        valores3 = modelo.run(return_columns=['Maquinaria comprada'])
        valores3.plot()
        plt.ylabel('Unidades')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()

# Cierra la conexión a la Base de Datos        
cur.close()
connection.close()

