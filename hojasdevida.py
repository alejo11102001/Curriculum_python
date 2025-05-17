import json
import os
from datetime import datetime

RUTA = "datos.json"

# Lista de códigos de colores ANSI para arcoíris
RAINBOW_COLORS = [
    "\033[91m",  # Rojo
    "\033[93m",  # Amarillo
    "\033[92m",  # Verde
    "\033[96m",  # Cyan claro
    "\033[94m",  # Azul
    "\033[95m"   # Magenta
]

RESET_COLOR = "\033[0m"

def print_rainbow(text):
    colored_text = ""
    color_count = len(RAINBOW_COLORS)
    for i, char in enumerate(text):
        color = RAINBOW_COLORS[i % color_count]
        colored_text += f"{color}{char}"
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

    # Validar que no quede vacío
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre:
            nueva["nombre"] = nombre
            break
        print_rainbow("El nombre no puede estar vacío. Intente nuevamente.")

    while True:
        documento = input("Documento: ").strip()
        if documento:
            nueva["documento"] = documento
            break
        print_rainbow("El documento no puede estar vacío. Intente nuevamente.")

    while True:
        contacto = input("Número de contacto: ").strip()
        if contacto:
            nueva["contacto"] = contacto
            break
        print_rainbow("El contacto no puede estar vacío. Intente nuevamente.")

    while True:
        direccion = input("Dirección: ").strip()
        if direccion:
            nueva["direccion"] = direccion
            break
        print_rainbow("La dirección no puede estar vacía. Intente nuevamente.")

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
            formacion = {
                "institucion": institucion,
                "titulo": titulo,
                "años": años
            }
            nueva["formacion"].append(formacion)
        else:
            print_rainbow("Datos inválidos en formación académica, inténtelo de nuevo.")
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
            exp = {
                "empresa": empresa,
                "cargo": cargo,
                "funciones": funciones,
                "duracion": duracion
            }
            nueva["experiencia"].append(exp)
        else:
            print_rainbow("Datos inválidos en experiencia profesional, inténtelo de nuevo.")
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
            ref = {
                "nombre": nombre_ref,
                "relacion": relacion,
                "telefono": telefono
            }
            nueva["referencias"].append(ref)
        else:
            print_rainbow("Datos inválidos en referencia, inténtelo de nuevo.")
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
    criterio = input("Buscar por nombre, documento o correo: ").lower()
    encontrados = []

    for d in datos:
        if criterio in d["nombre"].lower() or criterio in d["documento"].lower() or criterio in d["correo"].lower():
            encontrados.append(d)

    if encontrados:
        for e in encontrados:
            print(json.dumps(e, indent=4, ensure_ascii=False))
    else:
        print_rainbow("No se encontraron resultados.")

def actualizar_hoja_de_vida():
    datos = cargar_datos()
    documento = input("Ingrese el documento de la persona a actualizar: ").strip()

    for d in datos:
        if d["documento"] == documento:
            print("Datos actuales:")
            print(json.dumps(d, indent=4, ensure_ascii=False))
            contacto = input("Nuevo contacto (enter para no cambiar): ").strip()
            direccion = input("Nueva dirección (enter para no cambiar): ").strip()
            correo = input("Nuevo correo (enter para no cambiar): ").strip()

            if contacto:
                d["contacto"] = contacto
            if direccion:
                d["direccion"] = direccion
            if correo:
                if "@" in correo and "." in correo:
                    d["correo"] = correo
                else:
                    print_rainbow("Correo inválido, no se actualizó ese campo.")

            guardar_datos(datos)
            print_rainbow("Información actualizada correctamente.")
            return

    print_rainbow("No se encontró hoja de vida con ese documento.")
