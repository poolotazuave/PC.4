# EJERCICIO NUMERO 1 DE PC4
import requests

def obtener_precio_bitcoin():
    try:
        # Consultar la API de CoinDesk para obtener el precio actual de Bitcoin
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Verificar si hubo un error en la solicitud HTTP
        
        # Analizar la respuesta JSON
        data = response.json()
        
        # Obtener el precio de Bitcoin en USD
        precio_bitcoin_usd = float(data["bpi"]["USD"]["rate"].replace(",", ""))
        
        return precio_bitcoin_usd
    except requests.RequestException as e:
        print("Error al consultar la API de CoinDesk:", e)
        return None

def main():
    # Solicitar al usuario la cantidad de Bitcoins que posee
    try:
        cantidad_bitcoins = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")
        return
    
    # Obtener el precio actual de Bitcoin en USD
    precio_bitcoin_usd = obtener_precio_bitcoin()
    
    if precio_bitcoin_usd is not None:
        # Calcular el costo actual de "n" Bitcoins en USD
        costo_actual_usd = cantidad_bitcoins * precio_bitcoin_usd
        
        # Mostrar el costo actual con cuatro decimales y separador de miles
        print(f"El costo actual de {cantidad_bitcoins:.4f} Bitcoins es ${costo_actual_usd:,.4f} USD.")

if __name__ == "__main__":
    main()




