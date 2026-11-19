import sqlite3
from contextlib import closing

DB_PATH="database.db"

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    # Habilitar llaves foraneas
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_connection() -> None:
    with closing(get_connection()) as conn: # closing para terminar la conexion automaticamente
        
        with conn: # Ejecuta commit o rollback segun el resultado de las consultas
            cursor = conn.cursor()
            
            # Crear tabla Cliente si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido_1 TEXT NOT NULL,
                    apellido_2 TEXT,
                    correo TEXT UNIQUE NOT NULL
                )                   
            """)
            
            # Crear tabla Tecnico si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tecnicos(        
                    id_tecnico INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido_1 TEXT NOT NULL,
                    apellido_2 TEXT,
                    correo TEXT UNIQUE NOT NULL
                )
            """)
            
            # Crear tabla Ticket si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tickets(
                    id_ticket INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER NOT NULL,
                    id_tecnico INTEGER,
                    motivo TEXT NOT NULL,
                    estado TEXT DEFAULT 'Abierto',
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    fecha_cierre TIMESTAMP,
                    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
                    FOREIGN KEY (id_tecnico) REFERENCES tecnicos(id_tecnico)
                )               
            """)