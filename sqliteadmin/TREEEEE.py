
import tkinter
import datetime
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sys


import time
def confe11():
    conexion = sqlite3.connect('final.s3db')
    cursor=conexion.cursor()
    cursor.execute('select * from profesores')
    sql="update profesores set Nombre='"+nombre276.get()+"', Apellido='"+nombre376.get()+"',DNI='"+nombre476.get()+"' where Codigo="+nombre180.get()
    cursor.execute(sql)
    conexion.commit()
   

def guardar2():
    conexion = sqlite3.connect('final.s3db')
    cursor=conexion.cursor()
    datos= cod31.get(), nom31.get(), cred31.get()
    cursor.execute("insert into cursos(codcurso,nomcur,cred) values (?,?,?)",(datos))
    cursor.execute('select * from cursos')
    cred=cred31.get()
    if not (cred.isdigit()):
        messagebox.showwarning(" Sr!", "Creditaje incorrecto")
    cod31.delete(0,END)
    nom31.delete(0,END)
    cred31.delete(0,END)
    
  
    return

def confe():
    
    conexion = sqlite3.connect('final.s3db')
    cursor=conexion.cursor()
    cursor.execute('select * from cursos')
    sql="update cursos set nomcur='"+nombre270.get()+"', cred='"+nombre370.get()+"' where codcurso="+nombre170.get()
    cursor.execute(sql)
    conexion.commit()
    
    raiz100.destroy()
    return
def report1(): 
    global raiz5
    raiz5=Tk()
    raiz5.title(" Universidad Nacional de Ingeniería")
    raiz5.configure(background="olive Drab2")
    raiz5.iconbitmap('logo_uni.ico')
    raiz5.config(width="700",height="400")
    
## -------------------------------------------------------- hago mi conexion y creo mi var cursor   
    miConexion = sqlite3.connect ("final.s3db")
    miCursor = miConexion.cursor ()
## --------------------------------------------------------
## ire a mostrar registrs en pantalla:
    nombre123=Label(raiz5,text="Reporte de Docentes ",fg="blue",font=("bold",18,""))
    nombre123.place(x=40,y=50)
    
    ## grafico, diseño mi hoja de filas columnas: treeview()
    
    tree=ttk.Treeview(raiz5,height=12,columns=('#0','#1','#2','#3')) ## grafico standar p reportes
    tree.place(x=0,y=100)
    
    tree.heading('#0', text="Código  ",anchor=CENTER)
    tree.heading('#1', text="Nombre  ",anchor=CENTER)
    tree.heading('#2', text="Apellido",anchor=CENTER)
    
    tree.column('#0',width=80)
    tree.heading('#3', text="DNI",anchor=CENTER)
## Ejecuto mi cursor segun lo que dedso ver : registros
    
    miCursor.execute("SELECT * FROM profesores")

## colocar registros en TreeView 

    for row in miCursor: ## dsde mi ba jalo filas al arbol 

        tree.insert("",0,text=row[0], values=(row[1],row[2],row[3]))
        
     
    botonvolver=tkinter.Button (raiz5,text = "Volver al menú", font=("Times New Roman",14), bg="green", command = volv123).place(x=170,y=300)
confe11()
guardar2()
confe()
report1()
