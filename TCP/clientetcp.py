from socket import *
NomSer = '127.0.0.1'
PueSer = 12000
CliSock = socket(AF_INET, SOCK_STREAM)
CliSock.connect((NomSer, PueSer))
mensaje = input('Introduce un mensaje: ')
CliSock.send(bytes(mensaje, 'utf-8'))
mensajeMayu = CliSock.recv(1024)
print(mensajeMayu.decode('utf-8'))
CliSock.close()
