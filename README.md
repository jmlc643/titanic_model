# Titanic Survival Prediction API

## 📊 Descripción del Proyecto

Este proyecto implementa un modelo de **Árbol de Decisiones** para predecir la supervivencia de pasajeros del Titanic utilizando el dataset incluido en la librería **Seaborn**. El modelo está desplegado como una API REST usando **FastAPI**, permitiendo realizar predicciones en tiempo real a través de endpoints HTTP.

## 🚀 Características

- **Modelo de Machine Learning**: Árbol de Decisiones entrenado con el dataset del Titanic
- **API REST**: Implementada con FastAPI para predicciones en tiempo real
- **Containerización**: Incluye Dockerfile para fácil despliegue
- **Validación de datos**: Uso de Pydantic para validación automática de entrada
- **Manejo de errores**: Respuestas HTTP apropiadas con códigos de estado

## 🛠️ Tecnologías Utilizadas

- **Python 3.12**
- **FastAPI**: Framework web moderno y rápido
- **Scikit-learn**: Para el modelo de Machine Learning
- **Pandas & Numpy**: Manipulación y procesamiento de datos
- **Seaborn**: Fuente del dataset del Titanic
- **Joblib**: Serialización del modelo entrenado
- **Pydantic**: Validación de datos de entrada
- **Uvicorn**: Servidor ASGI para FastAPI

## 📁 Estructura del Proyecto

```
├── main.py                          # Aplicación FastAPI principal
├── model.py                         # Clase para cargar y usar el modelo
├── input.py                         # Esquemas de datos con Pydantic
├── model.ipynb                      # Notebook de entrenamiento del modelo
├── requirements.txt                 # Dependencias del proyecto
├── Dockerfile                       # Configuración de contenedor
├── README.md                        # Documentación del proyecto
└── models/
    └── titanic_decision_tree_model.pkl  # Modelo entrenado serializado
```

## 🔧 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar o descargar el proyecto**
   ```bash
   git clone https://github.com/jmlc643/titanic_model.git
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   uvicorn main:app --reload
   ```

La API estará disponible en: `http://localhost:8000`

## 📖 Uso de la API

### Endpoints Disponibles

#### 1. Endpoint de Salud
- **URL**: `GET /`
- **Descripción**: Verifica que la API esté funcionando
- **Respuesta**:
  ```json
  {
    "message": "Hello World!"
  }
  ```

#### 2. Endpoint de Predicción
- **URL**: `POST /predict`
- **Descripción**: Predice la supervivencia de un pasajero del Titanic

### Formato de Entrada

```json
{
    "pclass": 1,
    "sex": "female",
    "age": 38.0,
    "sibsp": 1,
    "parch": 0,
    "fare": 71.2833,
    "embarked": "C",
    "alone": false
}
```

#### Descripción de Parámetros:
- **pclass** (int): Clase del pasajero (1, 2, 3)
- **sex** (str): Sexo del pasajero ("male" o "female")
- **age** (float): Edad del pasajero
- **sibsp** (int): Número de hermanos/cónyuge a bordo
- **parch** (int): Número de padres/hijos a bordo
- **fare** (float): Tarifa pagada
- **embarked** (str): Puerto de embarque ("C", "Q", "S")
- **alone** (bool): Si el pasajero viajaba solo

### Formato de Respuesta

```json
{
    "prediction": 1,
    "survived": "Sí"
}
```

- **prediction** (int): Predicción numérica (0 = No sobrevivió, 1 = Sobrevivió)
- **survived** (str): Predicción en texto ("Sí" o "No")

### Ejemplo de Uso con cURL

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "pclass": 1,
       "sex": "female",
       "age": 38.0,
       "sibsp": 1,
       "parch": 0,
       "fare": 71.2833,
       "embarked": "C",
       "alone": false
     }'
```

### Ejemplo de Uso con Python

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "pclass": 1,
    "sex": "female",
    "age": 38.0,
    "sibsp": 1,
    "parch": 0,
    "fare": 71.2833,
    "embarked": "C",
    "alone": False
}

response = requests.post(url, json=data)
print(response.json())
```

## 🐳 Despliegue con Docker

1. **Construir la imagen**
   ```bash
   docker build -t titanic-api .
   ```

2. **Ejecutar el contenedor**
   ```bash
   docker run -p 8000:8000 titanic-api
   ```

## 📊 Sobre el Modelo

El modelo de **Árbol de Decisiones** fue entrenado utilizando el dataset del Titanic de Seaborn, que contiene información sobre los pasajeros del famoso transatlántico. El modelo utiliza características como la clase del pasajero, sexo, edad, número de familiares a bordo, tarifa pagada y puerto de embarque para predecir la probabilidad de supervivencia.

### Características del Dataset:
- **Fuente**: Librería Seaborn
- **Registros**: ~891 pasajeros
- **Características**: 8 variables predictoras
- **Variable objetivo**: Supervivencia (binaria)

## 📈 Documentación Interactiva

Una vez que la aplicación esté ejecutándose, puedes acceder a:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

Estas interfaces permiten probar la API de manera interactiva y explorar todos los endpoints disponibles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes sugerencias de mejora, no dudes en abrir un issue o enviar un pull request.

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

**Desarrollado con ❤️ para el aprendizaje de Machine Learning y APIs**
