import serial

class Leitor:

    def __init__(self, port, baudrate, timeout) -> None:
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.peso = 0
        self.peso_balanca = 0

    def exec(self, peso):

        self.peso = peso
        ser = serial.Serial()

        ser.port = self.port
        ser.baudrate = self.baudrate
        ser.timeout = self.timeout
        ser.open()

        while(self.peso != self.peso_balanca):
            self.peso_balanca = int.from_bytes(ser.read(10), byteorder='big')
            # x = self.peso - self.peso_balanca 
            # print("Balança", self.peso_balanca)
            # print("Fórmula", self.peso)
            # print("Diferença", x)

        # print("Peso está correto")
        ser.close()


