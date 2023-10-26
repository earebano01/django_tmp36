import serial
import requests

arduino = serial.Serial('COM13', 9600)  

api_url = 'http://localhost:8000/api/temperature-data/'

try:
    while True:
        data = arduino.readline().decode().strip()
        temperature = float(data)

        temperature_data = {
            'temperature': temperature,
        }

        response = requests.post(api_url, data=temperature_data)

        if response.status_code == 201:
            print(f"Data sent to Django: {temperature_data}")
        else:
            print(f"Failed to send data to Django: {response.status_code}")

except KeyboardInterrupt:
    arduino.close()

