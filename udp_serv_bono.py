from threading import Thread, Semaphore, Event
import socket
from collections import defaultdict, Counter, OrderedDict
import time
import sys
'''
https://superfastpython.com/thread-event-object-in-python/
'''
#Implementacion de Queue usando lista
#=====================================================================
class Queue:
    def __init__(self, size):
        #size logico
        self.size = size
        #size fisico
        self.queue = []
        
    
    #canitidad de elementos en el queue
    def len(self):
        return len(self.queue)
    
    #te dice si esta vacio
    def empty(self):
        #si no hay elementos en el queue
        return len(self.queue) == 0
    
    #te dice si esta lleno
    def full(self):
        #si back es igual a size es que no hay espacio
        return len(self.queue) == self.size
    
    #inserta un item al queue
    def push(self, item):
        #asegurarnos de que no este lleno
        if not self.full():
            #back incrementa y ese es el indice que se usa para 
            #representar el queue, A[b++]
            self.queue.append(item)
            #self.print_q()
    
    #remueve un elemento del queue y devuelve el item en front
    def pop(self):
        #asegurarnos de que no este vacio
        if not self.empty():
            #A[b--], 
            self.queue.sort(key = lambda x:x[1], reverse=True)
            val = self.queue[0]
            self.queue.pop(0)#usamos indice 0 para acceder al primer elemento
        return val

    #desplega los items
    def print_q(self):
        print("size f= ",len(self.queue), ", ", "size l= ", self.size)
        for i in range(len(self.queue)):
            print("p: ",self.queue[i])

#=====================================================================

UDP_IP = "localhost"
#comunicacion principal
UDP_PORT = int(sys.argv[1])

#comunicacion de respuesta
UDP_PORT_n = 8081

#almacena los trabajos
id_Tjob_q= Queue(25)
#evita la region critica
protector = Semaphore()

#proteje el queue
vacio = Semaphore(25) #representa los espacios disponibles = size del queue
lleno = Semaphore(0) #representa los espacios usados 

#el limite de iteraciones que va hacer el prod/cons
limit_ = 15

#indica al productor que el consumidor acabo
flag_ = Event()

def main():
    print("main")
    productor = Thread(target=servidor)
    consumidor = Thread(target=receptor)

    productor.start()
    consumidor.start()

    consumidor.join()    
    productor.join()
       
    print("fin de main")
    
def servidor():
    #establece la conecion
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #permite interactuar(ser visible) con el ip y puerto seleccionado
    sock.bind((UDP_IP, UDP_PORT))
    
    while not flag_.is_set():  
        data = sock.recv(1024).decode('utf-8')
        mensaje = data.split(':')
        
        time_l = (int(mensaje[0]),int(mensaje[1]))
        #mutex: pq se esta editanto el queue
        #si es 0 no se puede entrar a la region critica
        #entrando: 
        vacio.acquire() #quita un espacio
        protector.acquire()
        id_Tjob_q.push(time_l)
        protector.release()
        lleno.release()
        #saliendo:
        
def receptor():
    dicc_sum = defaultdict(int)
    mensaje = "next"

    #conexion nueva para responder a los edevice
    sock_n = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    pack_ = mensaje.encode('utf-8')

    for _ in range(limit_): 
        #mutex: se edita el queue
        lleno.acquire()
        protector.acquire()
        val = id_Tjob_q.pop()
        protector.release()
        vacio.release()
        #mutex
        
        #suma de valores por k
        if val[0] in dicc_sum:
            dicc_sum[val[0]] += val[1]
        else:
            dicc_sum[val[0]] =  val[1]

        time.sleep(dicc_sum[val[0]])#dicc_sum[k]

        #una vez que llegue aqui mandas el mensaje a edevice
        sock_n.sendto(pack_, (UDP_IP, UDP_PORT_n))
    
    #si se acaba el for loop, es que el consumer completo su limite
    #entonces se cambia el flag para acabar el while del producer
    flag_.set() #true
    
    #se printea la informacion dentro del diccionario
    for i in dicc_sum:  
        print("Device", i,"consumed", dicc_sum[i], "seconds of CPU time")

    #si el queue esta lleno pero el productor
    #termino el trabajo, desbloquea el vacio
    #ya que si no se tranca en el semaforo
    #del productor
    if flag_.is_set():
        vacio.release()
    
    
   
    
if __name__ == "__main__":
    main()