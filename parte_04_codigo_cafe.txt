# PROYECTO: CLASIFICACION DE CALIDAD DE GRANOS DE CAFE
# ESP32-CAM + PYTHON + OPENCV

# PARTE 4: REGLAS DE CLASIFICACION DEL GRANO
# Esta funcion decide el estado del grano usando variables como
# area, circularidad, solidez, color promedio y HSV.
# =============================================================

def clasificar_grano(area, perimetro, circularidad, color_promedio,
                     desviacion_color, solidez, tono_h, saturacion_s, brillo_v):

    estado = "BUENO"
    conclusion = "El grano presenta tamaño, forma y color aceptable."

    # Objeto demasiado pequeño: no se considera grano valido.
    if area < 500:
        estado = "OBJETO NO VALIDO"
        conclusion = "El objeto detectado es demasiado pequeño o no corresponde a un grano de cafe."

    # Objeto demasiado grande: puede ser fondo, sombra, mano u otro objeto.
    elif area > 8000:
        estado = "OBJETO NO VALIDO"
        conclusion = "El objeto detectado es demasiado grande para ser considerado un grano de cafe."

    # Tono verdoso: se considera grano inmaduro o no tostado.
    elif tono_h >= 35 and tono_h <= 95 and saturacion_s > 18 and brillo_v > 80:
        estado = "INMADURO"
        conclusion = "El grano presenta coloracion verde clara, posiblemente inmaduro o no tostado."

    # Baja solidez: indica huecos, quiebres o forma incompleta.
    elif solidez < 0.88:
        estado = "PARTIDO"
        conclusion = "El grano presenta una hendidura o parte incompleta."

    # Baja circularidad: indica forma irregular.
    elif circularidad < 0.55:
        estado = "PARTIDO"
        conclusion = "El grano presenta forma irregular, posiblemente esta partido."

    # Color promedio bajo: el grano se ve demasiado oscuro.
    elif color_promedio < 60:
        estado = "QUEMADO"
        conclusion = "El grano presenta color muy oscuro."

    # Alta desviacion de color: presencia de manchas o color no uniforme.
    elif desviacion_color > 32:
        estado = "MANCHADO"
        conclusion = "El grano presenta variaciones fuertes de color."

    return estado, conclusion


# =============================================================
