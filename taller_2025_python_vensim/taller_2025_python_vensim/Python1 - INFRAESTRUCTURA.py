

import sqlite3                      #Para importar de SQLite
import pysd                         #Para las tablas
import matplotlib.pyplot as plt     #Para las graficas
import pandas as pd                 #Para visualizar la tabla completa

#Conexion a la Base de Datos
connection = sqlite3.connect("DB_Infraestructura.s3db")
cur = connection.cursor()

print("* Conectando a la Base de Datos: DB_Infraestructura","\n")
print("\t\t\tSUBSISTEMA DE INFRAESTRUCTURA","\n")
    
tabla1 = "SELECT * FROM Veredas"
tabla2 = "SELECT * FROM Pistas"
tabla3 = "SELECT * FROM Losas"
tabla4 = "SELECT * FROM Puentes"
tabla5 = "SELECT * FROM Alumbrado_publico"

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

#Funcion que permite mostrar todos los registros de las tablas    
def Mostrar_Registros():
    i = 1
    for num in range(1,6):
        print("-"*30)
        if i == 1 :
            print("SUBMODELO",i,":",submodelo1)
            for row in cur.execute(tabla1):
                print("\tAño:",row[0])
                print("\tConstruidos:",row[1])
                print("\tEn construccion:",row[2])
                print("\tObsoletos:",row[3])
                print("\tMantenimiento:",row[4])
                print("\tGastos totales:",row[5],"\n")
        if i == 2 :
            print("SUBMODELO",i,":",submodelo2)
            for row in cur.execute(tabla2):
                print("\tAño:",row[0])
                print("\tConstruidos:",row[1])
                print("\tEn construccion:",row[2])
                print("\tObsoletos:",row[3])
                print("\tPistas Asfaltadas:",row[4])
                print("\tMonto Total:",row[5])
                print("\tCantidad mano de obra persona:",row[6])
                print("\tCantidad de maquinas asfaltadas:",row[7])
                print("\tCantidad de litros de pintura:",row[8])
                print("\tCantidad de maquinas totales:",row[9],"\n")
        if i == 3 :
            print("SUBMODELO",i,":",submodelo3)
            for row in cur.execute(tabla3):
                print("\tAño:",row[0])
                print("\tConstruidos:",row[1])
                print("\tEn construccion:",row[2])
                print("\tObsoletos:",row[3])
                print("\tMantenimiento:",row[4])
                print("\tGastos totales:",row[5])
                print("\tTasa en construccion:",row[6])
                print("\tTasa obsoleta:",row[7],"\n")
        if i == 4 :
            print("SUBMODELO",i,":",submodelo4)
            for row in cur.execute(tabla4):
                print("\tAño:",row[0])
                print("\tConstruidos:",row[1])
                print("\tEn construccion:",row[2])
                print("\tObsoletos:",row[3])
                print("\tTasa en construccion:",row[4])
                print("\tTasa obsoleta:",row[5])
                print("\tGastos totales:",row[6])
                print("\tMantenimiento:",row[7],"\n")
        if i == 5 :
            print("SUBMODELO",i,":",submodelo5)
            for row in cur.execute(tabla5):
                print("\tAño:",row[0])
                print("\tConstruidos:",row[1])
                print("\tEn construccion:",row[2])
                print("\tObsoletos:",row[3])
                print("\tGastos totales:",row[4])
                print("\tMantenimiento:",row[5])
                print("\tMaquinarias compradas:",row[6])
                print("\tPagos tecnicos contratados:",row[7])
                print("\tTasa en construccion:",row[8])
                print("\tTasa obsoleta:",row[9],"\n")
                
        i = i+1
        return

    
        
# Menú Principal"    
print("*"*13,"MENÚ PRINCIPAL","*"*13)
print("1. Mostrar registro de todos los submodelos")
print("2. Elegir registro de un submodelo")
print("3. Ver tablas y gráficas")
print("*"*42,"\n")
    
#Mostrar todos los registros de las tablas    
numero = input("Elegir la opción: ")
if numero == '1':
    Mostrar_Registros()

