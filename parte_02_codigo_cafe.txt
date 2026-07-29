# PROYECTO: CLASIFICACION DE CALIDAD DE GRANOS DE CAFE
# ESP32-CAM + PYTHON + OPENCV

# PARTE 2: FUNCIONES BASICAS DE INFORMACION Y PRESENTACION
# Estas funciones ayudan a revisar datos de la imagen y preparar
# cada etapa para mostrarla ordenadamente en un panel visual.
# =============================================================

def InfoImg(img):
    # Muestra informacion general de la imagen capturada o procesada
    print("Tamaño:", img.shape)
    print("Valor maximo:", np.max(img))
    print("Valor minimo:", np.min(img))
    print("Valor promedio:", round(np.mean(img), 2))


def preparar_para_panel(imagen, titulo, ancho=320, alto=240):
    # Si la imagen esta en escala de grises, se convierte a BGR
    # para poder unirla con otras imagenes a color en el panel.
    if len(imagen.shape) == 2:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

    # Se ajusta el tamaño de cada imagen para que todas tengan
    # la misma dimension dentro del panel final.
    imagen = cv2.resize(imagen, (ancho, alto))

    # Se coloca una franja negra con el nombre de la etapa.
    cv2.rectangle(imagen, (0, 0), (ancho, 30), (0, 0, 0), -1)
    cv2.putText(imagen, titulo, (10, 22),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    return imagen


# =============================================================
