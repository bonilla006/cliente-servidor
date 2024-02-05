Descripción:
Este programa realiza una conexión entre un cliente y un servidor mediante el protocolo UDP. 
-Edevice: python# edevice.py #
	*while true en el cual se va a mandar numeros random a la función sender. 
	*se realiza la conexión usando localhost y el puerto 8080. 
	*El mensaje se va a enviar a través de la variable pack_. 
	*después de enviar un (id,t_job), se irá a dormir un tiempo aleatorio
-Udp_serv: python# udp_serv.py #(puerto)
	*correr dos threads desde main, productor/consumidor. 
	*Tanto el productor como el consumidor estarán corriendo con un límite asignado. 
	*En el productor se realizará la función split para separar el mensaje en dos secciones, id/t_job, el cual será enviado al queue usando un tuple. 
	*Luego el productor se encargará de extraer el tuple del queue. 
		~También se realizará una suma de los valores según el id.

variaciones del bono:(edevice_n.py, udp_serv_bono.py)
-Una de las variaciones es que el productor estará siempre escuchando pero únicamente acabará cuando el consumidor acabe. flag_.set()
-También se estará mandando una alerta al edevice cada vez que se ejecute un trabajo el cual le indicará que puede enviar otro. función n_sender()

referencias:
>>>https://machinelearningmastery.com/command-line-arguments-for-your-python-script/
>>>https://www.geeksforgeeks.org/random-numbers-in-python/
>>>https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
	->So bytes can do much more than just encode a string. It's Pythonic that it would allow you to call the constructor with any type of source parameter that makes sense.
	For encoding a string, I think that some_string.encode(encoding) is more Pythonic than using the constructor
>>>https://www.educative.io/answers/learning-about-defaultdict-in-python
>>>https://superfastpython.com/thread-event-object-in-python/

colaboraciones:
Sergio 
Andres
Bernardo
Adriana




