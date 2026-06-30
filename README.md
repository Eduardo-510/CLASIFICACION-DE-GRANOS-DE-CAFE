# CLASIFICACION-DE-GRANOS-DE-CAFE
Este proyecto tiene como finalidad desarrollar un prototipo funcional basado en visión artificial para la inspección y evaluación preliminar de granos de café. El sistema propuesto integra una faja transportadora como mecanismo de desplazamiento, una cámara ESP32-CAM como dispositivo de adquisición de imagen, un entorno de procesamiento desarrollado en Python con la librería OpenCV, y un sistema de control electromecánico mediante Arduino para la activación del motor de la faja.
Desde el punto de vista técnico, el proyecto se orienta a la implementación de una estación de inspección automatizada, en la cual el grano de café es trasladado hasta una zona de captura controlada.

¿Cómo funciona?

El funcionamiento general se basa en la coordinación entre transporte, captura de imagen y análisis. El grano es llevado por la faja hasta una estación de inspección. En esta estación, la faja debe detenerse para que la imagen no salga borrosa. Luego, Python solicita la imagen al ESP32-CAM, la procesa y clasifica la calidad del grano. Finalmente, Python envía una orden al Arduino para continuar el ciclo.
La faja transporta el grano hasta la zona de visión.
La cámara captura una imagen con iluminación controlada.
El algoritmo calcula variables de forma y color.
El sistema imprime o muestra la calidad estimada del grano.
La faja vuelve a avanzar para procesar el siguiente grano.

Integrantes:

Torres Juarez Eduardo Fabrizio
Alvarado Vilela Cesar Rodrigo
Juarez Chira Frank Reynaldo
Anton Zeta Edwin Fernando
Zapata Viery Sharlles
Izquierdo Montenegro Eduardo
