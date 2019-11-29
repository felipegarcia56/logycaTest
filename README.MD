# Prueba desarrollador Python Back-end
## dependencias

 1. Python 3.x
 2. python pip
 3. Django
 4. Postgres
 
## Base de datos Postgresql
Previamente a la configuración y despliegue de la API REST es necesario crear la base de datos en el motor de postgres con el nombre ***Logyca_db***.

## Despliegue servicios rest Django

 1. Ingrese al directorio PG_test 
 2. Instale las dependencias del archivo ***"requirements.txt"*** con el comando ***pip install -r requirements.txt***
 4. Modifique el archivo ***settings.py***, dentro de la ruta ***PG_test/PG_test***, de acuerdo a las credenciales de la base de datos, configuradas en el motor postgres.
 5. Ejecute el comando ***python manage.py makemigrations***
 6. Ejecute el comando ***python manage.py migrate***
 7. ejecute el comando ***python manage.py runserver***


## Nota

 1. La API rest se ejecuta en el puerto 8000
 2. De ser necesario la API permite administrar las django apps con los usarios creados por el django admin.  
 3. En caso de presentar error en la instalación de las dependencia ***psycopg2***, borrarla del archivo requirements.txt instalarla manualmente, para sistemas linux ejecutar el comando ***apt-get install python3-psycopg2*** 
