# PROYECTO: CLASIFICACION DE CALIDAD DE GRANOS DE CAFE
# ESP32-CAM + PYTHON + OPENCV

# PARTE 7: SEGMENTACION DEL GRANO
# En esta etapa se detectan bordes, se binariza la imagen y se
# limpia el ruido usando operaciones morfologicas.
# =============================================================

# Deteccion de bordes mediante Canny.
img_bordes = cv2.Canny(img_gauss, 80, 150)

# Binarizacion con Otsu invertido.
# Esta parte funciona mejor cuando el fondo es claro y el grano es oscuro.
_, img_bin = cv2.threshold(
    img_gauss,
    0,
    255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# Limpieza de ruido con operaciones morfologicas.
kernel_morf = np.ones((5, 5), np.uint8)

# Apertura: elimina puntos pequeños de ruido.
img_limpia = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel_morf)

# Cierre: ayuda a unir pequenas zonas del objeto detectado.
img_limpia = cv2.morphologyEx(img_limpia, cv2.MORPH_CLOSE, kernel_morf)


# =============================================================
