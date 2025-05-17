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

def generar_reporte():
    datos = cargar_datos()
    if not datos:
        print("\033[91mNo hay datos para generar reporte.\033[0m")
        return

    print("\n--- Reporte de Candidatos con más de 2 experiencias ---")
    reporte = [
        [d["nombre"], d["documento"], len(d["experiencia"]), ", ".join(d["habilidades"])]
        for d in datos if len(d.get("experiencia", [])) > 2
    ]

    if reporte:
        print(tabulate(reporte, headers=["Nombre", "Documento", "Experiencias", "Habilidades"], tablefmt="grid"))
    else:
        print("\033[91mNingún candidato cumple el criterio.\033[0m")

def exportar_datos():
    datos = cargar_datos()
    with open("exportado.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Documento", "Correo", "Experiencia"])
        for d in datos:
            experiencia = ", ".join([e.get("duracion", "") for e in d.get("experiencia", [])])
            writer.writerow([d.get("nombre", ""), d.get("documento", ""), d.get("correo", ""), experiencia])
    print("\033[92mDatos exportados a exportado.csv correctamente.\033[0m")

def reporte_por_formacion():
    datos = cargar_datos()
    if not datos:
        print("No hay datos disponibles.")
        return

    print("\n¿Desea buscar por:")
    print("1. Formación académica")
    print("2. Habilidades")

    opcion = input("Seleccione una opción (1 o 2): ").strip()
    if opcion not in ["1", "2"]:
        print("Opción inválida.")
        return

    criterio = input("Ingrese el término de búsqueda: ").lower()
    encontrados = []

    for d in datos:
        if opcion == "1":
            for f in d.get("formacion", []):
                if criterio in f.get("titulo", "").lower():
                    encontrados.append([d["nombre"], d["documento"], f.get("institucion", ""), f.get("titulo")])
                    break
        elif opcion == "2":
            for h in d.get("habilidades", []):
                if criterio in h.lower():
                    encontrados.append([d["nombre"], d["documento"], ", ".join(d.get("habilidades", []))])
                    break

    if encontrados:
        if opcion == "1":
            print(tabulate(encontrados, headers=["Nombre", "Documento", "Institución", "Título"], tablefmt="grid"))
        else:
            print(tabulate(encontrados, headers=["Nombre", "Documento", "Habilidades"], tablefmt="grid"))
    else:
        print("No se encontraron candidatos con ese criterio.")