people = {}

used_emails = set()
global_habilities = set()

def return_to_menu_or_exit():
    while True:
        option_out = input("\033[93m\n¿Deseas volver al menú inicial?: S()si N()no:\033[0m")
        if option_out == "s":
            return False 
        elif option_out == "n":
            print("\033[93m\nSaliendo del sistema...\033[0m")
            exit()
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_function_update():
    while True:
        output_menu = input("\033[93m\n¿Deseas continuar actualizando hojas de vida?: S()si N()no:\033[0m")
        if output_menu == "n":
            return return_to_menu_or_exit() 
        elif output_menu == "s":
            return True 
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")

def advance_function_add():
    while True:
        output_menu = input("\033[93m\n¿Deseas continuar ingresando hojas de vida?: S()si N()no:\033[0m")
        if output_menu == "n":
            return return_to_menu_or_exit() 
        elif output_menu == "s":
            return True 
        else:
            print("\033[91m\nPor favor ingresa 'N' para no o 'S' para sí.\033[0m")


def add_curriculum_function(id, name, phone_number, address, email, birthdate, 
                            institution, title, years, 
                            company, job_position, functions, duration, 
                            references_name, relation_references, phone_references, 
                            certifications):
    clue = (id, birthdate)

    sheet = {
        "datos_personales": {
            "nombre_completo": name,
            "telefono": phone_number,
            "direccion": address,
            "correo": email,
            "fecha_nacimiento": birthdate
        },
        "formacion_academica": [
            {
                "institucion": institution,
                "titulo": title,
                "años": years
            }
        ],
        "experiencia_profesional": [
            {
                "empresa": company,
                "cargo": job_position,
                "funciones": functions,
                "duracion": duration
            }
        ],
        "referencias": [
            {
                "nombre": references_name,
                "relacion": relation_references,
                "telefono": phone_references
            }
        ],
        "habilidades_certificaciones": [skill.strip() for skill in certifications.split(",")]
    }
    people[clue] = sheet
    print(f"\033[92m\nLa hoja de vida de '{name}' fue agregada correctamente.\033[0m")
