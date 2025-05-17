# Archivo principal del sistema VitaeConsole

from hojasdevida import registrar_hoja_de_vida, buscar_hoja_de_vida, actualizar_hoja_de_vida
from reportes import generar_reporte, exportar_datos
import os
import sys

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        try:
            print("\n=== VitaeConsole ===")
            print("1. Registrar hoja de vida")
            print("2. Buscar hoja de vida")
            print("3. Actualizar hoja de vida")
            print("4. Generar reporte")
            print("5. Exportar datos")
            print("6. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                limpiar_pantalla()
                registrar_hoja_de_vida()
            elif opcion == "2":
                limpiar_pantalla()
                buscar_hoja_de_vida()
            elif opcion == "3":
                limpiar_pantalla()
                actualizar_hoja_de_vida()
            elif opcion == "4":
                limpiar_pantalla()
                generar_reporte()
            elif opcion == "5":
                limpiar_pantalla()
                exportar_datos()
            elif opcion == "6":
                print("Saliendo del sistema...")
                break
            else:
                print("❌ Opción inválida. Intente nuevamente.")
        except KeyboardInterrupt:
            print("\n\n🚫 Interrupción detectada. Saliendo del sistema.")
            sys.exit()
        except Exception as e:
            print(f"\n⚠️ Error inesperado: {e}")

if __name__ == "__main__":
    limpiar_pantalla()
    menu()
