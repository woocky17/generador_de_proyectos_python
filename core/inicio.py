import os


def inicio():
    nombre_proyecto = input("Introduce el nombre del proyecto: ")
    print("Selecciona la ubicación de la estructura de carpetas:")
    print("1. En una subcarpeta con el nombre del proyecto")
    print("2. En una ruta personalizada")
    opcion = input("Elige una opción (1/2): ").strip()

    if opcion == '1':
        ruta_base = f"../{nombre_proyecto}"
    elif opcion == '2':
        ruta_base = input("Introduce la ruta personalizada: ").strip()
    else:
        print("Opción no válida.")
        return inicio()

    estructura_carpetas = [
        "src",
        os.path.join("src", "api"),
        os.path.join("src", "database"),
        os.path.join("src", "core"),
        os.path.join("src", "utils"),
        os.path.join("src", "models"),
        os.path.join("src", "models", "mapper"),
        "config",
        "data",
    ]
    return estructura_carpetas, ruta_base
