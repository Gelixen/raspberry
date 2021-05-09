import serial
import csv
from datetime import datetime

#change ACM number as found from ls /dev/tty/ACM*
ser=serial.Serial("/dev/ttyACM0", 9600)

while True:
    read_ser=ser.readline().strip().decode("utf-8").split("\t")
    read_ser.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(read_ser)
    with open('temps.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(read_ser)
