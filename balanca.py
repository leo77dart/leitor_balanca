import math
import time
import serial

ser = serial.Serial('COM1')

pesos = [105, 104, 103, 100]

for p in pesos:
    t = math.ceil(p.bit_length() / 8)
    time.sleep(5)
    print(p)
    ser.write(p.to_bytes(t, byteorder='big'))

ser.close()
