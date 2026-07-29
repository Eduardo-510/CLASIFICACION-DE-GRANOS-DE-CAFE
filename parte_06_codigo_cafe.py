# PROYECTO: CLASIFICACION DE CALIDAD DE GRANOS DE CAFE
# ESP32-CAM + PYTHON + OPENCV

# PARTE 6: PREPROCESAMIENTO DE LA IMAGEN
# Aqui se convierte la imagen a escala de grises, se analiza su
# histograma y se aplican filtros para reducir ruido.
# =============================================================

print("\nINFORMACION DE IMAGEN ORIGINAL")
InfoImg(img)

# Conversion de imagen original a escala de grises.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("\nINFORMACION DE IMAGEN EN ESCALA DE GRISES")
InfoImg(img_gray)

# Histograma: muestra la distribucion de intensidades de gris.
hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

plt.figure()
plt.plot(hist)
plt.title("Histograma de la imagen en escala de grises")
plt.xlabel("Nivel de gris")
plt.ylabel("Cantidad de pixeles")
plt.show(block=False)

# Filtro promedio: suaviza la imagen.
kernel = np.ones((5, 5), np.float32) / 25
img_filtro = cv2.filter2D(img_gray, -1, kernel)

# Filtro gaussiano: reduce ruido y mejora la deteccion posterior.
img_gauss = cv2.GaussianBlur(img_gray, (5, 5), 0)


# =============================================================
