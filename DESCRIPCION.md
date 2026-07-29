## DESCRIPCION GENERAL DEL PROYECTO 
-El proyecto presenta el desarrollo de un prototipo para la clasificación básica de la calidad de granos de café mediante técnicas de visión artificial. El sistema integra una ESP32-CAM para la captura de imágenes, Python con OpenCV y NumPy para el procesamiento digital, y un Arduino encargado del control de una faja transportadora mediante un driver TB6612FNG. El algoritmo procesa la imagen a través de etapas como conversión a escala de grises, análisis de histograma, filtrado, detección de bordes, binarización, limpieza morfológica y extracción de contornos. Posteriormente calcula variables como área, perímetro, circularidad, color promedio y desviación de color para clasificar los granos en categorías como bueno, pequeño, partido, quemado, manchado u objeto no válido. El informe también describe la arquitectura del sistema, los componentes utilizados, la integración hardware-software y el avance alcanzado, validando la viabilidad técnica del prototipo para una futura automatización completa del proceso de inspección.

## PROBLEMA QUE SE BUSCA RESOLVER
-Tradicionalmente, la evaluación de la calidad del café se realiza mediante inspección visual por parte de operadores especializados, quienes clasifican los granos considerando características como el tamaño, la forma, el color y la presencia de defectos físicos. Aunque este procedimiento ha demostrado ser efectivo cuando es realizado por personal experimentado, presenta diversas limitaciones relacionadas con la subjetividad del evaluador, la fatiga visual, la variabilidad entre inspectores y el elevado tiempo requerido para analizar grandes volúmenes de producción. Estas limitaciones reducen la repetibilidad del proceso e incrementan los costos operativos, especialmente para pequeños productores que no disponen de equipos industriales automatizados. 

## POSIBLE SOLUCION
-En este contexto surge la motivación del presente proyecto, cuyo propósito consiste en desarrollar un prototipo funcional de bajo costo para la clasificación preliminar de granos de café mediante visión artificial. A diferencia de soluciones industriales complejas, la propuesta integra una cámara ESP32-CAM para la adquisición de imágenes, un algoritmo desarrollado en Python utilizando la biblioteca OpenCV para el procesamiento digital y un Arduino encargado del control de una faja transportadora. Esta arquitectura busca demostrar que es posible implementar un sistema de inspección automatizada utilizando componentes económicos y ampliamente disponibles, sin sacrificar la capacidad de identificar características relevantes del grano.

## OBJETIVO
-Por ello, este trabajo busca contribuir al desarrollo de soluciones tecnológicas accesibles para la automatización del control de calidad del café, proporcionando una plataforma escalable que en futuras investigaciones podrá incorporar técnicas de aprendizaje automático o redes neuronales profundas para incrementar la precisión de la clasificación sin modificar significativamente la arquitectura general del sistema.

## LIMITACIONES
-Las principales limitaciones que presenta en este proyecto es que si bien el proceso es automatico, la colocacion de los granos de cafe es de forma manual esto influye en el tiempo que se necesita para seleccionar grandes cantidades de granos de cafe, tambien existe una precaria visualizacion debido a que la camara que se utiliza para capturar la imagen del grano es poco eficiente, pero es un buen prototipo para posibles mejoras y actualizaciones del sistema.

## VERSIONES DE LOS PAQUETES UTILIZADOS
- ESP32 CAM
- ARDUINO UNO
- DRIVER TB6612FNG
- MOTOR DC 12
- FAJA TRANSPORTADORA

## SISTEMA OPERATIVO
- WINDOWS

## ENTORNO DE TRABAJO
-Visual Studio Code 1.103 (Python) y Arduino IDE 2.x para la programación del Arduino UNO.


## Integrantes:

-Torres Juarez Eduardo Fabrizio

-Alvarado Vilela Cesar Rodrigo

-Juarez Chira Frank Reynaldo

-Anton Zeta Edwin Fernando

-Zapata Viery Sharlles

-Izquierdo Montenegro Eduardo
