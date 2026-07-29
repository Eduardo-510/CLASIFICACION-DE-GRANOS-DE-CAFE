# PROYECTO: CLASIFICACION DE CALIDAD DE GRANOS DE CAFE
# ESP32-CAM + PYTHON + OPENCV

# PARTE 5: CONEXION Y CAPTURA DE IMAGEN DESDE LA ESP32-CAM
# El programa se conecta a la IP de la camara y captura una foto.
# Si hay error de conexion, realiza varios intentos.
# =============================================================

url = "http://172.20.10.10/capture"

print("Capturando imagen desde ESP32-CAM...")

img = None

for intento in range(1, 6):
    try:
        print("Intento de captura:", intento)

        # Se solicita una imagen a la ESP32-CAM mediante la ruta /capture.
        respuesta = requests.get(url, timeout=15)

        if respuesta.status_code != 200:
            print("Error HTTP:", respuesta.status_code)
            time.sleep(1)
            continue

        # Se convierte la imagen recibida en bytes a formato OpenCV.
        img_array = np.frombuffer(respuesta.content, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if img is not None:
            print("Imagen capturada correctamente")
            break
        else:
            print("No se pudo decodificar la imagen")
            time.sleep(1)

    except requests.exceptions.ConnectTimeout:
        print("Error: No se pudo conectar con la ESP32-CAM.")
        print("Revisa que la IP sea correcta y que la laptop este en el mismo WiFi.")
        time.sleep(2)

    except requests.exceptions.ConnectionError:
        print("Error: La ESP32-CAM cerro o rechazo la conexion.")
        print("Cierra el navegador o el Start Stream y vuelve a intentar.")
        time.sleep(2)

    except requests.exceptions.Timeout:
        print("Error: Tiempo de espera agotado.")
        time.sleep(2)

    except Exception as e:
        print("Error inesperado:", e)
        time.sleep(2)

if img is None:
    print("\nNo se pudo obtener imagen desde la ESP32-CAM.")
    print("Verifica primero en el navegador:")
    print("http://172.20.10.10/capture")
    print("Si no carga ahi, el problema es conexion WiFi/IP, no el procesamiento.")
    exit()


# =============================================================
