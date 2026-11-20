# 🤖 BotLangChain - Asistente de Servicio al Cliente con IA

![Estado](https://img.shields.io/badge/Estado-Alpha-orange)
![Python](https://img.shields.io/badge/Python-3.12%20%7C%203.13-blue)
![Framework](https://img.shields.io/badge/LangChain-AI%20Agent-green)

Aplicación de chat web inteligente diseñada como sistema de soporte y asistencia para una **tienda en línea de videojuegos** (estilo Steam o Epic Games). Utiliza Inteligencia Artificial Generativa, búsqueda semántica (RAG) y ejecución de herramientas (*Tool Calling*) para consultar y gestionar información según el rol del usuario.

---

## 🎯 Funcionalidades por Rol

El sistema delimita el comportamiento y acceso a datos mediante prompts específicos y herramientas asignadas:

* **👤 Rol Usuario (Cliente):**
  * Resolución de dudas frecuentes y políticas de la tienda mediante consulta **RAG** sobre documentación en Markdown.
  * Consulta de estado de tickets, compras o información personal en la base de datos mediante `@tools`.
* **🛡️ Rol Administrador:**
  * Acceso completo a consultas **RAG** y consultas avanzadas a la base de datos.
  * Búsqueda de historial, tickets y registros de usuarios específicos para soporte técnico y gestión.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python (3.12 - 3.13)
* **Orquestación de IA:** LangChain (RAG & Tool Calling)
* **Modelo LLM:** Google Gemini AI
* **Base de Datos Relacional:** SQLite
* **Base de Datos Vectorial:** ChromaDB
* **Interfaz Web:** Streamlit

---

## 📋 Prerrequisitos

Antes de comenzar, asegúrate de contar con:
1. **Python 3.12 o 3.13** instalado en tu sistema.
2. Una **API Key de Google Gemini** (puedes obtenerla en Google AI Studio).

---

## 🚀 Guía de Instalación

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/SrChicken6711/BotLangChain.git](https://github.com/SrChicken6711/BotLangChain.git)
cd BotLangChain
```

2. Crear y activar el entorno virtual (venv)

#### Linux / macOS:

```Bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows (PowerShell / CMD):

```PowerShell
python -m venv venv
.\venv\Scripts\activate
```
#### 3. Instalar dependencias
```Bash
pip install -r requirements.txt
```

#### 4. Configurar variables de entorno
Crea tu archivo .env a partir de la plantilla de ejemplo y añade tu llave de API:
```Bash
cp .env.example .env
```
(Edita el archivo .env y asigna tu clave en la variable correspondiente).

#### 5. Inicializar la base de datos
Ejecuta el script de inicialización para crear las tablas y cargar los datos base de prueba:

```Bash
python init_db.py
```

#### 6. Ejecución
⚠️ Nota: La interfaz web en Streamlit se encuentra actualmente en desarrollo.
```Bash
# Próximamente:
streamlit run app.py
```
#### 📂 Estructura del Proyecto
```Plaintext
BotLangChain/
├── docs/                  # Documentos Markdown base para el sistema RAG
├── pages/
│   └── admin.py           # Vista y panel para el rol de administrador
├── prompts/               # Instrucciones del sistema (System Prompts) por rol
│   ├── admin.md           # Prompt y reglas para administradores
│   └── client.md          # Prompt y reglas para clientes
├── querys/                # Scripts SQL
│   ├── base_data.sql      # Datos semilla (seed) para pruebas
│   └── querys.sql         # Consultas SQL utilizadas por las tools del agente
├── .env.example           # Plantilla de variables de entorno requeridas
├── .gitignore             # Archivos ignorados por Git
├── .python-version        # Versión de Python recomendada para el entorno
├── app.py                 # Punto de entrada principal de la aplicación Streamlit
├── bot_engine.py          # Lógica principal y configuración del agente LangChain
├── db_manager.py          # Gestor de conexión y funciones de consulta (@tools)
├── init_db.py             # Script de creación e inicialización de SQLite
├── rag_manager.py         # Gestión de embeddings y recuperación en ChromaDB
├── README.md              # Documentación del proyecto
└── requirements.txt       # Dependencias del proyecto
```

### 🗺️ Hoja de Ruta (Roadmap)
[x] Fase 1: Núcleo del Bot Conversacional

[x] Bot capaz de mantener conversaciones (pruebas iniciales por CLI).

[x] División de roles y prompts (admin.md / client.md) para delimitar permisos.

[ ] Fase 2: Base de Datos y Tool Calling (En progreso)

[x] Diseño relacional y conexión de tablas en SQLite.

[x] Creación e inicialización de la base de datos (init_db.py).

[ ] Creación y validación de consultas SQL (querys.sql).

[ ] Implementación de consultas como @tools en LangChain (db_manager.py).

[ ] Pruebas integrales del agente interactuando con la base de datos.

[ ] Fase 3: Sistema RAG

[ ] Generación de embeddings e indexación de archivos .md en ChromaDB (rag_manager.py).

[ ] Fase 4: Interfaz Web

[ ] Desarrollo de vistas interactivas de cliente y administrador en Streamlit (app.py, pages/admin.py).

#### 💡 Ejemplo de Respuesta del Agente
Respuesta estructurada devuelta por el motor conversacional al procesar una interacción mediante la API:

```JSON
[
  {
    "type": "text",
    "text": "¡Hola! 😊 ¿Qué tal? ¿En qué te puedo ayudar hoy?",
    "extras": {
      "signature": "EokBCoYBAWkUfRPO9y3aUqRhUXKYwME9Lb0qL5T5po9c8hcFjv6dN8tqZ/h9HUFkLjXqzX7yv6e3KU2FislrgBXjYhSuMESSj1KXUstL2ZuW/2F4UxsZ7Hq2DTCD4ZcZHPRwov79wTAQbGEKOmtAjsCYKuDiAQ2fWtsDp6BQh7Y36NnrKetcuz2t1tA="
    }
  }
]
```

#### 👨‍💻 Autor
Victor De Luna
GitHub: @SrChicken6711