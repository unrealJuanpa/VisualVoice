import socket

def obtener_direccion_ip():
    hostname = socket.gethostname()
    direccion_ip = socket.gethostbyname(hostname)
    return direccion_ip

# Ejemplo de uso
ip = obtener_direccion_ip()
print("Mi dirección IP es:", ip)
