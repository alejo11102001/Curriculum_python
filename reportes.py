import json
import os
import csv
from tabulate import tabulate

RUTA = "datos.json"

def print_warning(text):
    print(f"\033[93m{text}\033[0m")  

def print_error(text):
    print(f"\033[91m{text}\033[0m") 

def print_success(text):
    print(f"\033[92m{text}\033[0m") 
def print_message(text):
    print(text)

def cargar_datos():
    if not os.path.exists(RUTA):
        print_warning(f"Archivo '{RUTA}' no encontrado.")
        return []
    try:
        with open(RUTA, "r", encoding="utf-8") as f:
            datos = json.load(f)
            if not isinstance(datos, list):
                print_warning("El contenido del archivo no es una lista válida.")
                return []
            return datos
    except json.JSONDecodeError:
        print_error("Error al decodificar JSON. Verifique el formato del archivo.")
        return []
    except Exception as e:
        print_error(f"Error al cargar datos: {e}")
        return []

def generar_reporte():
    datos = cargar_datos()
    if not datos:
        print_warning("No hay datos para generar reporte.")
        return

    print("\n\033[96m--- Reporte de Candidatos con más de 2 experiencias ---\033[0m")
    reporte = []
    for d in datos:
        experiencia = d.get("experiencia")
        if experiencia and isinstance(experiencia, list) and len(experiencia) > 2:
            nombre = d.get("nombre", "N/A")
            documento = d.get("documento", "N/A")
            habilidades = d.get("habilidades")
            if habilidades and isinstance(habilidades, list):
                habilidades_str = ", ".join(str(h) for h in habilidades)
            else:
                habilidades_str = "\033[93mNo definidas\033[0m"  
            reporte.append([nombre, documento, len(experiencia), habilidades_str])

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
        print_warning("Ningún candidato cumple el criterio.")
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
        print_warning("No hay datos para exportar.")
        return
    try:
        with open("exportado.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Nombre", "Documento", "Correo", "Experiencia"])
            for d in datos:
                nombre = d.get("nombre", "")
                documento = d.get("documento", "")
                correo = d.get("correo", "")
                experiencia = d.get("experiencia")
                if experiencia and isinstance(experiencia, list):
                    experiencia_str = ", ".join(str(e.get("duracion", "")) for e in experiencia if isinstance(e, dict))
                else:
                    experiencia_str = ""
                writer.writerow([nombre, documento, correo, experiencia_str])
        print_success("Datos exportados a exportado.csv correctamente.")
    except Exception as e:
        print_error(f"Error al exportar datos: {e}")
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
