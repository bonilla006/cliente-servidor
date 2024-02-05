import sys
import random
import socket
import time
'''
referencias:
https://machinelearningmastery.com/command-line-arguments-for-your-python-script/
https://www.geeksforgeeks.org/random-numbers-in-python/
https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
->So bytes can do much more than just encode a string. It's Pythonic that it would allow you to call the constructor with any type of source parameter that makes sense.
For encoding a string, I think that some_string.encode(encoding) is more Pythonic than using the constructor
'''
x = 0
limit_edevice = 15
UDP_IP = "localhost" #ip donde se va dar la comunicacion (local)
UDP_PORT = 8080 #puerto de comunicacion
UDP_PORT_n = 8081

def main():
    #for i in range(limit_edevice):
    boolin = False
    while True:
        num = random.choice([1,2,3,4,5]) #tiempo para dormir, ,3,4,5,6,7,8,9
        
        #if else,
        #corre primero el else pq por default va ser falso
        #luego corre la segunda vez,cada que el serv le responda
        if boolin:
            sender(int(sys.argv[1]), num)
        else:
            sender(int(sys.argv[1]), num)
        
        #recibe comunicacion del serv
        #funcion
        boolin = n_sender()


def sender(id, rand_num):
    #mensaje que se va a enviar
    pack = "%s:%s" %(id,rand_num)
    #establcer conexion usando UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    pack_ = pack.encode('utf-8')#convierte el mensaje en binario
    sock.sendto(pack_, (UDP_IP, UDP_PORT))

def n_sender():
    #establece conexion con el serv
    sock_n = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_n.bind((UDP_IP, UDP_PORT_n))
    data = sock_n.recv(1024).decode('utf-8')
    if data == "next":
        print("...")
        return True

if __name__ == "__main__":
    main()