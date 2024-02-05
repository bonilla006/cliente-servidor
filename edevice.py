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
limit_edevice = 15

def main():
    #for i in range(limit_edevice):
    while True:
        num = random.choice([1,2,3,4,5,6,7,8,9])
        sender(int(sys.argv[1]), num)
        
        #recibe comunicacion del serv
        time.sleep(random.choice([1,2,3,4,5])) 


def sender(id, rand_num):
    pack = "%s:%s" %(id,rand_num)

    #se encarga de mandar el (id,rand#)
    UDP_IP = "localhost" #ip donde se va dar la comunicacion (local)
    UDP_PORT = 8080 #puerto de comunicacion

    #establcer conexion usando UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    
    #envia la data al servidor
    pack_ = pack.encode('utf-8')#convierte el mensaje en binario
    sock.sendto(pack_, (UDP_IP, UDP_PORT))

if __name__ == "__main__":
    main()
