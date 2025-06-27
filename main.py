import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Servidor UDP escuchando en el puerto {UDP_PORT}...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Mensaje recibido de {addr}: {data.decode()}")
