import math
import time
import serial

pesos = [105, 104, 103, 100]

while True:
    ser = serial.Serial('COM1')
    for p in pesos:
        t = math.ceil(p.bit_length() / 8)
        time.sleep(2)
        print(p)
        ser.write(p.to_bytes(t, byteorder='big'))
    ser.close()
