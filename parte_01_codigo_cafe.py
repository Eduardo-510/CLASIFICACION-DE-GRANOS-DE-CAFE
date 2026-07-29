# PROYECTO: CLASIFICACION DE CALIDAD DE GRANOS DE CAFE
# ESP32-CAM + PYTHON + OPENCV

# PARTE 1: LIBRERIAS
# En esta parte se importan las librerias necesarias para capturar,
# procesar y mostrar la imagen del grano de cafe.
# =============================================================

import cv2                    # Libreria OpenCV para procesamiento de imagenes
import requests               # Permite conectarse a la ESP32-CAM por medio de la IP
import numpy as np             # Permite trabajar con matrices y operaciones matematicas
import matplotlib.pyplot as plt # Permite graficar el histograma de la imagen
import time                    # Permite usar pausas y tiempos de espera


# =============================================================
