#EJERCICIO NUMERO 3 DE PC4
import requests

# URL de la imagen que deseas descargar
url_imagen = "https://unsplash.com/es/s/fotos/perrito"  # Reemplaza esta URL por la URL de la imagen que desees descargar

# Realizar una solicitud HTTP GET para obtener la imagen
response = requests.get(url_imagen)

# Verificar si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # Obtener el contenido de la imagen
    contenido_imagen = response.content
    
    # Especificar el nombre del archivo en el que deseas guardar la imagen
    nombre_archivo = "imagen_descargada.jpg"  # Puedes cambiar este nombre
    
    # Guardar la imagen en un archivo local
    with open(nombre_archivo, "wb") as archivo:
        archivo.write(contenido_imagen)
    print(f"Imagen descargada como '{nombre_archivo}'.")
else:
    print("No se pudo descargar la imagen. Código de respuesta:", response.status_code)
