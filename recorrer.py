import os
import shutil

# def subir_archivos(ruta_origen, ruta_destino):
#     # Recorrer las carpetas en la ruta de origen
#     for carpeta in os.listdir(ruta_origen):
#         ruta_carpeta = os.path.join(ruta_origen, carpeta)
#         if os.path.isdir(ruta_carpeta):
#             # Recorrer los archivos dentro de la carpeta
#             for archivo in os.listdir(ruta_carpeta):
#                 ruta_archivo = os.path.join(ruta_carpeta, archivo)
               

# # Definir la ruta de origen y la ruta de destino
# ruta_origen = "/ruta/a/la/carpeta_principal"
# ruta_destino = "/ruta/destino"

# # Llamar a la función para subir los archivos
# subir_archivos(ruta_origen, ruta_destino)

for root, dirs, files in os.walk("./boxes-to-upload", True):
   for name in files:
           ruta = root + "/" + name
           ruta = ruta.replace("\\" , "/").strip("./")
           
           print(ruta)
           print(name)