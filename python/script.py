import serial
import requests

arduino = serial.Serial('COM13', 9600)

humidity_api_url = 'http://127.0.0.1:8001/api/humidity-data/'
celsius_api_url = 'http://127.0.0.1:8001/api/celsius-data/'
fahrenheit_api_url = 'http://127.0.0.1:8001/api/fahrenheit-data/'
hic_api_url = 'http://127.0.0.1:8001/api/hic-data/'
hif_api_url = 'http://127.0.0.1:8001/api/hif-data/'

try:
    while True:
        data = arduino.readline()
        decoded_data = data.decode().strip()
        values = decoded_data.split(',')

        if len(values) >= 5:
            humidity, celsius, fahrenheit, hic, hif = map(float, values)

            humidity_data = {'humidity': humidity}
            celsius_data = {'celsius': celsius}
            fahrenheit_data = {'fahrenheit': fahrenheit}
            hic_data = {'hic': hic}
            hif_data = {'hif': hif}

            humidity_response = requests.post(humidity_api_url, json=humidity_data)
            celsius_response = requests.post(celsius_api_url, json=celsius_data)
            fahrenheit_response = requests.post(fahrenheit_api_url, json=fahrenheit_data)
            hic_response = requests.post(hic_api_url, json=hic_data)
            hif_response = requests.post(hif_api_url, json=hif_data)

            if humidity_response.status_code == 201:
                print(f"Humidity data sent: {humidity_data}")
            else:
                print(f"Failed to send humidity data. Server status code: {humidity_response.status_code}")

            if celsius_response.status_code == 201:
                print(f"Celsius data sent: {celsius_data}")
            else:
                print(f"Failed to send Celsius data. Server status code: {celsius_response.status_code}")

            if fahrenheit_response.status_code == 201:
                print(f"Fahrenheit data sent: {fahrenheit_data}")
            else:
                print(f"Failed to send Fahrenheit data. Server status code: {fahrenheit_response.status_code}")

            if hic_response.status_code == 201:
                print(f"HIC data sent: {hic_data}")
            else:
                print(f"Failed to send HIC data. Server status code: {hic_response.status_code}")

            if hif_response.status_code == 201:
                print(f"HIF data sent: {hif_data}")
            else:
                print(f"Failed to send HIF data. Server status code: {hif_response.status_code}")

except KeyboardInterrupt:
    arduino.close()
