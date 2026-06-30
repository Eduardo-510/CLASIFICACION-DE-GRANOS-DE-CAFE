#LIBRERIAS
import cv2
import requests
import numpy as np
import matplotlib.pyplot as plt
import time


# FUNCION PARA VER INFORMACION DE LA IMAGEN
def InfoImg(img):
    print("Tamaño:", img.shape)
    print("Valor maximo:", np.max(img))
    print("Valor minimo:", np.min(img))
    print("Valor promedio:", round(np.mean(img), 2))


# FUNCION PARA PREPARAR CADA IMAGEN DEL PROCESO
def preparar_para_panel(imagen, titulo, ancho=320, alto=240):

    if len(imagen.shape) == 2:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)

    imagen = cv2.resize(imagen, (ancho, alto))

    cv2.rectangle(imagen, (0, 0), (ancho, 30), (0, 0, 0), -1)
    cv2.putText(imagen, titulo, (10, 22),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    return imagen


# FUNCION PARA MOSTRAR TODO EL PROCESO EN UNA SOLA VENTANA
def crear_panel_proceso(img_original, img_gray, img_filtro, img_gauss,
                        img_bordes, img_bin, img_limpia, img_resultado,
                        estado, area, perimetro, circularidad,
                        color_promedio, desviacion_color,
                        total_granos, granos_validos, objetos_no_validos):

    p1 = preparar_para_panel(img_original, "1. Original")
    p2 = preparar_para_panel(img_gray, "2. Escala de grises")
    p3 = preparar_para_panel(img_filtro, "3. Filtro promedio")
    p4 = preparar_para_panel(img_gauss, "4. Filtro gaussiano")

    p5 = preparar_para_panel(img_bordes, "5. Bordes Canny")
    p6 = preparar_para_panel(img_bin, "6. Imagen binaria")
    p7 = preparar_para_panel(img_limpia, "7. Binaria limpia")
    p8 = preparar_para_panel(img_resultado, "8. Resultado final")

    fila1 = np.hstack((p1, p2, p3, p4))
    fila2 = np.hstack((p5, p6, p7, p8))

    # FRANJA INFERIOR PARA MOSTRAR VARIABLES
    ancho_panel = fila1.shape[1]
    alto_info = 150
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

    cv2.putText(panel_info, "Color promedio: " + str(round(color_promedio, 2)), (720, 85),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(panel_info, "Desv. color: " + str(round(desviacion_color, 2)), (1000, 85),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(panel_info, "Objetos detectados: " + str(total_granos), (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    cv2.putText(panel_info, "Granos validos: " + str(granos_validos), (300, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    cv2.putText(panel_info, "Objetos no validos: " + str(objetos_no_validos), (550, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    panel = np.vstack((fila1, fila2, panel_info))

    return panel


# CLASIFICACION DEL GRANO
def clasificar_grano(area, perimetro, circularidad, color_promedio, desviacion_color):

    estado = "BUENO"
    conclusion = "El grano presenta tamaño, forma y color aceptable."

    if area > 8000:
        estado = "OBJETO NO VALIDO"
        conclusion = "No se encontro un grano de cafe valido en la zona de inspeccion."

    elif circularidad < 0.20:
        estado = "OBJETO NO VALIDO"
        conclusion = "No se encontro un grano de cafe valido. La forma detectada no corresponde a un grano."

    elif area < 300:
        estado = "PEQUEÑO"
        conclusion = "El grano tiene un area menor al valor esperado."

    elif circularidad < 0.45:
        estado = "PARTIDO"
        conclusion = "El grano presenta forma irregular, posiblemente esta partido o deformado."

    elif color_promedio < 60:
        estado = "QUEMADO"
        conclusion = "El grano presenta color muy oscuro, por lo que puede estar quemado o defectuoso."

    elif desviacion_color > 35:
        estado = "MANCHADO"
        conclusion = "El grano presenta variaciones fuertes de color, posiblemente tiene manchas."

    return estado, conclusion


# TOMA FOTO DEL ESP32-CAM
url = "http://172.20.10.10/capture"

session = requests.Session()
session.trust_env = False

print("Capturando imagen desde ESP32-CAM...")

respuesta = session.get(url, timeout=10)

img_array = np.frombuffer(respuesta.content, np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

if img is None:
    print("No se pudo leer la imagen")
    exit()


# INFORMACION DE IMAGEN ORIGINAL
print("\nINFORMACION DE IMAGEN ORIGINAL")
InfoImg(img)


# ESCALA DE GRISES
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("\nINFORMACION DE IMAGEN EN ESCALA DE GRISES")
InfoImg(img_gray)


# HISTOGRAMA
hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

plt.figure()
plt.plot(hist)
plt.title("Histograma de la imagen en escala de grises")
plt.xlabel("Nivel de gris")
plt.ylabel("Cantidad de pixeles")
plt.show(block=False)


# FILTRO PROMEDIO
kernel = np.ones((5, 5), np.float32) / 25
img_filtro = cv2.filter2D(img_gray, -1, kernel)


# FILTRO GAUSSIANO
img_gauss = cv2.GaussianBlur(img_gray, (5, 5), 0)


# DETECCION DE BORDES
img_bordes = cv2.Canny(img_gauss, 80, 150)


# BINARIZACION
_, img_bin = cv2.threshold(img_gauss, 90, 255, cv2.THRESH_BINARY_INV)


# LIMPIEZA DE RUIDO
kernel_morf = np.ones((3, 3), np.uint8)
img_limpia = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel_morf)


# DETECCION DE CONTORNOS
contornos, _ = cv2.findContours(img_limpia, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_resultado = img.copy()

total_granos = 0
granos_validos = 0
objetos_no_validos = 0

ultimo_estado = "SIN ANALISIS"
ultima_area = 0
ultimo_perimetro = 0
ultima_circularidad = 0
ultimo_color_promedio = 0
ultima_desviacion_color = 0

print("\nANALISIS DE GRANOS")
print("------------------------------------------")


# ANALISIS DE CADA CONTORNO
for contorno in contornos:

    area = cv2.contourArea(contorno)

    # Evita contar ruido pequeño
    if area < 100:
        continue

    perimetro = cv2.arcLength(contorno, True)

    if perimetro == 0:
        continue

    circularidad = 4 * np.pi * area / (perimetro ** 2)

    # Mascara para analizar solo el objeto detectado
    mascara = np.zeros(img_gray.shape, dtype=np.uint8)
    cv2.drawContours(mascara, [contorno], -1, 255, -1)

    color_promedio = cv2.mean(img_gray, mask=mascara)[0]

    pixeles_grano = img_gray[mascara == 255]
    desviacion_color = np.std(pixeles_grano)

    estado, conclusion = clasificar_grano(
        area,
        perimetro,
        circularidad,
        color_promedio,
        desviacion_color
    )

    total_granos += 1

    if estado == "OBJETO NO VALIDO":
        objetos_no_validos += 1
        color_rectangulo = (0, 0, 255)
    else:
        granos_validos += 1
        color_rectangulo = (0, 255, 0)

    ultimo_estado = estado
    ultima_area = area
    ultimo_perimetro = perimetro
    ultima_circularidad = circularidad
    ultimo_color_promedio = color_promedio
    ultima_desviacion_color = desviacion_color

    # MOSTRAR RESULTADO FINAL
    x, y, w, h = cv2.boundingRect(contorno)

    cv2.rectangle(img_resultado, (x, y), (x + w, y + h), color_rectangulo, 2)

    cv2.putText(img_resultado, estado, (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_rectangulo, 1)

    print("Grano N°:", total_granos)
    print("Area:", round(area, 2))
    print("Perimetro:", round(perimetro, 2))
    print("Circularidad:", round(circularidad, 2))
    print("Color promedio:", round(color_promedio, 2))
    print("Desviacion de color:", round(desviacion_color, 2))
    print("Estado:", estado)
    print("Conclusion:", conclusion)
    print("------------------------------------------")


# CONCLUSION
print("\nRESUMEN")
print("Cantidad de objetos detectados:", total_granos)
print("Cantidad de granos validos:", granos_validos)
print("Objetos no validos:", objetos_no_validos)

if total_granos == 0:
    ultimo_estado = "GRANO NO DETECTADO"

    print("\nESTADO: GRANO NO DETECTADO")
    print("Conclusion: No se identifico ningun grano en la zona de inspeccion.")
    print("Recomendacion: Revisar iluminacion, fondo, enfoque o posicion del grano.")

    cv2.putText(img_resultado, "GRANO NO DETECTADO", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

elif granos_validos == 0 and objetos_no_validos > 0:
    ultimo_estado = "OBJETO NO VALIDO"

    print("\nESTADO: OBJETO NO VALIDO")
    print("Conclusion: No se encontro un grano de cafe valido en la zona de inspeccion.")
    print("Recomendacion: Retirar objetos externos, mejorar el fondo o centrar el grano.")

    cv2.putText(img_resultado, "OBJETO NO VALIDO", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

else:
    print("\nAnalisis finalizado correctamente.")
    print("Conclusion general: Se detecto al menos un grano valido y se evaluo su estado mediante area, perimetro, circularidad, color promedio y desviacion de color.")


# CREAR UNA SOLA IMAGEN CON TODO EL PROCESO Y VARIABLES ABAJO
panel = crear_panel_proceso(
    img,
    img_gray,
    img_filtro,
    img_gauss,
    img_bordes,
    img_bin,
    img_limpia,
    img_resultado,
    ultimo_estado,
    ultima_area,
    ultimo_perimetro,
    ultima_circularidad,
    ultimo_color_promedio,
    ultima_desviacion_color,
    total_granos,
    granos_validos,
    objetos_no_validos
)

cv2.imshow("PROCESO COMPLETO DEL ANALISIS", panel)

cv2.waitKey(0)
cv2.destroyAllWindows()