import api
import base_datos
import os
os.system("cls")
base_datos.iniciar_db()

def menu():
    while True:
        print("===== Menu Principal =========")
        print("1- Consultar Clima")
        print("2- Ver Historial")
        print("3- Exportar Historial a CSV")
        print("4- Salir")
        print("="*30)
        opciones = input("Ingrese la opcion que necesite: ")

        match opciones:
            case "1":
                os.system("cls")
                print("===== Consultar Clima ========")
                ciudad = input("Ingrese una ciudad: ")
                clima = api.consultar_clima(ciudad)
                
                if clima:
                    print(f"\nCiudad: {clima['ciudad']}")
                    print(f"Temperatura: {clima['temperatura']}°C")
                    print(f"Clima: {clima['descripcion']}\n")

                    base_datos.guardar_consulta(
                        clima["ciudad"],
                        clima["temperatura"],
                        clima["descripcion"]
                    )
                else:
                    print("Error al consultar el clima")
                print("="*30)
                input("\nPresione Enter para continuar....")
                os.system("cls")

            case "2":
                os.system("cls")
                print("===== Ver Historia ========")
                historial = base_datos.ver_historial()
                if historial:
                    for fila in historial:
                        print(f"ID: {fila[0]} | Ciudad: {fila[1]} | Temp: {fila[2]}°C | Clima: {fila[3]} | Fecha: {fila[4]}")
                else:
                    print("No hay datos guardados")
                print("\n")
                print("="*27)
                input("\nPresione Enter para continuar....")
                os.system("cls")

            case "3":
                os.system("cls")
                print("===== Exportar Archivo =======")
                base_datos.exportar_historial()
                print("Historial exportado a CSV correctamente\n")
                print("="*30)
                input("\nPresione Enter para continuar....")
                os.system("cls")
            case "4":
                print("Hasta Luego!!")
                break
            case _:
                print("Opcion Invalida")
                input("Presione Enter...")

menu()