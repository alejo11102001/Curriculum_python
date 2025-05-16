def update_recorded_information(people):
    print("\n--- Actualizar Información Registrada ---")
    doc = input("Ingrese su documento de identidad: ").strip()

    clave, persona = None, None
    for k, p in people.items():
        if k[0] == doc:
            clave, persona = k, p
            break

    if persona is None:
        print("\033[91mNo se encontró ninguna hoja de vida con ese documento.\033[0m")
        return

    print("""
    ¿Qué desea actualizar?
    1. Añadir Experiencia
    2. Añadir Formación
    3. Actualizar Datos Personales
    4. Cambiar Habilidades
    5. Añadir Referencia
    """)

    try:
        opcion = int(input("Ingrese una opción (1-5): "))
    except ValueError:
        print("Opción inválida.")
        return

    if opcion == 1:
        empresa = input("Empresa: ")
        cargo = input("Cargo: ")
        funciones = input("Funciones: ")
        duracion = input("Duración: ")
        persona["experiencia_profesional"].append({
            "empresa": empresa,
            "cargo": cargo,
            "funciones": funciones,
            "duracion": duracion
        })
        print("Experiencia agregada.")

    elif opcion == 2:
        institucion = input("Institución: ")
        titulo = input("Título: ")
        años = input("Años: ")
        persona["formacion_academica"].append({
            "institucion": institucion,
            "titulo": titulo,
            "años": años
        })
        print("Formación agregada.")

    elif opcion == 3:
        persona["datos_personales"]["nombre_completo"] = input("Nuevo nombre: ")
        persona["datos_personales"]["telefono"] = input("Nuevo teléfono: ")
        persona["datos_personales"]["direccion"] = input("Nueva dirección: ")
        persona["datos_personales"]["correo"] = input("Nuevo correo: ")
        print("Datos personales actualizados.")

    elif opcion == 4:
        habilidades = input("Habilidades (separadas por coma): ")
        persona["habilidades_certificaciones"] = [h.strip() for h in habilidades.split(",")]
        print("Habilidades actualizadas.")

    elif opcion == 5:
        nombre = input("Nombre de referencia: ")
        relacion = input("Relación: ")
        telefono = input("Teléfono: ")
        persona["referencias"].append({
            "nombre": nombre,
            "relacion": relacion,
            "telefono": telefono
        })
        print("Referencia agregada.")

    else:
        print("Opción no válida.")
