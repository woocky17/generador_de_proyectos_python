from setuptools import setup, find_packages

setup(
    name="new_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "loguru>=0.7.2",
        "sqlalchemy>=2.0.0",
        "pyodbc>=4.0.39"
    ],
    entry_points={
        "console_scripts": [
            "generador-estructura=main:main"
        ]
    },
    author="David Ortet",
    description="Generador de estructura de proyectos Python",
)
