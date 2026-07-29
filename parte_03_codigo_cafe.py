# PROYECTO: CLASIFICACION DE CALIDAD DE GRANOS DE CAFE
# ESP32-CAM + PYTHON + OPENCV

# PARTE 3: PANEL GENERAL DEL PROCESO
# Esta funcion junta en una sola ventana todas las etapas del
# procesamiento de imagen y las variables usadas para clasificar.
# =============================================================

def crear_panel_proceso(img_original, img_gray, img_filtro, img_gauss,
                        img_bordes, img_bin, img_limpia, img_resultado,
                        estado, area, perimetro, circularidad,
                        color_promedio, desviacion_color, solidez,
                        tono_h, saturacion_s, brillo_v,
                        total_granos, granos_validos, objetos_no_validos):

    # Se prepara cada imagen del proceso con su respectivo titulo.
    p1 = preparar_para_panel(img_original, "1. Original")
    p2 = preparar_para_panel(img_gray, "2. Escala de grises")
    p3 = preparar_para_panel(img_filtro, "3. Filtro promedio")
    p4 = preparar_para_panel(img_gauss, "4. Filtro gaussiano")

    p5 = preparar_para_panel(img_bordes, "5. Bordes Canny")
    p6 = preparar_para_panel(img_bin, "6. Imagen binaria")
    p7 = preparar_para_panel(img_limpia, "7. Binaria limpia")
    p8 = preparar_para_panel(img_resultado, "8. Resultado final")

    # Se unen las imagenes en dos filas.
    fila1 = np.hstack((p1, p2, p3, p4))
    fila2 = np.hstack((p5, p6, p7, p8))

    # Se crea una zona inferior para mostrar los resultados numericos.
    ancho_panel = fila1.shape[1]
    alto_info = 200
    panel_info = np.zeros((alto_info, ancho_panel, 3), dtype=np.uint8)

    cv2.putText(panel_info, "RESULTADO DEL ANALISIS DEL GRANO DE CAFE", (20, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.putText(panel_info, "Estado: " + estado, (20, 55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 1)

    cv2.putText(panel_info, "Area: " + str(round(area, 2)), (20, 85),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(panel_info, "Perimetro: " + str(round(perimetro, 2)), (220, 85),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(panel_info, "Circularidad: " + str(round(circularidad, 2)), (470, 85),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(panel_info, "Solidez: " + str(round(solidez, 2)), (720, 85),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(panel_info, "Color prom: " + str(round(color_promedio, 2)), (900, 85),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(panel_info, "Desv. color: " + str(round(desviacion_color, 2)), (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(panel_info, "HSV H: " + str(round(tono_h, 2)), (300, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(panel_info, "HSV S: " + str(round(saturacion_s, 2)), (500, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(panel_info, "HSV V: " + str(round(brillo_v, 2)), (700, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(panel_info, "Objetos detectados: " + str(total_granos), (20, 155),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    cv2.putText(panel_info, "Granos validos: " + str(granos_validos), (300, 155),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    cv2.putText(panel_info, "Objetos no validos: " + str(objetos_no_validos), (550, 155),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    cv2.putText(panel_info,
                "Variables usadas: area, perimetro, circularidad, solidez, color promedio, desviacion y HSV",
                (20, 185), cv2.FONT_HERSHEY_SIMPLEX, 0.48, (180, 180, 180), 1)

    # Se une todo en una sola imagen final.
    panel = np.vstack((fila1, fila2, panel_info))

    return panel


# =============================================================
