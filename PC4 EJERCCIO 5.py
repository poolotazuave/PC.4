#EJERCICIO NUMERO 5 DE PC4
pip install requests
import requests
import csv

# Obtener datos de precios de Bitcoin desde la API de CoinDesk
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/historical/close.json")
    response.raise_for_status()  # Verificar si hubo un error en la solicitud HTTP
    data = response.json()
    bitcoin_prices = data["bpi"]
except requests.RequestException as e:
    print("Error al consultar la API de CoinDesk:", e)
    bitcoin_prices = {}

# Guardar los datos en un archivo TXT
try:
    with open("bitcoin_prices.txt", "w") as archivo_txt:
        for fecha, precio in bitcoin_prices.items():
            archivo_txt.write(f"{fecha}: {precio}\n")
    print("Datos de Bitcoin guardados en bitcoin_prices.txt")
except IOError as e:
    print("Error al guardar los datos en el archivo TXT:", e)

# Guardar los datos en un archivo CSV
try:
    with open("bitcoin_prices.csv", "w", newline="") as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(["Fecha", "Precio"])
        for fecha, precio in bitcoin_prices.items():
            escritor.writerow([fecha, precio])
    print("Datos de Bitcoin guardados en bitcoin_prices.csv")
except IOError as e:
    print("Error al guardar los datos en el archivo CSV:", e)

