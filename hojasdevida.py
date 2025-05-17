import json
import os
from datetime import datetime
from tabulate import tabulate

RUTA = "datos.json"

RAINBOW_COLORS = ["\033[91m", "\033[93m", "\033[92m", "\033[96m", "\033[94m", "\033[95m"]
RESET_COLOR = "\033[0m"

def print_rainbow(text):
    colored_text = ""
    for i, char in enumerate(text):
        colored_text += RAINBOW_COLORS[i % len(RAINBOW_COLORS)] + char
    colored_text += RESET_COLOR
    print(colored_text)

def cargar_datos():
    if not os.path.exists(RUTA):
        return []
    with open(RUTA, "r") as f:
        return json.load(f)

def guardar_datos(datos):
    with open(RUTA, "w") as f:
        json.dump(datos, f, indent=4)

def registrar_hoja_de_vida():
    datos = cargar_datos()
    nueva = {}

    print("\n--- Registro de Hoja de Vida ---")
    campos = [
        ("nombre", "Nombre completo"),
        ("documento", "Documento"),
        ("contacto", "Número de contacto"),
        ("direccion", "Dirección")
    ]

    for key, mensaje in campos:
        while True:
            valor = input(f"{mensaje}: ").strip()
            if valor:
                nueva[key] = valor
                break
            print_rainbow(f"{mensaje} no puede estar vacío.")

    while True:
        correo = input("Correo electrónico: ").strip()
        if correo and "@" in correo and "." in correo:
            nueva["correo"] = correo
            break
        print_rainbow("Correo inválido. Intente nuevamente.")

    while True:
        fecha = input("Fecha de nacimiento (AAAA-MM-DD): ").strip()
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            nueva["fecha_nacimiento"] = fecha
            break
        except ValueError:
            print_rainbow("Formato de fecha incorrecto. Use AAAA-MM-DD.")

    nueva["formacion"] = []
    while True:
        print("Agregar formación académica:")
        institucion = input("  Institución: ").strip()
        titulo = input("  Título: ").strip()
        años = input("  Años: ").strip()

        if institucion and titulo and años.isdigit():
            nueva["formacion"].append({
                "institucion": institucion,
                "titulo": titulo,
                "años": años
            })
        else:
            print_rainbow("Datos inválidos en formación académica.")
            continue

        if input("¿Agregar otra formación? (s/n): ").lower() != "s":
            break

    nueva["experiencia"] = []
    while True:
        print("Agregar experiencia profesional:")
        empresa = input("  Empresa: ").strip()
        cargo = input("  Cargo: ").strip()
        funciones = input("  Funciones: ").strip()
        duracion = input("  Duración: ").strip()

        if empresa and cargo and funciones and duracion:
            nueva["experiencia"].append({
                "empresa": empresa,
                "cargo": cargo,
                "funciones": funciones,
                "duracion": duracion
            })
        else:
            print_rainbow("Datos inválidos en experiencia profesional.")
            continue

        if input("¿Agregar otra experiencia? (s/n): ").lower() != "s":
            break

    nueva["referencias"] = []
    while True:
        print("Agregar referencia:")
        nombre_ref = input("  Nombre: ").strip()
        relacion = input("  Relación: ").strip()
        telefono = input("  Teléfono: ").strip()

        if nombre_ref and relacion and telefono:
            nueva["referencias"].append({
                "nombre": nombre_ref,
                "relacion": relacion,
                "telefono": telefono
            })
        else:
            print_rainbow("Datos inválidos en referencia.")
            continue

        if input("¿Agregar otra referencia? (s/n): ").lower() != "s":
            break

    habilidades = input("Ingrese habilidades separadas por coma: ").strip()
    nueva["habilidades"] = [h.strip() for h in habilidades.split(",") if h.strip()]

    datos.append(nueva)
    guardar_datos(datos)
    print_rainbow("Hoja de vida registrada correctamente.")

