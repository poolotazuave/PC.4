# EJERCICIO NUMERO 2 DE PC4
import random
from pyfiglet import Figlet

# Obtener la lista de fuentes disponibles
fuentes_disponibles = Figlet().getFonts()

# Solicitar al usuario el nombre de una fuente o seleccionar una aleatoria
fuente_seleccionada = input("Ingrese el nombre de una fuente o deje en blanco para seleccionar una aleatoria: ")
if not fuente_seleccionada:
    fuente_seleccionada = random.choice(fuentes_disponibles)

# Crear una instancia de Figlet con la fuente seleccionada
figlet = Figlet(font=fuente_seleccionada)

# Solicitar al usuario el texto a imprimir
texto_imprimir = input("Ingrese el texto a imprimir: ")

# Imprimir el texto utilizando la fuente seleccionada
print(figlet.renderText(texto_imprimir))
