# Desafio de CRUD

## Instalacion

1. Clona el repositorio en tu maquina local
```bash
$ git clone https://github.com/DaironRV/Django_Prueba_Tecnica.git
```

2. Navega en el directorio del proyecto 
```bash
$ cd Django_Prueba_Tecnica
```

3. Puedes cambiar el origen del proyecto con los siguientes comando

```bash
$ git remote -v
$ git remote remove origin
$ git remote add origin <nueva_url_del_repositorio>
```

4. Instalar venv (O el entorno de preferencia)
- Windows:
```bash
- $ python -m venv venv
```
- Linux/Mac
```bash
- $ python3 -m venv venv
```


5 Instalar las dependecias necesarias
- Recuerda tener el requirements.txt para poder instalar las dependencias en tu maquina local y activar el entorno de preferencia o en este caso "Venv"

- Windows
```bash
$ source venv/Scripts/activate
```

- Linux/Mac
```bash
$ source venv/bin/activate
```
Y por ultimo instalar las dependencias

```bash
$ pip install -r requirements.txt
```

## Uso

1. Inicia la aplicación: Recuerda siempre activar el entorno virtual

- Windows:

```bash
- $ py manage.py runserver 
```

- Linux/Mac:

```bash
- $ python3 manage.py runserver
```

2. Accede a la documentación de la API en tu navegador:

http://localhost:8000/admin


