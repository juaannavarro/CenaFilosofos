import threading

class Filosofo():
    def __init__(self, nombre, tenedorIZQ, tenedorDER):
        threading.Thread.__init__(self)
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
        tenedor1 = self.tenedorIZQ
        tenedor2 =  self.tenedorDER
        primero = tenedor1
        segundo = tenedor2     
        with primero:
            with segundo:
                self.comer_Filosofo()
        

        
    def comer_Filosofo(self):
        print(self.nombre, "está comiendo")
        
    
tenedor1 = threading.Lock()
tenedor2 = threading.Lock()
tenedor3 = threading.Lock()
tenedor4 = threading.Lock()
tenedor5 = threading.Lock()

filosofo1 = Filosofo("Sócrates", tenedor5, tenedor1)
filosofo2 = Filosofo("Platón", tenedor1, tenedor2)
filosofo3 = Filosofo("Aristóteles", tenedor2, tenedor3)
filosofo4 = Filosofo("Descartes", tenedor3, tenedor4)
filosofo5 = Filosofo("Kant", tenedor4, tenedor5)

filosofo1.run()
filosofo2.run()
filosofo3.run()
filosofo4.run()
filosofo5.run()
        
        
    

        