
# Proyecto Urban Routes - Qa Engineer TripleTen

Este proyecto consiste en una aplicación para solicitar taxis llamada Urban Routes, de la cual, el equipo de desarrollo realizó una lista de varias pruebas para comprobar la funcionalidad de la aplicación, por lo que este trabajo se basa en describir el proceso de las pruebas automatizadas.

## Estructura del Proyecto

### Archivos y Directorios Principales

- **`data.py`**: Archivo encargado de manejar los datos del proyecto.
- **`main.py`**: Archivo en donde se desarrollan las pruebas automatizadas

## Tecnologías Utilizadas

- **Pycharm**: Entorno de Desarrollo Integrado para trabajar con Python.
- **Pytest**: Framework para Python que permite la ejecución de pruebas automatizadas de manera simple, escalable y expresiva.
- **Python**: Lenguaje de programación principal del proyecto.
- **Selenium WebDriver**: Herramienta que permite la automatización de pruebas mediante el control de navegadores web.
- **Assert:** Confirma los resultados esperados en cada paso de la prueba.
- **WebDriverWait**: Herramienta de espera explícita que se usa en Selenium WebDriver para decirle al script que espere hasta que ocurra una condición específica antes de continuar.
- **Expected Conditions (EC)**: Son condiciones predefinidas que se usan junto con WebDriverWait en Selenium para esperar hasta que algo específico ocurra en la página web.
- **Google Chrome y ChromeDriver:** Navegador y controlador utilizados para la ejecución de las pruebas.

## Ejecución de las Pruebas
 
 **Requisitos previos**
 
 * **Instalar dependencias:** Asegúrate de tener Python instalado y luego instala las dependencias necesarias con:
 `pip install selenium pytest`
 *  **Configurar ChromeDriver:** Descarga e instala ChromeDriver.
 * **Agrega ChromeDriver al PATH de tu sistema.**

## Explicación de las Pruebas

Las pruebas automatizadas verifican los siguientes escenarios:
* **test_set_route:** Verifica que la ruta de origen y destino se puede establecer correctamente.

* **test_select_comfort_rate_icon:** Comprueba la selección de la tarifa "Comfort".

* **test_enter_phone_number:** Valida la autenticación con código SMS.

* **test_enter_payment_method:** Añade y verifica un método de pago.

* **test_enter_message_to_driver:** Envía un mensaje al conductor.

* **test_select_blanket_and_handkerchief:** Activa la opción de cobija y pañuelo.

* **test_add_ice_cream:** Incrementa el contador de helado.

* **test_order_taxi_button:** Solicita un taxi exitosamente.

* **test_trip_details_modal_after_countdown:** Muestra los modales del contador y de la información del viaje.

**IMPORTANTE**
* Se recomienda cerrar todas las ventanas del navegador antes de ejecutar las pruebas para evitar conflictos.

* Asegúrate de actualizar la URL de Urban Routes data.py antes de ejecutar las pruebas.

## Estructura del archivo de prueba main.py
 **Imports utilizados**    
El código usa los siguientes imports
```python
import sender_stand_requests  
import data
import json
import time
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

---

Claudia Faúndez, Cohorte 27, Sprint 8  
