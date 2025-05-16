def add_experience():
    print("\n--- Añadir Experiencia ---")
    experiencia = input("Ingrese su experiencia laboral (empresa, cargo, tiempo): ")
    print(f"Experiencia registrada: {experiencia}")


def add_education():
    print("\n--- Añadir Formación ---")
    formacion = input("Ingrese su formación académica (institución, título, año): ")
    print(f"Formación registrada: {formacion}")


def update_personal_info():
    print("\n--- Actualizar Datos Personales ---")
    nombre = input("Nuevo nombre completo: ")
    telefono = input("Nuevo número de teléfono: ")
    correo = input("Nuevo correo electrónico: ")
    print(f"Datos personales actualizados:\nNombre: {nombre}\nTeléfono: {telefono}\nCorreo: {correo}")


def update_skills():
    print("\n--- Agregar o Cambiar Habilidades ---")
    habilidades = input("Ingrese sus habilidades separadas por coma (ej: Python, Trabajo en equipo): ")
    lista_habilidades = [h.strip() for h in habilidades.split(',')]
    print("Habilidades registradas:")
    for habilidad in lista_habilidades:
        print(f"- {habilidad}")


def update_references():
    print("\n--- Agregar o Cambiar Referencias ---")
    referencia = input("Ingrese el nombre y contacto de su referencia: ")
    print(f"Referencia registrada: {referencia}")


def update_recorded_information():
    print("\n------ Actualizar información registrada ------\n")
    print("""
    1. Añadir Experiencia
    2. Añadir Formación
    3. Actualizar Datos Personales
    4. Agregar o Cambiar Habilidades
    5. Agregar o Cambiar Referencias
    """)

while True:
        try:
            opcion = int(input("Ingrese una OPCIÓN: "))
            if opcion < 1 or opcion > 5:
                print("\n\033[93mIngrese una OPCIÓN válida (1 - 5)\n\033[0m")
                continue
            break
        except ValueError:
            print("\n\033[93mValor inválido. Ingrese un número.\n\033[0m")

match opcion:
    case 1:
        add_experience()
    case 2:
        add_education()
    case 3:
        update_personal_info()
    case 4:
        update_skills()
    case 5:
        update_references()
