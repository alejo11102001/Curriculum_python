# Módulo de gestión de hojas de vida

import json
import os
from datetime import datetime

RUTA = "datos.json"

# Función para cargar los datos desde el archivo JSON
def cargar_datos():
    if not os.path.exists(RUTA):
        return []
    with open(RUTA, "r") as f:
        return json.load(f)

# Función para guardar los datos al archivo JSON
def guardar_datos(datos):
    with open(RUTA, "w") as f:
        json.dump(datos, f, indent=4)

# Función para registrar una nueva hoja de vida
def registrar_hoja_de_vida():
    datos = cargar_datos()
    nueva = {}

    print("\n--- Registro de Hoja de Vida ---")
    nueva["nombre"] = input("Nombre completo: ")
    nueva["documento"] = input("Documento: ")
    nueva["contacto"] = input("Número de contacto: ")
    nueva["direccion"] = input("Dirección: ")
    nueva["correo"] = input("Correo electrónico: ")
    nueva["fecha_nacimiento"] = input("Fecha de nacimiento (AAAA-MM-DD): ")

    nueva["formacion"] = []
    while True:
        print("Agregar formación académica:")
        formacion = {
            "institucion": input("  Institución: "),
            "titulo": input("  Título: "),
            "años": input("  Años: ")
        }
        nueva["formacion"].append(formacion)
        if input("¿Agregar otra formación? (s/n): ").lower() != "s":
            break

    nueva["experiencia"] = []
    while True:
        print("Agregar experiencia profesional:")
        exp = {
            "empresa": input("  Empresa: "),
            "cargo": input("  Cargo: "),
            "funciones": input("  Funciones: "),
            "duracion": input("  Duración: ")
        }
        nueva["experiencia"].append(exp)
        if input("¿Agregar otra experiencia? (s/n): ").lower() != "s":
            break

    nueva["referencias"] = []
    while True:
        print("Agregar referencia:")
        ref = {
            "nombre": input("  Nombre: "),
            "relacion": input("  Relación: "),
            "telefono": input("  Teléfono: ")
        }
        nueva["referencias"].append(ref)
        if input("¿Agregar otra referencia? (s/n): ").lower() != "s":
            break

    habilidades = input("Ingrese habilidades separadas por coma: ")
    nueva["habilidades"] = [h.strip() for h in habilidades.split(",")]

    datos.append(nueva)
    guardar_datos(datos)
    print("Hoja de vida registrada correctamente.")

# Función para buscar una hoja de vida
def buscar_hoja_de_vida():
    datos = cargar_datos()
    criterio = input("Buscar por nombre, documento o correo: ").lower()
    encontrados = []

    for d in datos:
        if criterio in d["nombre"].lower() or criterio in d["documento"] or criterio in d["correo"].lower():
            encontrados.append(d)

    if encontrados:
        for e in encontrados:
            print(json.dumps(e, indent=4))
    else:
        print("No se encontraron resultados.")

# Función para actualizar una hoja de vida
def actualizar_hoja_de_vida():
    datos = cargar_datos()
    documento = input("Ingrese el documento de la persona a actualizar: ")

    for d in datos:
        if d["documento"] == documento:
            print("Datos actuales:")
            print(json.dumps(d, indent=4))
            d["contacto"] = input("Nuevo contacto: ")
            d["direccion"] = input("Nueva dirección: ")
            d["correo"] = input("Nuevo correo: ")
            guardar_datos(datos)
            print("Información actualizada correctamente.")
            return

    print("No se encontró hoja de vida con ese documento.")