# Módulo de gestión de hojas de vida

import json
import os

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

from tabulate import tabulate
import json

def buscar_hoja_de_vida():
    datos = cargar_datos()
    
    print("\n¿Buscar por qué criterio?")
    print("1. Nombre")
    print("2. Documento")
    print("3. Correo")
    print("4. Años de experiencia")
    print("5. Formación")
    print("6. Habilidades")

    opcion = input("Seleccione una opción (1-6): ")
    criterio = input("Ingrese el valor de búsqueda: ").lower()
    encontrados = []

    for d in datos:
        if opcion == "1" and criterio in d["nombre"].lower():
            encontrados.append(d)
        elif opcion == "2" and criterio in d["documento"]:
            encontrados.append(d)
        elif opcion == "3" and criterio in d["correo"].lower():
            encontrados.append(d)
        elif opcion == "4":
            for exp in d.get("experiencia", []):
                if criterio in exp.get("duracion", "").lower():
                    encontrados.append(d)
                    break
        elif opcion == "5":
            for f in d.get("formacion", []):
                if criterio in f.get("titulo", "").lower():
                    encontrados.append(d)
                    break
        elif opcion == "6":
            for h in d.get("habilidades", []):
                if criterio in h.lower():
                    encontrados.append(d)
                    break

    if encontrados:
        for e in encontrados:
            print("\n==============================")
            print(f" Hoja de vida de: {e['nombre']}")
            print("==============================")

            # Datos personales
            personales = [[
                e.get("nombre", ""),
                e.get("documento", ""),
                e.get("contacto", ""),
                e.get("direccion", ""),
                e.get("correo", ""),
                e.get("fecha_nacimiento", "")
            ]]
            print("\n Datos Personales:")
            print(tabulate(personales, headers=["Nombre", "Documento", "Contacto", "Dirección", "Correo", "Fecha Nac."]))

            # Formación
            formacion = []
            for f in e.get("formacion", []):
                formacion.append([f.get("institucion", ""), f.get("titulo", ""), f.get("años", "")])
            print("\n Formación:")
            print(tabulate(formacion, headers=["Institución", "Título", "Años"]))

            # Experiencia
            experiencia = []
            for ex in e.get("experiencia", []):
                experiencia.append([ex.get("empresa", ""), ex.get("cargo", ""), ex.get("funciones", ""), ex.get("duracion", "")])
            print("\n Experiencia:")
            print(tabulate(experiencia, headers=["Empresa", "Cargo", "Funciones", "Duración"]))

            # Referencias
            referencias = []
            for r in e.get("referencias", []):
                referencias.append([r.get("nombre", ""), r.get("relacion", ""), r.get("telefono", "")])
            print("\n Referencias:")
            print(tabulate(referencias, headers=["Nombre", "Relación", "Teléfono"]))

            # Habilidades
            habilidades = [[", ".join(e.get("habilidades", []))]]
            print("\n Habilidades:")
            print(tabulate(habilidades, headers=["Habilidades"]))
    else:
        print("No se encontraron resultados.")

def actualizar_hoja_de_vida():
    datos = cargar_datos()
    documento = input("Ingrese el documento de la persona a actualizar: ")

    for d in datos:
        if d["documento"] == documento:
            print("Datos actuales:")
            print("\n📌 Datos personales:")
            personales = [[
                d.get("nombre", ""),
                d.get("documento", ""),
                d.get("contacto", ""),
                d.get("direccion", ""),
                d.get("correo", ""),
                d.get("fecha_nacimiento", "")
            ]]
            print(tabulate(personales, headers=["Nombre", "Documento", "Contacto", "Dirección", "Correo", "Fecha Nac."]))

            print("\n🎓 Formación:")
            formacion = [[f["institucion"], f["titulo"], f["años"]] for f in d.get("formacion", [])]
            print(tabulate(formacion, headers=["Institución", "Título", "Años"]))

            print("\n💼 Experiencia:")
            experiencia = [[e["empresa"], e["cargo"], e["funciones"], e["duracion"]] for e in d.get("experiencia", [])]
            print(tabulate(experiencia, headers=["Empresa", "Cargo", "Funciones", "Duración"]))

            print("\n📞 Referencias:")
            referencias = [[r["nombre"], r["relacion"], r["telefono"]] for r in d.get("referencias", [])]
            print(tabulate(referencias, headers=["Nombre", "Relación", "Teléfono"]))

            print("\n🛠️ Habilidades:")
            print(", ".join(d.get("habilidades", [])))

            # Actualizar campos básicos
            d["contacto"] = input("Nuevo contacto: ")
            d["direccion"] = input("Nueva dirección: ")
            d["correo"] = input("Nuevo correo: ")

            # Añadir nueva experiencia
            if input("¿Desea agregar una nueva experiencia? (s/n): ").lower() == "s":
                nueva_exp = {
                    "empresa": input("Empresa: "),
                    "cargo": input("Cargo: "),
                    "funciones": input("Funciones: "),
                    "duracion": input("Duración (meses o años): ")
                }
                d.setdefault("experiencia", []).append(nueva_exp)

            # Añadir nueva formación
            if input("¿Desea agregar una nueva formación? (s/n): ").lower() == "s":
                nueva_form = {
                    "institucion": input("Institución: "),
                    "titulo": input("Título obtenido: "),
                    "años": input("Años de formación: ")
                }
                d.setdefault("formacion", []).append(nueva_form)

            # Cambiar o agregar habilidades
            if input("¿Desea modificar las habilidades? (s/n): ").lower() == "s":
                habilidades = input("Ingrese las habilidades separadas por coma: ")
                d["habilidades"] = [h.strip() for h in habilidades.split(",")]

            # Cambiar o agregar referencias
            if input("¿Desea modificar las referencias? (s/n): ").lower() == "s":
                nuevas_ref = []
                while True:
                    nombre = input("Nombre de referencia: ")
                    relacion = input("Relación: ")
                    telefono = input("Teléfono: ")
                    nuevas_ref.append({
                        "nombre": nombre,
                        "relacion": relacion,
                        "telefono": telefono
                    })
                    if input("¿Agregar otra referencia? (s/n): ").lower() != "s":
                        break
                d["referencias"] = nuevas_ref

            guardar_datos(datos)
            print("Información actualizada correctamente.")
            return

    print("No se encontró hoja de vida con ese documento.")