# PROYECTO: CLASIFICACION DE CALIDAD DE GRANOS DE CAFE
# ESP32-CAM + PYTHON + OPENCV

# PARTE 9: CLASIFICACION FINAL Y DIBUJO DEL RESULTADO
# Con las variables calculadas se determina el estado del grano
# y se dibuja un rectangulo con el resultado sobre la imagen.
# =============================================================

if len(candidatos) > 0:

    estado, conclusion = clasificar_grano(
        area_total,
        perimetro_total,
        circularidad,
        color_promedio,
        desviacion_color,
        solidez,
        h_promedio,
        s_promedio,
        v_promedio
    )

    # Validacion extra para objetos demasiado pequenos.
    if area_total < 500:
        estado = "OBJETO NO VALIDO"
        conclusion = "El objeto detectado no cumple el tamaño minimo para ser considerado grano de cafe."

    # Si hay varias partes cercanas, se considera grano partido.
    elif len(contornos_grano) > 1 and estado != "INMADURO":
        estado = "PARTIDO"
        conclusion = "El grano presenta separacion o fragmentacion visible."

    total_granos = 1

    if estado == "OBJETO NO VALIDO":
        granos_validos = 0
        objetos_no_validos = 1
    else:
        granos_validos = 1
        objetos_no_validos = 0

    ultimo_estado = estado
    ultima_area = area_total
    ultimo_perimetro = perimetro_total
    ultima_circularidad = circularidad
    ultimo_color_promedio = color_promedio
    ultima_desviacion_color = desviacion_color
    ultima_solidez = solidez
    ultimo_tono_h = h_promedio
    ultima_saturacion_s = s_promedio
    ultimo_brillo_v = v_promedio

    # Color del rectangulo segun el estado obtenido.
    if estado == "BUENO":
        color_rectangulo = (0, 255, 0)
    elif estado == "PARTIDO":
        color_rectangulo = (0, 165, 255)
    elif estado == "INMADURO":
        color_rectangulo = (255, 255, 0)
    else:
        color_rectangulo = (0, 0, 255)

    # Se dibuja el rectangulo sobre el objeto detectado.
    x, y, w, h = cv2.boundingRect(todos_puntos)

    cv2.rectangle(img_resultado, (x, y), (x + w, y + h), color_rectangulo, 2)

    cv2.putText(img_resultado, estado, (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, color_rectangulo, 2)

    print("Estado:", estado)
    print("Area:", round(area_total, 2))
    print("Perimetro:", round(perimetro_total, 2))
    print("Circularidad:", round(circularidad, 2))
    print("Solidez:", round(solidez, 2))
    print("Color promedio:", round(color_promedio, 2))
    print("Desviacion de color:", round(desviacion_color, 2))
    print("HSV H:", round(h_promedio, 2))
    print("HSV S:", round(s_promedio, 2))
    print("HSV V:", round(v_promedio, 2))
    print("Partes detectadas:", len(contornos_grano))
    print("Conclusion:", conclusion)
    print("------------------------------------------")


# =============================================================
