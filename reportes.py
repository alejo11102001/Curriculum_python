# Módulo para generación de reportes

import json
import os
import csv
from tabulate import tabulate

RUTA = "datos.json"

def cargar_datos():
    if not os.path.exists(RUTA):
        return []
    with open(RUTA, "r") as f:
        return json.load(f)

# Genera un reporte en consola con tabulate
def generar_reporte():
    datos = cargar_datos()
    if not datos:
        print("No hay datos para generar reporte.")
        return

    print("\n--- Reporte de Candidatos con más de 2 experiencias ---")
    reporte = []
    for d in datos:
        if len(d["experiencia"]) > 2:
            reporte.append([d["nombre"], d["documento"], len(d["experiencia"]), ", ".join(d["habilidades"])])

    if reporte:
        print(tabulate(reporte, headers=["Nombre", "Documento", "Experiencias", "Habilidades"]))
    else:
        print("Ningún candidato cumple el criterio.")

# Exporta los datos a CSV
def exportar_datos():
    datos = cargar_datos()
    with open("exportado.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Documento", "Correo", "Experiencia"])
        for d in datos:
            experiencia = ", ".join([e["duracion"] for e in d["experiencia"]])
            writer.writerow([d["nombre"], d["documento"], d["correo"], experiencia])
    print("Datos exportados a exportado.csv correctamente.")

def reporte_por_formacion():
    datos = cargar_datos()
    if not datos:
        print("No hay datos disponibles.")
        return

    criterio = input("Ingrese la certificación o formación que desea buscar: ").lower()
    encontrados = []

    for d in datos:
        formaciones = d.get("formacion", [])
        for f in formaciones:
            titulo = f.get("titulo", "").lower()
            if criterio in titulo:
                institucion = f.get("institucion", "No especificada")
                encontrados.append([
                    d["nombre"],
                    d["documento"],
                    institucion,
                    f["titulo"]
                ])
                break  # Ya lo agregamos, no es necesario seguir revisando más formaciones

    if encontrados:
        print("\n--- Candidatos con formación relacionada con:", criterio, "---")
        print(tabulate(encontrados, headers=["Nombre", "Documento", "Institución", "Título"]))
    else:
        print("No se encontraron candidatos con esa formación.")

