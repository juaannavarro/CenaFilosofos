import threading

class Filosofo():
    def __init__(self, nombre, tenedorIZQ, tenedorDER):
        self.nombre = nombre
        self.tenedorIZQ = tenedorIZQ
        self.tenedorDER = tenedorDER
        
    def run(self):
        while True:
            self.comer()
            self.pensar()
            
    def pensar(self):
        print(self.nombre, "está pensando")
        
    def comer(self):
        print(self.nombre, "está comiendo")
        
    def solucion(self):
        tenedor1 = self.tenedorIZQ
        tenedor2 = self.tenedorDER
        while True:
            tenedor1.acquire()
            locked = tenedor2.acquire(False)
            if locked:
                break
            tenedor1.release()
            print(self.nombre, "intercambia tenedores")
            tenedor1, tenedor2 = tenedor2, tenedor1
        
        
    

        