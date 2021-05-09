#!/usr/bin/env python3

import requests as req
import json
import time
import random
import serial
from datetime import datetime

url = 'https://www.barbora.lt/api/eshop/v1/cart/deliveries'
headers = {
    'Authorization': '',
    'Cookie': ''
}

def main():
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    while True:
        response = req.get(url = url, headers=headers)
        parsedJson = json.loads(response.text)
        try:
            days = parsedJson['deliveries'][0]['params']['matrix']
        except:
            print(parsedJson)
            continue
        freeSpot = False;

        for day in days:
            hours = day['hours']
            for hour in hours:
                available = hour['available']
                if available == True:
                    freeSpot = True
                    print(hour['deliveryTime'])

        print(datetime.now().strftime("%H:%M:%S"), ' ', freeSpot)
        print()
        arduino.write(("1" if freeSpot else "0").encode())
        time.sleep(random.randint(25, 59))


if __name__ == '__main__':
    main()

