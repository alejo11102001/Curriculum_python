from hojasdevida import *
from consultar_hojas_vida import *
from actualizar_informacion_registrada import *

def add_curriculum():
    print("---- Registro de Datos Personales ----")
    id = input("Ingrese su documento de identidad: ").strip()
    name = input("Ingrese su nombre completo: ").strip()
    phone_number = input("Ingrese su número de contacto: ").strip()
    address = input("Ingrese su dirección: ").strip()
    email = input("Ingrese su correo: ").strip()
    birthdate = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ").strip()

    if email in used_emails:
        print("\033[91mEste correo ya está registrado.\033[0m")
        return
    used_emails.add(email)

    print("\n---- Registro Formación Académica ----")
    institution = input("Ingrese la institución a la que asistió: ").strip()
    title = input("Ingrese título logrado: ").strip()
    years = int(input("Ingrese los años que duró el proceso: "))

    print("\n---- Registro Experiencia Profesional ----")
    company = input("Ingrese el nombre de la empresa: ").strip()
    job_position = input("Ingrese cargo asignado: ").strip()
    functions = input("Ingrese las funciones que realizaba: ").strip()
    duration = int(input("Ingrese la duración en años: "))

    print("\n---- Registro Referencias Personales ----")
    references_name = input("Ingrese nombre de la referencia: ").strip()
    relation_references = input("Ingrese la relación con la referencia: ").strip()
    phone_references = input("Ingrese teléfono de la referencia: ").strip()

    print("\n---- Registro Habilidades o Certificaciones Adicionales ----")
    certifications = input("Ingrese sus habilidades o certificados (separados por comas): ").strip()

    for h in certifications.split(","):
        global_habilities.add(h.strip())

    add_curriculum_function(
        id, name, phone_number, address, email, birthdate,
        institution, title, years,
        company, job_position, functions, duration,
        references_name, relation_references, phone_references,
        certifications)

while True:

    print("""
        --------- Menu ----------
        1. Registrar hoja de vida.
        2. Consultar hoja de vida.
        3. Actualizar informacion registrada.
        4. Generar reportes.
        5. SALIR
        """)

    while True:
        try:
            opcion = int(input("Ingrese una OPCION: "))
            if opcion < 1 or opcion > 5:
                print("\n\033[93mIngrese una OPCION valida (1 - 5)\n\033[0m")
                continue
            break
        except ValueError:
            print("\n\033[93mValor invaido.\n\033[0m")

    match opcion:
        case 1:
            while True:
                add_curriculum()
                if not advance_function_add():
                    break
        case 2:
            while True:
                searchMain()
                if not advance_function_add():
                    break
        case 3:
            while True:
                update_recorded_information()
                if not advance_function_update():
                    break
        case 4:
            print("hola")
        case 5:
            print("👋 Saliste del Sistema... ¡Hasta luego!")