def buscar_hoja_de_vida():
    datos = cargar_datos()

    print("\n¿Buscar por qué criterio?")
    print("1. Nombre\n2. Documento\n3. Correo\n4. Años de experiencia\n5. Formación\n6. Habilidades")

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
            print(tabulate([[k, json.dumps(v, ensure_ascii=False)] for k, v in e.items()], headers=["Campo", "Valor"]))
    else:
        print_rainbow("No se encontraron resultados.")

def actualizar_hoja_de_vida():
    datos = cargar_datos()
    documento = input("Ingrese el documento de la persona a actualizar: ").strip()

    for d in datos:
        if d["documento"] == documento:
            print("Datos actuales:")
            tabla = [[k, json.dumps(v, ensure_ascii=False)] for k, v in d.items()]
            print(tabulate(tabla, headers=["Campo", "Valor"], tablefmt="grid"))

            # Actualizar contacto, dirección y correo
            contacto = input("Nuevo contacto (Enter para mantener actual): ").strip()
            if contacto:
                d["contacto"] = contacto

            direccion = input("Nueva dirección (Enter para mantener actual): ").strip()
            if direccion:
                d["direccion"] = direccion

            correo = input("Nuevo correo (Enter para mantener actual): ").strip()
            if correo:
                d["correo"] = correo

            # Agregar nuevas experiencias
            while True:
                agregar_exp = input("¿Desea agregar experiencia profesional? (s/n): ").lower()
                if agregar_exp == "s":
                    empresa = input("  Empresa: ").strip()
                    cargo = input("  Cargo: ").strip()
                    funciones = input("  Funciones: ").strip()
                    duracion = input("  Duración: ").strip()

                    if empresa and cargo and funciones and duracion:
                        exp = {
                            "empresa": empresa,
                            "cargo": cargo,
                            "funciones": funciones,
                            "duracion": duracion
                        }
                        d.setdefault("experiencia", []).append(exp)
                        print_rainbow("Experiencia agregada.")
                    else:
                        print_rainbow("Datos inválidos en experiencia, inténtelo de nuevo.")
                elif agregar_exp == "n":
                    break
                else:
                    print_rainbow("Opción no válida. Por favor ingrese 's' o 'n'.")

            # Agregar nuevas formaciones
            while True:
                agregar_form = input("¿Desea agregar formación académica? (s/n): ").lower()
                if agregar_form == "s":
                    institucion = input("  Institución: ").strip()
                    titulo = input("  Título: ").strip()
                    años = input("  Años: ").strip()

                    if institucion and titulo and años.isdigit():
                        formacion = {
                            "institucion": institucion,
                            "titulo": titulo,
                            "años": años
                        }
                        d.setdefault("formacion", []).append(formacion)
                        print_rainbow("Formación agregada.")
                    else:
                        print_rainbow("Datos inválidos en formación académica, inténtelo de nuevo.")
                elif agregar_form == "n":
                    break
                else:
                    print_rainbow("Opción no válida. Por favor ingrese 's' o 'n'.")

            # Actualizar habilidades
            habilidades = input("Ingrese habilidades separadas por coma (Enter para mantener actuales): ").strip()
            if habilidades:
                d["habilidades"] = [h.strip() for h in habilidades.split(",") if h.strip()]
                print_rainbow("Habilidades actualizadas.")

            # Agregar nuevas referencias
            while True:
                agregar_ref = input("¿Desea agregar una referencia? (s/n): ").lower()
                if agregar_ref == "s":
                    nombre_ref = input("  Nombre: ").strip()
                    relacion = input("  Relación: ").strip()
                    telefono = input("  Teléfono: ").strip()

                    if nombre_ref and relacion and telefono:
                        ref = {
                            "nombre": nombre_ref,
                            "relacion": relacion,
                            "telefono": telefono
                        }
                        d.setdefault("referencias", []).append(ref)
                        print_rainbow("Referencia agregada.")
                    else:
                        print_rainbow("Datos inválidos en referencia, inténtelo de nuevo.")
                elif agregar_ref == "n":
                    break
                else:
                    print_rainbow("Opción no válida. Por favor ingrese 's' o 'n'.")

            guardar_datos(datos)
            print_rainbow("Información actualizada correctamente.")
            return

    print_rainbow("No se encontró hoja de vida con ese documento.")