#Mostrar los registros de una tabla    
if numero == '2':
    print("-"*40)
    j = input("-> Ver submodelo: ")
    print("")
    if j == '1' :
        print("SUBMODELO",j,":",submodelo1)
        for row in cur.execute(tabla1):
            print("\tAño:",row[0])
            print("\tConstruidos:",row[1])
            print("\tEn construccion:",row[2])
            print("\tObsoletos:",row[3])
            print("\tMantenimiento:",row[4])
            print("\tGastos totales:",row[5],"\n")
    if j == '2' :
        print("SUBMODELO",j,":",submodelo2)
        for row in cur.execute(tabla2):
            print("\tAño:",row[0])
            print("\tConstruidos:",row[1])
            print("\tEn construccion:",row[2])
            print("\tObsoletos:",row[3])
            print("\tPistas Asfaltadas:",row[4])
            print("\tMonto Total:",row[5])
            print("\tCantidad mano de obra persona:",row[6])
            print("\tCantidad de maquinas asfaltadas:",row[7])
            print("\tCantidad de litros de pintura:",row[8])
            print("\tCantidad de maquinas totales:",row[9],"\n")
    if j == '3' :
        print("SUBMODELO",j,":",submodelo3)
        for row in cur.execute(tabla3):
            print("\tAño:",row[0])
            print("\tConstruidos:",row[1])
            print("\tEn construccion:",row[2])
            print("\tObsoletos:",row[3])
            print("\tMantenimiento:",row[4])
            print("\tGastos totales:",row[5])
            print("\tTasa en construccion:",row[6])
            print("\tTasa obsoleta:",row[7],"\n")
    if j == '4' :
        print("SUBMODELO",j,":",submodelo4)
        for row in cur.execute(tabla4):
            print("\tAño:",row[0])
            print("\tConstruidos:",row[1])
            print("\tEn construccion:",row[2])
            print("\tObsoletos:",row[3])
            print("\tTasa en construccion:",row[4])
            print("\tTasa obsoleta:",row[5])
            print("\tGastos totales:",row[6])
            print("\tMantenimiento:",row[7],"\n")
    if j == '5' :
        print("SUBMODELO",j,":",submodelo5)
        for row in cur.execute(tabla5):
            print("\tAño:",row[0])
            print("\tConstruidos:",row[1])
            print("\tEn construccion:",row[2])
            print("\tObsoletos:",row[3])
            print("\tGastos totales:",row[4])
            print("\tMantenimiento:",row[5])
            print("\tMaquinarias compradas:",row[6])
            print("\tPagos tecnicos contratados:",row[7])
            print("\tTasa en construccion:",row[8])
            print("\tTasa obsoleta:",row[9],"\n")

