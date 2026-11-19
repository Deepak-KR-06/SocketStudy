import socket

s = socket.socket()
s.connect(('localhost', 8000))

print("Connected to server")

while True:
    msg = s.recv(1024).decode()

    if not msg:
        break

    print("Message from server:", msg)

    s.send("ACK: Message received".encode())

s.close()