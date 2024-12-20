# Interpretador de Sueños - API

## Descripción
Esta API permite interpretar descripciones de sueños proporcionadas por los usuarios. Utiliza FastAPI para manejar las solicitudes y respuestas, y se integra con un servicio externo para generar interpretaciones basadas en la descripción del sueño.

---

## Características Principales
- **Interpretación de Sueños**: Proporciona interpretaciones detalladas basadas en las descripciones enviadas por el usuario.
- **Documentación Interactiva**: Incluye Swagger UI y Redoc para explorar los endpoints.

---

## Endpoints

### 1. **Raíz del API**
**GET /**

- **Descripción**: Devuelve un mensaje de bienvenida para verificar que el servidor esté en funcionamiento.
- **Respuesta**:
  ```json
  {
    "Hello": "World"
  }
  ```

### 2. **Interpretación de Sueños**
**POST /interpreter/**

- **Descripción**: Interpreta la descripción de un sueño proporcionada por el usuario.
- **Parámetros de Entrada**:
  - **dream_description** (objeto `DreamRequest`): La descripción del sueño a interpretar.
  ```json
  {
    "dream_description": "Soñé que estaba volando sobre una ciudad desconocida."
  }
  ```
- **Respuesta**:
  - Código 200: Devuelve una interpretación como una cadena de texto.
    ```json
    "La ciudad representa tu deseo de explorar nuevas oportunidades."
    ```
  - Código 400: Devuelve un error si no se proporciona una descripción válida.
    ```json
    {
      "detail": "No se ha proporcionado una descripción del sueño."
    }
    ```

---

## Cómo Ejecutar la API

### 1. **Requisitos Previos**
- Python 3.9 o superior
- `pip` para gestionar dependencias

### 2. **Instalación**
1. Clona este repositorio:
   ```bash
   git clone https://github.com/MatiSrv/SiravegnaMatias-api-dream-challengefinal/edit/main/README.md
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### 3. **Ejecuta el Servidor**
1. Inicia el servidor de desarrollo:
   ```bash
   uvicorn main:app --reload
   ```
2. Accede a la API en tu navegador:
   - Documentación interactiva (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Documentación Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---


Si necesitas modificar los orígenes permitidos, actualiza la configuración en el archivo `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://nuevo-origen.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Dependencias Clave
- **FastAPI**: Framework principal para la creación de la API.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación.
- **CORS Middleware**: Para habilitar solicitudes cruzadas entre dominios.

---

## Futuras Mejoras
- Agregar base de datos relacional para almacenar datos
- Agregar modulo de usuarios 
- Agregar autenticación para proteger los endpoints.
---

