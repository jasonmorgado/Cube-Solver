"""
This is a script used to test the Python -> Arduino functionality.
Make sure the associated Arduino script PortTest/PortTest.ino is uploaded onto the Arduino AND
It's still connected with the cable BEFORE running this script.

Once this script is running, type a number into the command line and the
Arduino's LED should light up for that many seconds.
"""
import serial
import time

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    num = input("Enter a number: ")
    value = write_read(num)
    print(value)
