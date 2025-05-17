# Archivo principal del sistema VitaeConsole

# Importamos los módulos necesarios
from hojasdevida import registrar_hoja_de_vida, buscar_hoja_de_vida, actualizar_hoja_de_vida
from reportes import generar_reporte, exportar_datos
import os

def menu():
    while True:
        print("\n=== VitaeConsole ===")
        print("1. Registrar hoja de vida")
        print("2. Buscar hoja de vida")
        print("3. Actualizar hoja de vida")
        print("4. Generar reporte")
        print("5. Exportar datos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if not opcion.isdigit():
            print("\033[91m\nError: Por favor ingrese un número válido.\033[0m")  # Rojo
            continue

        opcion_num = int(opcion)
        
        if opcion_num == 1:
            registrar_hoja_de_vida()
        elif opcion_num == 2:
            buscar_hoja_de_vida()
        elif opcion_num == 3:
            actualizar_hoja_de_vida()
        elif opcion_num == 4:
            generar_reporte()
        elif opcion_num == 5:
            exportar_datos()
        elif opcion_num == 6:
            print("\033[92mSaliendo del sistema...\033[0m")  # Verde
            break
        else:
            print("\033[91mOpción inválida. Intente nuevamente.\033[0m")  # Rojo

if __name__ == "__main__":
    menu()