#Mostrar tablas y graficas de una tabla       
if numero == '3':
    pd.options.display.max_rows=None        #Visualizar todas las filas
    pd.options.display.max_columns=None     #Visualizar todas las columnas
    print("-"*40)
    j = input("-> Submodelo: ")
    print("")
    if j == '1' :
        print("SUBMODELO",j,":",submodelo1,"\n")
        modelo = pysd.read_vensim('Forrester - Veredas.mdl')
        valores = modelo.run(return_columns = ['Veredas Construidas',
        'Veredas en construccion','Veredas obsoletas',
        'Tasa Veredas Construccion','Tasa Veredas Obsoletas',
        'Gastos Totales Veredas','Mantenimiento Veredas'])
        tabla = valores.head(20)
        print(tabla)
        valores1 = modelo.run(return_columns = ['Veredas Construidas',
        'Veredas en construccion','Veredas obsoletas'])
        valores1.plot()
        plt.ylabel('Veredas (Unidades)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()
        valores2 = modelo.run(return_columns = ['Gastos Totales Veredas',
        'Mantenimiento Veredas'])
        valores2.plot()
        plt.ylabel('Soles (S/.)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()
    if j == '2' :
        print("SUBMODELO",j,":",submodelo2,"\n")
        modelo = pysd.read_vensim('Forrester - Pistas.mdl')
        valores = modelo.run(return_columns = ['Pistas Construidas',
        'Pistas en construccion','Pistas obsoletas',
        'Tasa Pistas Construccion','Tasa Pistas Obsoletas',
        'Pistas asfaltadas','Cantidad de litros de pintura',
        'Cantidad maquinas asfaltos','Cantidad de mano de obra persona',
        'Cantidad de maquinarias total','Monto Total Pistas'])
        tabla = valores.head(20)
        print(tabla)
        valores1 = modelo.run(return_columns = ['Pistas Construidas',
        'Pistas en construccion','Pistas obsoletas','Pistas asfaltadas'])
        valores1.plot()
        plt.ylabel('Pistas (Unidades)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()
        valores2 = modelo.run(return_columns = ['Cantidad de litros de pintura',
        'Cantidad maquinas asfaltos','Cantidad de mano de obra persona',
        'Cantidad de maquinarias total'])
        valores2.plot()
        plt.ylabel('Unidades')
        plt.xlabel('Años')
        plt.legend(loc='upper left')
        plt.show()
        valores3 = modelo.run(return_columns = ['Monto Total Pistas'])
        valores3.plot()
        plt.ylabel('Soles (S/,)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()
    if j == '3' :
        print("SUBMODELO",j,":",submodelo3,"\n")
        modelo = pysd.read_vensim('Forrester - Losas.mdl')
        valores = modelo.run(return_columns = ['Losas Deportivas Construidas',
        'Losas en contruccion','Losas obsoletas','Tasa Losas Obsoletas',
        'Gastos Totales Losas','Mantenimiento Losas'])
        tabla = valores.head(20)
        print(tabla)
        valores1 = modelo.run(return_columns = ['Losas Deportivas Construidas',
        'Losas en contruccion','Losas obsoletas'])
        valores1.plot()
        plt.ylabel('Losas (Unidades)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()
        valores2 = modelo.run(return_columns = ['Gastos Totales Losas',
        'Mantenimiento Losas'])
        valores2.plot()
        plt.ylabel('Soles (S/.)')
        plt.xlabel('Años')
        plt.legend(loc='upper center')
        plt.show()
    if j == '4' :
        print("SUBMODELO",j,":",submodelo4,"\n")
        modelo = pysd.read_vensim('Forrester - Puentes.mdl')
        valores = modelo.run(return_columns = ['Puentes Construidos',
        'Puentes en Construccion','Puentes Obsoletos',
        'Tasa Puentes Construccion','Tasa Puentes Obsoletos',
        'Gastos Totales','Mantenimiento'])
        tabla = valores.head(20)
        print(tabla)
        valores1 = modelo.run(return_columns = ['Puentes Construidos',
        'Puentes en Construccion','Puentes Obsoletos'])
        valores1.plot()
        plt.ylabel('Puentes (Unidades)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()
        valores2 = modelo.run(return_columns = ['Gastos Totales',
        'Mantenimiento'])
        valores2.plot()
        plt.ylabel('Soles (S/.)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()
    if j == '5' :
        print("SUBMODELO",j,":",submodelo5,"\n")
        modelo = pysd.read_vensim('Forrester - Alumbrado publico.mdl')
        valores = modelo.run(return_columns = ['Alumbrado Publico Construidos',
        'Alumbrado publico en construccion','Alumbrado publico obsoletas',
        'Tasa Alumbrado Publico Construccion','Tasa Alumbrado Publico Obsoletas',
        'Gastos Totales Alumbrado Publico','Mantenimiento Alumbrado Publico',
        'Pago por tecnicos contratados','Maquinaria comprada'])
        tabla = valores.head(20)
        print(tabla)
        valores1 = modelo.run(return_columns = ['Alumbrado Publico Construidos',
        'Alumbrado publico en construccion','Alumbrado publico obsoletas'])
        valores1.plot()
        plt.ylabel('Alumbrado público (Unidades)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()
        valores2 = modelo.run(return_columns = ['Gastos Totales Alumbrado Publico',
        'Mantenimiento Alumbrado Publico','Pago por tecnicos contratados'])
        valores2.plot()
        plt.ylabel('Soles (S/.)')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()
        valores3 = modelo.run(return_columns = ['Maquinaria comprada'])
        valores3.plot()
        plt.ylabel('Unidades')
        plt.xlabel('Años')
        plt.legend(loc='center right')
        plt.show()

#Cierra las conexion a la Base de Datos        
cur.close()
connection.close()
