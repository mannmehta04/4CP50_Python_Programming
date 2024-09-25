import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("Server is listening...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()
    print(f"Client says: {message}")

    if message.lower() == "bye":
        print("Client ended the conversation.")
        break

    reply = input("Enter reply: ")
    server_socket.sendto(reply.encode(), client_address)

    if reply.lower() == "bye":
        print("Server ended the conversation.")
        break

server_socket.close()