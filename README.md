# Desafío de CRUD

## Hola reclutador/a

Es un gusto poderte presentar mi proyecto hecho con mucho cariño y esfuerzo. ¡Espero te guste!

## Funcionalidad en el despliegue

### Capturas de la aplicación web

!Página inicial
![](https://github.com/DaironRV/Django_Prueba_Tecnica/blob/main/Page%20init.png)

1. Coloca un título descriptivo.
2. Llena los datos de las transacciones hechas (tanto el presupuesto que tienes como el dinero que quieres gastar).
3. Asegúrate de colocar la fecha.
4. Simplemente presiona el botón **Save**.
5. ¡Ya tienes la transacción registrada!

---

!Página de edición
![](https://github.com/DaironRV/Django_Prueba_Tecnica/blob/main/Page%20edit.png)

1. Coloca un título descriptivo.
2. Llena los datos de las transacciones hechas (tanto el presupuesto que tienes como el dinero que quieres gastar).
3. Asegúrate de colocar la fecha.
4. Simplemente presiona el botón **Save**.
5. ¡Ya tienes la transacción editada!

## Diseño web

A continuación, te comparto el diseño completo y los recursos que he utilizado en Figma.

!Diseño en Figma

> ¡Espero te guste!

## Instalación

1. Clona el repositorio en tu máquina local:
    ```bash
    git clone https://github.com/DaironRV/Django_Prueba_Tecnica.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd Django_Prueba_Tecnica
    ```

3. Cambia el origen del proyecto con los siguientes comandos:
    ```bash
    git remote -v
    git remote remove origin
    git remote add origin <nueva_url_del_repositorio>
    ```

4. Instala `venv` (o el entorno de tu preferencia):
    - **Windows**:
        ```bash
        python -m venv venv
        ```
    - **Linux/Mac**:
        ```bash
        python3 -m venv venv
        ```

5. Instala las dependencias necesarias:
    - Recuerda tener el `requirements.txt` para poder instalar las dependencias en tu máquina local y activar el entorno de preferencia (en este caso, "venv").

    - **Windows**:
        ```bash
        source venv/Scripts/activate
        ```
    - **Linux/Mac**:
        ```bash
        source venv/bin/activate
        ```

    - Finalmente, instala las dependencias:
        ```bash
        pip install -r requirements.txt
        ```

## Uso

1. Inicia la aplicación (recuerda siempre activar el entorno virtual):
    - **Windows**:
        ```bash
        py manage.py runserver
        ```
    - **Linux/Mac**:
        ```bash
        python3.manage.py runserver
        ```

2. Accede a la documentación de la API en tu navegador:
    http://localhost:8000/tasks
