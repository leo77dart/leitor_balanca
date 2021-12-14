import keyboard
import serial
import sys

ser = serial.Serial()

try:
    ser.port = sys.argv[1]
    ser.baudrate = int(sys.argv[2])
    ser.timeout = int(sys.argv[3])
    peso_definido = int(sys.argv[4])
    ser.open()
except:
    print('Argumentos inválidos')
else:
    peso_balanca = 0

    while(peso_definido != peso_balanca):

        if keyboard.is_pressed("s"):
            break

        peso_balanca = int.from_bytes(ser.read(10), byteorder='big') / 10
        print(peso_balanca)

    ser.close()


