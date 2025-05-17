# VitaeConsole

## Integrantes del Equipo

    - Jerónimo Cardona Restrepo - Van Rossum
    - Tomas Loiza - Ritchie
    - Diego Zuluaga - Van Rossum

**Grupo:** Equipo Pitón 🐍

---

## Descripción General

**VitaeConsole** 
    Es un sistema desarrollado en Python que permite la gestión integral de hojas de vida desde la consola. El sistema facilita el registro, búsqueda, actualización, generación de reportes y exportación de información personal, académica y profesional de candidatos, almacenando los datos en formato JSON y permitiendo la exportación a CSV para análisis externo.

---

## Instrucciones para Ejecutar el Programa

    1. Clona o descarga el repositorio a tu máquina local.
    2. Asegúrate de tener Python 3.7 o superior instalado.
    3. Instala la librería necesaria con el siguiente comando:
    ```bash
    
    pip install tabulate

python main.py

## Liberias
    - json (incluida en Python)
    - csv (incluida en Python)
    - os (incluida en Python)
    - re (incluida en Python)
    - tabulate (instalable con pip install tabulate)

# Ejemplos de Uso

## Registro de una Hoja de Vida
    Al seleccionar la opción 1 en el menú, el sistema solicitará ingresar datos como nombre, documento, contacto, formación académica, experiencia profesional, referencias y habilidades separadas por comas.

## Ejemplo de entrada:

    - Nombre completo: Juan Pérez
    - Documento: 12345678
    - Número de contacto: 3001234567
    - Dirección: Calle Falsa 123
    - Correo electrónico: juan.perez@mail.com
    - Fecha de nacimiento (AAAA-MM-DD): 1990-05-20

## Agregar formación académica:
    - Institución: Universidad Nacional
    - Título: Ingeniero de Sistemas
    - Años: 5

    ¿Agregar otra formación? (s/n): n

## Agregar experiencia profesional:
    - Empresa: Tech Solutions
    - Cargo: Desarrollador
    - Funciones: Desarrollo de software
    - Duración: 3 años

    ¿Agregar otra experiencia? (s/n): n

## Agregar referencia:
    - Nombre: María Gómez
    - Relación: Exjefa
    - Teléfono: 3109876543

    ¿Agregar otra referencia? (s/n): n

    - Ingrese habilidades separadas por coma: 

    Python, SQL, Trabajo en equipo
