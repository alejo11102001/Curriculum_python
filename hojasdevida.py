people: '1010' = {
    "datos_personales": {
        
        "nombre_completo": "Juan Pérez",
        "telefono": "+57 300 1234567",
        "direccion": "Calle 123 #45-67, Medellín, Colombia",
        "correo": "juan.perez@email.com",
        "fecha_nacimiento": "1990-05-15"
    },
    "formacion_academica": [
        {
            "institucion": "Universidad Nacional de Colombia",
            "titulo": "Ingeniero de Sistemas",
            "años": 5
        }
    ],
    "experiencia_profesional": [
        {
            "empresa": "Empresa XYZ S.A.",
            "cargo": "Desarrollador de Software",
            "funciones": "Desarrollo de aplicaciones web con Python y Django",
            "duracion": 3
        }
    ],
    "referencias": [
        {
            "nombre": "María Gómez",
            "relacion": "Exjefa directa",
            "telefono": "+57 310 7654321"
        }
    ],
    "habilidades_certificaciones": [
        "Python",
        "Django",
        "Git",
        "Inglés avanzado"
    ]
}

used_emails = set()
global_habilities = set()

def main(funcion):
    while True:
        funcion()
        while True:
            exit_menu = input("\n\033[32m¿Desea continuar o regrear al menu? S(si) - N(no):\033[0m ").lower()
            if exit_menu == "s":
                break  
            elif exit_menu == "n":
                return 
            else:
                print("\033[31mPor favor, ingrese una opción válida (S / N)\033[0m")
    funcion()

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
