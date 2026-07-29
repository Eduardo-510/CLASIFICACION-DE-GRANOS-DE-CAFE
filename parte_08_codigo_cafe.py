# PROYECTO: CLASIFICACION DE CALIDAD DE GRANOS DE CAFE
# ESP32-CAM + PYTHON + OPENCV

# PARTE 8: DETECCION DE CONTORNOS Y CALCULO DE VARIABLES
# Se detecta el contorno principal del grano y se calculan las
# variables necesarias para clasificarlo.
# =============================================================

contornos, _ = cv2.findContours(img_limpia, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_resultado = img.copy()

print("\nANALISIS DE GRANOS")
print("------------------------------------------")

# Se eliminan contornos demasiado pequenos o demasiado grandes.
candidatos = []

for contorno in contornos:

    area = cv2.contourArea(contorno)

    if area < 80:
        continue

    if area > 12000:
        print("Contorno descartado por fondo/sombra. Area:", round(area, 2))
        continue

    candidatos.append(contorno)

# Variables iniciales del analisis.
total_granos = 0
granos_validos = 0
objetos_no_validos = 0

ultimo_estado = "SIN ANALISIS"
ultima_area = 0
ultimo_perimetro = 0
ultima_circularidad = 0
ultimo_color_promedio = 0
ultima_desviacion_color = 0
ultima_solidez = 0
ultimo_tono_h = 0
ultima_saturacion_s = 0
ultimo_brillo_v = 0

# Si no existe ningun objeto valido, se indica que no se detecto grano.
if len(candidatos) == 0:

    ultimo_estado = "GRANO NO DETECTADO"

    print("\nESTADO: GRANO NO DETECTADO")
    print("Conclusion: No se identifico ningun grano en la zona de inspeccion.")
    print("Recomendacion: Revisar iluminacion, fondo, enfoque o posicion del grano.")

    cv2.putText(img_resultado, "GRANO NO DETECTADO", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

else:

    # Se escoge el contorno con mayor area como objeto principal.
    contorno_principal = max(candidatos, key=cv2.contourArea)

    x1, y1, w1, h1 = cv2.boundingRect(contorno_principal)
    cx1 = x1 + w1 // 2
    cy1 = y1 + h1 // 2

    contornos_grano = [contorno_principal]

    # Se buscan partes cercanas al contorno principal.
    # Esto ayuda cuando un grano esta partido en varias partes.
    for contorno in candidatos:

        if np.array_equal(contorno, contorno_principal):
            continue

        x, y, w, h = cv2.boundingRect(contorno)
        cx = x + w // 2
        cy = y + h // 2

        distancia = ((cx - cx1) ** 2 + (cy - cy1) ** 2) ** 0.5

        if distancia < 80:
            contornos_grano.append(contorno)

    # Se unen los puntos de los contornos considerados parte del grano.
    todos_puntos = np.vstack(contornos_grano)

    area_total = 0
    perimetro_total = 0

    for c in contornos_grano:
        area_total += cv2.contourArea(c)
        perimetro_total += cv2.arcLength(c, True)

    # Circularidad: mide que tan regular o redondeada es la forma.
    if perimetro_total != 0:
        circularidad = 4 * np.pi * area_total / (perimetro_total ** 2)
    else:
        circularidad = 0

    # Solidez: compara el area real con el area de su envolvente convexa.
    hull = cv2.convexHull(todos_puntos)
    area_hull = cv2.contourArea(hull)

    if area_hull != 0:
        solidez = area_total / area_hull
    else:
        solidez = 0

    # Mascara para analizar solo los pixeles del grano.
    mascara = np.zeros(img_gray.shape, dtype=np.uint8)

    for c in contornos_grano:
        cv2.drawContours(mascara, [c], -1, 255, -1)

    color_promedio = cv2.mean(img_gray, mask=mascara)[0]

    pixeles_grano = img_gray[mascara == 255]

    if len(pixeles_grano) > 0:
        desviacion_color = np.std(pixeles_grano)
    else:
        desviacion_color = 0

    # Se convierte a HSV para analizar mejor el color del grano.
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_promedio = cv2.mean(img_hsv[:, :, 0], mask=mascara)[0]
    s_promedio = cv2.mean(img_hsv[:, :, 1], mask=mascara)[0]
    v_promedio = cv2.mean(img_hsv[:, :, 2], mask=mascara)[0]


# =============================================================
