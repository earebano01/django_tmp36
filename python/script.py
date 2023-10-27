import serial
import requests

arduino = serial.Serial('COM13', 9600)  
api_url = 'http://localhost:8000/api/temperature-data/'

try:
    while True:
        data = arduino.readline()
        decoded_data = data.decode().strip() 
        values = decoded_data.split(',')
        
        if len(values) >= 5:
            humidity, celsius, fahrenheit, hic, hif = map(float, values)
            dht11_data = {
                'humidity': humidity,
                'celsius': celsius,
                'fahrenheit': fahrenheit,
                'hic': hic,
                'hif': hif,
            }

            response = requests.post(api_url, json=dht11_data)

            if response.status_code == 201:
                print(f"Données envoyées : {dht11_data}")
            else:
                print(f"Échec de l'envoi. Code d'état du serveur : {response.status_code}")

except KeyboardInterrupt:
    arduino.close()
