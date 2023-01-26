from socket import *
PueSer = 23000
SerSock = socket(AF_INET, SOCK_DGRAM)
SerSock.bind(('', PueSer))
print('Bienvenido al servidor de josema')
while True:
    mensaje, CliDir = SerSock.recvfrom(2048)
    mensajeMayuscula = mensaje.upper()
    SerSock.sendto(mensajeMayuscula, CliDir)
