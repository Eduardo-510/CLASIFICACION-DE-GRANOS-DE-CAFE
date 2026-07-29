# Proyecto Final de PDS 2  
## Clasificación de Calidad de Granos de Café

## Integrantes

- Alvarado Vilela Cesar Rodrigo
- Anton Zeta Fernando
- Izquierdo Montenegro Juan Eduardo
- Juarez Chira Frank Reynaldo
- Torres Juarez Eduardo Fabrizio
- Zapata Viery Sharlles

---

## 1. Descripción general del proyecto

El presente proyecto consiste en el desarrollo de un sistema básico de clasificación de calidad de granos de café mediante visión artificial. El sistema utiliza una cámara ESP32-CAM para capturar imágenes de los granos ubicados sobre una faja transportadora. Posteriormente, las imágenes son enviadas a un programa desarrollado en Python, donde se procesan con la librería OpenCV para identificar el grano, extraer características visuales y determinar su estado.

El sistema permite clasificar el grano de café en diferentes estados, tales como grano bueno, partido, quemado, manchado, inmaduro, objeto no válido o grano no detectado. Esta clasificación se realiza a partir de variables extraídas de la imagen, como área, perímetro, circularidad, solidez, color promedio, desviación de color y valores de color en el espacio HSV.

---

## 2. Problema que aborda

En procesos de selección de granos de café, la evaluación visual suele realizarse de forma manual. Este procedimiento puede ser lento, subjetivo y dependiente de la experiencia del operador. Además, cuando se requiere analizar varios granos, la inspección manual puede generar errores por cansancio, mala iluminación o falta de uniformidad en los criterios de clasificación.

El problema que aborda este proyecto es la necesidad de contar con una herramienta automatizada que permita apoyar la identificación visual de defectos en los granos de café, utilizando una solución de bajo costo basada en hardware accesible y procesamiento digital de imágenes.

---

## 3. Solución propuesta

La solución propuesta consiste en implementar una maqueta funcional compuesta por una faja transportadora, una ESP32-CAM, un sistema de iluminación LED y un programa en Python. La faja transporta el grano hasta una zona de inspección, donde la cámara captura una imagen. Luego, el programa procesa la imagen y muestra el resultado de clasificación.

El procesamiento de imagen incluye las siguientes etapas:

1. Captura de imagen desde la ESP32-CAM mediante conexión WiFi.
2. Conversión de la imagen a escala de grises.
3. Aplicación de filtros para reducir ruido.
4. Detección de bordes.
5. Binarización de la imagen.
6. Limpieza morfológica.
7. Detección de contornos.
8. Extracción de características visuales.
9. Clasificación del grano mediante reglas condicionales.
10. Visualización del resultado final en una interfaz gráfica generada con OpenCV.

---

## 4. Objetivo general

Desarrollar un sistema de clasificación de calidad de granos de café mediante visión artificial, utilizando una ESP32-CAM, procesamiento de imágenes con Python/OpenCV y una faja transportadora controlada electrónicamente.

---

## 5. Objetivos específicos

- Capturar imágenes de granos de café utilizando una ESP32-CAM conectada por WiFi.
- Procesar las imágenes capturadas mediante técnicas de visión artificial.
- Detectar el contorno principal del grano de café dentro de la imagen.
- Extraer variables como área, perímetro, circularidad, solidez, color promedio, desviación de color y valores HSV.
- Clasificar el estado del grano mediante reglas lógicas programadas en Python.
- Mostrar visualmente cada etapa del procesamiento de imagen para facilitar la comprensión del sistema.
- Integrar el sistema de visión artificial con una maqueta física basada en una faja transportadora.

---

## 6. Funcionamiento del sistema

El funcionamiento general del proyecto es el siguiente:

1. El grano de café es colocado sobre la faja transportadora.
2. La faja avanza hasta ubicar el grano en la zona de inspección.
3. La ESP32-CAM captura una imagen del grano.
4. Python solicita la imagen mediante la URL de captura de la cámara.
5. OpenCV procesa la imagen para separar el grano del fondo.
6. El programa calcula características geométricas y de color.
7. Según los valores obtenidos, el sistema clasifica el estado del grano.
8. Se muestra una ventana con el proceso completo y el resultado final.

---


## 7. Tecnologías utilizadas

### Hardware

- ESP32-CAM AI Thinker con sensor OV2640.
- Arduino UNO o placa compatible para control de faja.
- Módulo relé para encendido y apagado del motor DC.
- Motor DC para faja transportadora.
- Fuente externa para el motor.
- Iluminación LED para mejorar la captura de imagen.
- Estructura física o maqueta de faja transportadora.

### Software

- Python.
- OpenCV.
- NumPy.
- Requests.
- Matplotlib.
- Arduino IDE.
- Visual Studio Code.

---

## 8. Versiones utilizadas

Las versiones pueden variar según el equipo donde se ejecute el proyecto. Las versiones utilizadas/recomendadas son:

- Sistema operativo: Windows 10 o Windows 11.
- Python: 3.13 o superior.
- OpenCV: 4.x.
- NumPy: 2.x.
- Requests: 2.x.
- Matplotlib: 3.x.
- Arduino IDE: 2.3.x.
- Placa seleccionada en Arduino IDE: AI Thinker ESP32-CAM.


## 9. Limitaciones del proyecto

- La clasificación se realiza mediante reglas condicionales, no mediante entrenamiento de inteligencia artificial.
- La precisión depende de la iluminación, enfoque, fondo y resolución de la cámara.
- La ESP32-CAM puede saturarse si se usa video en vivo y captura por Python al mismo tiempo.
- El sistema analiza principalmente un grano a la vez.
- Los umbrales de clasificación pueden requerir ajuste según el tipo de café, color del fondo y condiciones de luz.
- La detección puede verse afectada por sombras, reflejos o mala ubicación del grano.

---

## 10. Resultados esperados

Se espera que el sistema pueda:

- Capturar correctamente la imagen del grano.
- Separar el grano del fondo.
- Calcular variables geométricas y de color.
- Clasificar el estado del grano.
- Mostrar el proceso completo de análisis en una sola ventana.
- Servir como prototipo funcional para una solución de clasificación visual de bajo costo.

