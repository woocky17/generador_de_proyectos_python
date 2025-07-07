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

    # Paso adicional: ¿Crear README.md?
    print("¿Deseas crear un archivo README.md?")
    print("1. Sí")
    print("2. No")
    opcion_readme = input("Elige una opción (1/2): ").strip()
    crear_readme = opcion_readme == '1'

    # Paso adicional: ¿Crear .gitignore?
    print("¿Deseas crear un archivo .gitignore?")
    print("1. Sí")
    print("2. No")
    opcion_gitignore = input("Elige una opción (1/2): ").strip()
    crear_gitignore = opcion_gitignore == '1'

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
    # Devuelve también las opciones elegidas
    return estructura_carpetas, ruta_base, crear_readme, crear_gitignore
