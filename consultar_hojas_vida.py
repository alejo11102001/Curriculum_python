from main import *
from hojasdevida import *

def searchCVName():
    name = input("Ingrese el nombre: ")
    name = name.title()
    print(name)
    if name in people["datos_personales"]:
        print("Su nombre esta en la base de datos.")

def searchCVID():
    identify = input("Ingrese el numero de identificacion: ")
    print(identify)
    if identify in people["datos_personales"]:
        print("Su nombre esta en la base de datos.")

def searchCVEmail():
    email = input("Ingrese el correo electronico: ")

def optionUser():
    print("1. Buscar por nombre")
    print("2. Buscar por numero de identificacion")
    print("3. Buscar por correo electronico")
    print("4. Salir")
    option= input("¿Como desea buscar la hoja de vida: ")
    return(option)


def searchMain():
    option = optionUser()
    while True:
        match option:
            case "1":
                searchCVName()
            case "2":
                searchCVID()
            case "3":
                searchCVEmail()
            case "4":
                print("Regresando al menu principal.")
                break
            case _:
                print("La opcion no esta en el menu.")
            
searchMain()