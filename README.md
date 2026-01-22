# 👨‍💻 Cookbook.py: Manual de Sabores

¡Bienvenido a Cookbook.py! Este no es solo un recetario, es una aplicación web interactiva diseñada con la mentalidad de un desarrollador. Aquí, la gastronomía se encuentra con la ingeniería para ofrecer una experiencia de usuario fluida, robusta y eficiente.

Originalmente enfocado en sabores venezolanos, este manual está diseñado para ser escalable y permitir la integración de platos de cualquier rincón del mundo.

---

## 🛠️ Requisitos del Sistema

Antes de comenzar, asegúrate de tener instalado:
* Python 3.10 o superior (Descárgalo en python.org).
* Terminal (Bash, CMD o PowerShell).

---

## 🚀 Guía de Instalación y Ejecución Paso a Paso

Sigue estos pasos en tu terminal para configurar el proyecto desde cero:

### 1. Preparar la carpeta del proyecto
Ejecuta estos comandos para crear tu espacio de trabajo:
$ mkdir cookbook-py
$ cd cookbook-py

### 2. Instalar dependencias
Solo necesitamos Streamlit, ya que SQLite viene integrado en Python:
$ pip install streamlit

### 3. Crear el archivo del código
1. Crea un archivo nuevo en tu editor (VS Code) llamado: recetario_web.py
2. Pega el código de la aplicación (el que incluye la función inicializar_db_si_no_existe).
3. Guarda el archivo dentro de la carpeta que creaste.

### 4. Lanzar la aplicación
Ejecuta el servidor local con el siguiente comando:
$ streamlit run recetario_web.py

> 💡 Nota de Robustez: Al ejecutarlo por primera vez, el programa detectará automáticamente que no existe el archivo de base de datos y creará el archivo "recetas_venezuela.db" con los platos iniciales por ti.

---

## 📂 Estructura del Proyecto

Una vez que la aplicación esté funcionando, tu carpeta se verá así:
* recetario_web.py: Código principal, interfaz y lógica de creación de datos.
* recetas_venezuela.db: Base de datos generada automáticamente.
* .gitignore: Archivo para evitar subir datos temporales a GitHub.

---

## ✍️ Cómo contribuir o editar recetas

Este proyecto es totalmente flexible para ediciones:

1. Vía DB Browser (Recomendado): Abre recetas_venezuela.db con el programa, edita la tabla "platos" (puedes añadir platos internacionales como Ensalada César o Pasta), haz clic en el botón "Escribir cambios" (Write Changes) y refresca tu navegador.
2. Vía Código: Si deseas cambiar los datos que aparecen por defecto, edita la lista "repertorio_inicial" dentro del código, borra el archivo .db y vuelve a iniciar la aplicación.

---

## 🧠 Aprendizajes de Desarrollo (Nivel Jr)
* Persistencia Local: Aprendizaje sobre el uso de SQLite para guardar datos de forma permanente.
* UI Reactiva: Creación de filtros dinámicos que reaccionan a cada letra escrita por el usuario sin recargar la página.
* Arquitectura Robusta: El software es capaz de autogestionar su entorno (crear su propia base de datos) si los archivos faltan.

---
Desarrollado por: Arin Romero