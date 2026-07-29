# PROYECTO: CLASIFICACION DE CALIDAD DE GRANOS DE CAFE
# ESP32-CAM + PYTHON + OPENCV

# PARTE 10: RESUMEN FINAL Y VISUALIZACION DEL PANEL
# Se imprime la conclusion general y se muestra una ventana con
# todas las etapas del analisis.
# =============================================================

print("\nRESUMEN")
print("Cantidad de objetos detectados:", total_granos)
print("Cantidad de granos validos:", granos_validos)
print("Objetos no validos:", objetos_no_validos)

if ultimo_estado == "GRANO NO DETECTADO":
    print("Conclusion general: No se detecto ningun grano valido.")

elif ultimo_estado == "OBJETO NO VALIDO":
    print("Conclusion general: El objeto detectado no cumple las condiciones para ser considerado grano de cafe.")

elif ultimo_estado == "PARTIDO":
    print("Conclusion general: El grano presenta separacion, hendidura o forma partida.")

elif ultimo_estado == "INMADURO":
    print("Conclusion general: El grano presenta coloracion verde clara, posiblemente inmaduro o no tostado.")

else:
    print("Conclusion general: Se detecto un grano y se evaluo su estado.")

# Se crea y muestra el panel completo del proceso.
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
    ultima_solidez,
    ultimo_tono_h,
    ultima_saturacion_s,
    ultimo_brillo_v,
    total_granos,
    granos_validos,
    objetos_no_validos
)

cv2.imshow("PROCESO COMPLETO DEL ANALISIS", panel)

cv2.waitKey(0)
cv2.destroyAllWindows()
