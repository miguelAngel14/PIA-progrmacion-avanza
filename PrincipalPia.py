import re
#importamos a la libreria de expresiones regulares 
import csv
#utilizamos esta sentecia para que pueda leer los datos del archivo csv
import os
#utilizaos la funcion de llamar al sistema operativo
#importamos el objeto que habiamos echo en el 1 programa 
from mis.Contactos import CONTACTO
#declaramos las variables a utilizar
Lista_Contactos=[]
#utilizamos una lista fuera las expresiones par que guarde los datos 
def Cargar_Archivo():
    with open('contactos_mobil.csv') as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter='|')
        contador_lineas = 0
        for linea in lector:
            if contador_lineas == 0:
                
                print(f'Los nombres de columna son {", ".join(linea)}')
            else:
                #instanciamos un objeto que es temporal
                objeto_temporal = CONTACTO({linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]})
                Lista_Contactos.append(objeto_temporal)
 
            # Utilizamos un contador para la cuestion de los contactos
            contador_lineas += 1
    print(f'Procesadas {len(Lista_Contactos)} líneas.')
 
def Menu_Principal():
    while True:
        LimpiarPantalla = lambda: os.system('cls')
        print("MENU CONTACTOS")
        print("[1] Agregar un contacto")
        print("[2] Buscar un contacto")
        print("[3] Eliminar un contacto")
        print("[4] Mostrar contactos")
        print("[5] Serializar datos")
        print("[0] Salir")
        _resp= input("Opcion: ")
 
        if _resp == 1:
            Agregar_Contacto()
        elif _resp== 2:
            Buscar_Contacto()
        elif _resp== 3:
            Eliminar_Contacto()
        elif _resp== 4:
            Mostrar_Contactos()
        elif _resp == 5:
            Serializar_Contacto()
        elif _resp == 0:
            print("programa finalizado")
            break
        else:
            print("Opcion Invalida\nIntente de nuevo")
def Validar(txt):
    pass
def Agregar_Contacto():
    pass
def Buscar_Contacto():
    pass
def Eliminar_Contacto():
    pass
def Mostrar_Contactos():
    pass
def Serializar_Contacto():
    pass
 
Cargar_archivos()

Menu_Principal()
