import os
from utils.crear_conection_db import crear_conection_db
from utils.crear_main_py import crear_main_py
from utils.crear_readme import crear_readme
from utils.crear_gitignore import crear_gitignore
from utils.crear_requirements import crear_requirements
from utils.crear_env import crear_env
from utils.crear_constantes import crear_constantes


def estructura(estructura, ruta_base="./", crear_readme=True, crear_gitignore=True):
    vs_code_opened = False
    for ruta in estructura:
        if os.path.isabs(ruta_base):
            ruta_completa = os.path.join(ruta_base, ruta)
        else:
            ruta_completa = os.path.join(ruta_base, ruta)
        try:
            os.makedirs(ruta_completa)
            print(f"Carpeta creada: {ruta_completa}")
            init_path = os.path.join(ruta_completa, "__init__.py")
            if not os.path.exists(init_path):
                with open(init_path, "w", encoding="utf-8") as f:
                    f.write("")
            if not vs_code_opened:
                abs_root = os.path.abspath(ruta_base)
                os.system(f'code "{abs_root}"')
                vs_code_opened = True
        except OSError as e:
            print(f"Error al crear {ruta_completa}: {e}")
    crear_main_py(ruta_base)
    if crear_readme:
        crear_readme_fn = globals().get('crear_readme', crear_readme)
        crear_readme_fn(ruta_base)
    if crear_gitignore:
        crear_gitignore_fn = globals().get('crear_gitignore', crear_gitignore)
        crear_gitignore_fn(ruta_base)
    crear_requirements(ruta_base)
    crear_env(ruta_base)
    crear_constantes(ruta_base)
    crear_conection_db(ruta_base)
