from socket import *
PueSer = 12000
SerSock = socket(AF_INET, SOCK_STREAM)
SerSock.bind(('', PueSer))
SerSock.listen(1)
print('Bienvenido al servidor de josema')
while True:
    socketConex, clienteDir = SerSock.accept()
    mensaje = socketConex.recv(1024)
    mensajeMay = mensaje.upper()
    socketConex.send(mensajeMay)
    socketConex.close()
