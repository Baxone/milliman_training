1 - Siempre crear un entorno de desarrollo dentro de la carpeta de cada ejercicio
        - python -m venv .venv
2 - Activar el entorno de desarollo 
        - source .venv/Scripts/activate
3 - Cuando terminemos desactivar el entorno de desarollo
        - deactivate
4 - Crear el fichero requirements.txt - con el listado de dependencias del proyecto
        - pip freeze > requirements.txt 
5 - Para instalar todo lo que hay en el requirements.txt ejecuto el siguiente comando. OJO entorno de desarrollo creado y activado.
        - pip install -r requirements.txt