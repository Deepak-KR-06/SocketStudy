import socket

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)

print("Server waiting for client...")

c, addr = s.accept()
print("Client connected:", addr)

while True:
    msg = input("Enter a message: ")

    if msg.lower() == "exit":
        break

    c.send(msg.encode())

    ack = c.recv(1024).decode()
    print("Client ACK:", ack)

c.close()
s.close()