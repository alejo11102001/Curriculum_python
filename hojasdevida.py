people = {}

def main(funcion):
    funcion()
    while True:
        exit_menu = input("\n\033[32m¿Desea continuar o regrear al menu? S(si) - N(no):\033[0m ").lower()
        if exit_menu == "s":
            break  
        elif exit_menu == "n":
            return 
        else:
            print("\033[31mPor favor, ingrese una opción válida (S / N)\033[0m")

def add_curriculum_function(id, name, phone_number, address, email, birthdate, 
                            institution, title, years, 
                            company, job_position, functions, duration, 
                            references_name, relation_references, phone_references, 
                            certifications):
    people[id] = {
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
    print(f"\033[92m\nLa hoja de vida de '{name}' fue agregada correctamente.\033[0m")
