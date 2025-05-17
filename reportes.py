# Módulo para generación de reportes

import json
import os
import csv
from tabulate import tabulate

RUTA = "datos.json"

def cargar_datos():
    if not os.path.exists(RUTA):
        return []
    try:
        with open(RUTA, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Error al leer el archivo de datos. Verifica el formato JSON.")
        return []

# Genera un reporte en consola usando tabulate
def generar_reporte():
    datos = cargar_datos()
    if not datos:
        print("⚠️ No hay datos disponibles para generar reporte.")
        return

    print("\n📊 --- Reporte: Candidatos con más de 2 experiencias ---")
    reporte = []
    for d in datos:
        if isinstance(d.get("experiencia"), list) and len(d["experiencia"]) > 2:
            nombre = d.get("nombre", "Desconocido")
            doc = d.get("documento", "N/D")
            exp_count = len(d["experiencia"])
            habilidades = ", ".join(d.get("habilidades", []))
            reporte.append([nombre, doc, exp_count, habilidades])

    if reporte:
        print(tabulate(reporte, headers=["Nombre", "Documento", "Experiencias", "Habilidades"], tablefmt="grid"))
    else:
        print("ℹ️ Ningún candidato cumple con más de 2 experiencias.")

# Exporta los datos a un archivo CSV
def exportar_datos():
    datos = cargar_datos()
    if not datos:
        print("⚠️ No hay datos para exportar.")
        return

    try:
        with open("exportado.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Nombre", "Documento", "Correo", "Cantidad Experiencias", "Habilidades"])

            for d in datos:
                nombre = d.get("nombre", "N/A")
                documento = d.get("documento", "N/A")
                correo = d.get("correo", "N/A")
                experiencia = len(d.get("experiencia", []))
                habilidades = ", ".join(d.get("habilidades", []))
                writer.writerow([nombre, documento, correo, experiencia, habilidades])
        print("✅ Datos exportados correctamente a 'exportado.csv'.")
    except Exception as e:
        print(f"❌ Error al exportar datos: {e}")
