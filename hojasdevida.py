# Módulo de gestión de hojas de vida

import json
import os
import re
from datetime import datetime

RUTA = "datos.json"

def cargar_datos():
    if not os.path.exists(RUTA):
        return []
    with open(RUTA, "r") as f:
        return json.load(f)

def guardar_datos(datos):
    with open(RUTA, "w") as f:
        json.dump(datos, f, indent=4)

def input_no_vacio(mensaje):
    dato = input(mensaje).strip()
    while not dato:
        print("Este campo no puede estar vacío.")
        dato = input(mensaje).strip()
    return dato

def input_documento(mensaje):
    doc = input(mensaje).strip()
    while not doc.isdigit() or len(doc) < 5:
        print("Documento inválido. Debe contener solo números y tener al menos 5 dígitos.")
        doc = input(mensaje).strip()
    return doc

def input_correo(mensaje):
    correo = input(mensaje).strip()
    while not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        print("Correo electrónico inválido.")
        correo = input(mensaje).strip()
    return correo

def input_fecha(mensaje):
    while True:
        fecha = input(mensaje).strip()
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Formato de fecha inválido. Usa AAAA-MM-DD.")

def input_telefono(mensaje):
    tel = input(mensaje).strip()
    while not tel.isdigit() or len(tel) < 7:
        print("Teléfono inválido. Debe contener solo números y tener al menos 7 dígitos.")
        tel = input(mensaje).strip()
    return tel

def registrar_hoja_de_vida():
    datos = cargar_datos()
    nueva = {}

    print("\n--- Registro de Hoja de Vida ---")
    nueva["nombre"] = input_no_vacio("Nombre completo: ")
    nueva["documento"] = input_documento("Documento: ")
    nueva["contacto"] = input_telefono("Número de contacto: ")
    nueva["direccion"] = input_no_vacio("Dirección: ")
    nueva["correo"] = input_correo("Correo electrónico: ")
    nueva["fecha_nacimiento"] = input_fecha("Fecha de nacimiento (AAAA-MM-DD): ")

    nueva["formacion"] = []
    while True:
        print("Agregar formación académica:")
        formacion = {
            "institucion": input_no_vacio("  Institución: "),
            "titulo": input_no_vacio("  Título: "),
            "años": input_no_vacio("  Años: ")
        }
        nueva["formacion"].append(formacion)
        if input("¿Agregar otra formación? (s/n): ").lower() != "s":
            break

    nueva["experiencia"] = []
    while True:
        print("Agregar experiencia profesional:")
        exp = {
            "empresa": input_no_vacio("  Empresa: "),
            "cargo": input_no_vacio("  Cargo: "),
            "funciones": input_no_vacio("  Funciones: "),
            "duracion": input_no_vacio("  Duración: ")
        }
        nueva["experiencia"].append(exp)
        if input("¿Agregar otra experiencia? (s/n): ").lower() != "s":
            break

    nueva["referencias"] = []
    while True:
        print("Agregar referencia:")
        ref = {
            "nombre": input_no_vacio("  Nombre: "),
            "relacion": input_no_vacio("  Relación: "),
            "telefono": input_telefono("  Teléfono: ")
        }
        nueva["referencias"].append(ref)
        if input("¿Agregar otra referencia? (s/n): ").lower() != "s":
            break

    habilidades = input("Ingrese habilidades separadas por coma: ").strip()
    nueva["habilidades"] = [h.strip() for h in habilidades.split(",") if h.strip()]

    datos.append(nueva)
    guardar_datos(datos)
    print("✅ Hoja de vida registrada correctamente.")

def buscar_hoja_de_vida():
    datos = cargar_datos()
    criterio = input("Buscar por nombre, documento o correo: ").lower()
    encontrados = []

    for d in datos:
        if criterio in d["nombre"].lower() or criterio in d["documento"] or criterio in d["correo"].lower():
            encontrados.append(d)

    if encontrados:
        for e in encontrados:
            print(json.dumps(e, indent=4, ensure_ascii=False))
    else:
        print("❌ No se encontraron resultados.")

def actualizar_hoja_de_vida():
    datos = cargar_datos()
    documento = input_documento("Ingrese el documento de la persona a actualizar: ")

    for d in datos:
        if d["documento"] == documento:
            print("Datos actuales:")
            print(json.dumps(d, indent=4, ensure_ascii=False))
            d["contacto"] = input_telefono("Nuevo contacto: ")
            d["direccion"] = input_no_vacio("Nueva dirección: ")
            d["correo"] = input_correo("Nuevo correo: ")
            guardar_datos(datos)
            print("✅ Información actualizada correctamente.")
            return

    print("❌ No se encontró hoja de vida con ese documento.")
