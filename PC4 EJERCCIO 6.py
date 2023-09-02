#EJERCICIO NUMERO 6 PC4
import requests
import sqlite3
from datetime import datetime

# Obtener datos de precios de Bitcoin desde la API de CoinDesk
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()  # Verificar si hubo un error en la solicitud HTTP
    data = response.json()
    bitcoin_prices = data["bpi"]
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
except requests.RequestException as e:
    print("Error al consultar la API de CoinDesk:", e)
    bitcoin_prices = {}
    fecha_actual = None

# Crear una conexión a la base de datos SQLite
try:
    conn = sqlite3.connect("cryptos.db")
    cursor = conn.cursor()

    # Crear la tabla bitcoin si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin (
            id INTEGER PRIMARY KEY,
            fecha TEXT,
            precio_usd REAL,
            precio_gbp REAL,
            precio_eur REAL
        )
    ''')

    # Insertar los datos en la tabla
    cursor.execute('''
        INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur)
        VALUES (?, ?, ?, ?)
    ''', (fecha_actual, bitcoin_prices.get("USD", 0), bitcoin_prices.get("GBP", 0), bitcoin_prices.get("EUR", 0)))

    # Guardar los cambios en la base de datos
    conn.commit()
    print("Datos de Bitcoin almacenados en la base de datos cryptos.db")
except sqlite3.Error as e:
    print("Error al interactuar con la base de datos:", e)
finally:
    # Cerrar la conexión a la base de datos
    if conn:
        conn.close()
