import streamlit as st
import sqlite3
import os


DB_NAME = "cookbook.db"

def inicializar_db_si_no_existe():
    """Crea la base de datos y tablas solo si el archivo .db no existe."""
    if not os.path.exists(DB_NAME):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            # Creamos la tabla
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS platos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    categoria TEXT,
                    ingredientes TEXT,
                    instrucciones TEXT,
                    imagen_url TEXT,
                    tiempo_preparacion TEXT,
                    dificultad TEXT
                )
            ''')
            
            
            repertorio_inicial = [
                ("Arepa de Reina Pepiada", "Desayunos", "Harina de maíz, aguacate, pollo, mayonesa", "Preparar la masa de arepa, asar. Mezclar pollo desmechado con aguacate y mayonesa. Rellenar.", "https://images.unsplash.com/photo-1541518763669-279f00ed51ca?q=80&w=500", "30 min", "Media"),
                ("Pabellón Criollo", "Almuerzos", "Arroz blanco, caraotas negras, carne mechada, tajadas", "Cocinar los componentes por separado. Servir de forma tradicional acompañando con plátano frito.", "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=500", "1.5 h", "Alta"),
                ("Ensalada César", "Ensaladas", "Lechuga romana, croutons, queso parmesano, aderezo", "Mezclar la lechuga con el aderezo, añadir croutons y queso al gusto.", "https://images.unsplash.com/photo-1550304943-4f24f54ddde9?q=80&w=500", "15 min", "Baja")
            ]
            
            cursor.executemany('''
                INSERT INTO platos (nombre, categoria, ingredientes, instrucciones, imagen_url, tiempo_preparacion, dificultad)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', repertorio_inicial)
            conn.commit()
        st.success("💻 Cookbook.py: Base de datos inicializada correctamente.")

def fetch_recipes():
    """Consulta los datos actuales de la base de datos."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM platos")
            return cursor.fetchall()
    except sqlite3.Error as e:
        st.error(f"Error de base de datos: {e}")
        return []

def main():
    # Configuración de la pestaña del navegador
    st.set_page_config(page_title="Cookbook.py", page_icon="👨‍💻", layout="wide")
    
    # Asegurar que la DB existe
    inicializar_db_si_no_existe()
    
    recipes = fetch_recipes()

    # Título Principal con branding de programador
    st.title("👨‍💻 Cookbook.py: Manual de Sabores")
    st.markdown("---")
    
    # Buscador dinámico
    col_busq1, col_busq2 = st.columns([2, 1])
    with col_busq1:
        busqueda = st.text_input("🔍 Buscar receta o ingrediente...", placeholder="Ej: Aguacate o Almuerzos")

    # Lógica de filtrado
    recetas_filtradas = [
        r for r in recipes 
        if busqueda.lower() in r[1].lower() or busqueda.lower() in r[3].lower() or busqueda.lower() in r[2].lower()
    ]

    # Visualización de resultados
    if not recetas_filtradas:
        st.info("No se encontraron coincidencias en el manual.")
    else:
        for recipe in recetas_filtradas:
            with st.container():
                col1, col2 = st.columns([1, 2])
                with col1:
                    # Imagen con manejo de URL
                    st.image(recipe[5], use_container_width=True)
                with col2:
                    st.header(recipe[1])
                    m1, m2, m3 = st.columns(3)
                    m1.write(f"📁 **Categoría:** {recipe[2]}")
                    m2.write(f"⏱ **Tiempo:** {recipe[6]}")
                    m3.write(f"📊 **Dificultad:** {recipe[7]}")
                    
                    st.write("### 📝 Ingredientes")
                    st.write(recipe[3])
                    
                    with st.expander("Ver Instrucciones de Preparación"):
                        st.write(recipe[4])
                st.divider()

if __name__ == "__main__":
    main()