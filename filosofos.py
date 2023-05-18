import threading, time, random

class Filosofo(threading.Thread):
    pensando = 0
    comiendo = 1
    def __init__(self, nombre, tenedorIZQ, tenedorDER, max_comidas):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.tenedorIZQ = tenedorIZQ
        self.tenedorDER = tenedorDER
        self.comidas = 0
        self.comidas_max = max_comidas
        
    def run(self):
        while self.comidas < self.comidas_max:
            self.pensar()
            self.coger_tenedores()
            self.comer_Filosofo()
            self.soltar_tenedores()
            
        
            
    def pensar(self):
        print(f'{self.nombre} está pensando')
        time.sleep(random.randint(1,5))
                
    def coger_tenedores(self):
        tenedorIZQ = self.tenedorIZQ
        tenedorDER =  self.tenedorDER    
        while True:
            tenedorIZQ.acquire()
            locked = tenedorDER.acquire(False)
            if locked: 
                break
            tenedorIZQ.release()
            print(f'{self.nombre} está esperando los tenedores')
            tenedorIZQ, tenedorDER = tenedorDER, tenedorIZQ
            
    
    def soltar_tenedores(self):
        self.tenedorIZQ.release()
        self.tenedorDER.release()
            
        

        
    def comer_Filosofo(self):
        print(f'{self.nombre} está comiendo')
        time.sleep(random.randint(1,5))
        self.comidas += 1
        
    

def main():
    num_filosofos = 5
    max_comidas = 4
    tenedores = [threading.Lock() for n in range(num_filosofos)]
    filosofos = [Filosofo(f'Filosofo {n}', tenedores[n%num_filosofos], tenedores[(n+1)%num_filosofos], max_comidas) 
                 for n in range(num_filosofos)]
        
    for filosofo in filosofos:
        filosofo.start()
        
    for filosofo in filosofos:
        filosofo.join()
        
    
if __name__ == '__main__':
    main()
    

        