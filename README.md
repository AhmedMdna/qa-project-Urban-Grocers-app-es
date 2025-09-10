# Proyecto Urban Grocers: 

- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Ejecuta todas las pruebas con el comando pytest.


[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Testing%20Framework-green)](https://docs.pytest.org/)

-Automatización de pruebas para la API de Urban Grocers, con enfoque en el campo `name` en la solicitud de creación de un kit de productos.

## 📋 Requisitos
- Python 3.8+
- Dependencias: `pytest`, `requests`
- Se pueden consultar los requisitos de la api siguiendo el enlace URL_SERVICE+"/docs/"

## 🛠 Instalación
```bash
git clone https://github.com/AhmedMdna/qa-project-Urban-Grocers-app-es
cd tu-repo
pip install pytest requests

🗂 Estructura
.
├── data.py # Headers y cuerpos de requests, datos de pruebas
├── configuration.py # URLs y endpoints
├── sender_stand_request.py # Cliente HTTP para crear user y kit
├── create_kit_name_kit_test.py # Archivo de pruebas (9 casos)
└── README.md

▶ Ejecución
bash
# Ejecutar todas las pruebas:
pytest create_kit_name_kit_test.py -v

# Ejecutar prueba específica:
# Ejemplo Prueba 1: Nombre con 1 carácter
pytest create_kit_name_kit_test.py::test_1_create_kit_name_1_letter -v

🧪 Casos Cubiertos
Caso	Descripción	                Status Esperado
1	Nombre con 1 carácter   	        201
2	Nombre con 511 caracteres   	        201
3	Nombre vacío ("")                       400
4       Nombre con 512 caracteres	        400
5	Caracteres especiales (Ej: №%@)	        201
6       Nombre con espacios                     201
7       Nombre con números                      201
8	Campo `name` ausente	                400
9       Parametro de tipo diferente             400
