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
        print("\033[91mN\033[93mo\033[92m \033[96mh\033[94ma\033[95my\033[91m \033[93md\033[92ma\033[96mt\033[94mo\033[95ms \033[91mp\\033[93ma\033[92mr\033[96a\033[94m \033[95m g\033[91me\033[93mn\033[92me\033[96mr\033[94ma\033[95mr\033[91m \033[93mr\033[92me\033[96mp\033[94mo\033[95mr\033[91mt\033[93e\033[92m.\033[0m")
        return

    print("\n--- Reporte de Candidatos con más de 2 experiencias ---")
    reporte = []
    for d in datos:
        if "experiencia" in d and len(d["experiencia"]) > 2:
            reporte.append([d.get("nombre", "N/A"), d.get("documento", "N/A"), len(d["experiencia"]), ", ".join(d.get("habilidades", []))])

    if reporte:
        print(tabulate(reporte, headers=["Nombre", "Documento", "Experiencias", "Habilidades"]))
    else:
        print("\033[91mN\033[93mi\033[92mng\033[96mu\033[94mn\033[95m c\033[91ma\033[93md\033[92mi\033[96md\033[94ma\033[95mt\033[91mo\033[93s \033[92mc\033[96mu\033[94ml\033[95mp\033[91l\033[93en \033[92me\033[96l \033[94mcr\033[95mité\033[91mr\033[93io.\033[0m")

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
                break 

    if encontrados:
        print("\n--- Candidatos con formación relacionada con:", criterio, "---")
        print(tabulate(encontrados, headers=["Nombre", "Documento", "Institución", "Título"]))
    else:
        print("No se encontraron candidatos con esa formación.")

    if not datos:
        print("\033[91mN\033[93mo\033[92m \033[96mh\033[94aa\033[95my\033[91m \033[93md\033[92ma\033[96mt\033[94oo\033[95s \033[91mp\033[93ma\033[92mr\033[96a \033[94me\033[95mx\033[91mp\033[93mo\033[92nr\033[96ta\033[94mr.\033[0m")
        return

    try:
        with open("exportado.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Nombre", "Documento", "Correo", "Experiencia"])
            for d in datos:
                experiencia = ", ".join([e.get("duracion", "") for e in d.get("experiencia", [])])
                writer.writerow([d.get("nombre", ""), d.get("documento", ""), d.get("correo", ""), experiencia])
        print("\033[92mD\033[96ma\033[94mt\033[95os \033[91me\033[93mx\033[92mp\033[96mo\033[94mr\033[95ta\033[91md\033[93os \033[92ma\033[96a\033[94r\033[95ch\033[91iv\033[93o\033[92s \033[96ce\033[94xr\033[95rp\033[91lo\033[93rt\033[92ad\033[96o.\033[0m")
    except Exception as e:
        print(f"\033[91mE\033[93mr\033[92mr\033[96mo\033[94rr \033[95mal\033[91m e\033[93mx\033[92mp\033[96or\033[94ttar \033[95md\033[91aatos: {e}\033[0m")
