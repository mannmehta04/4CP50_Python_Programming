import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)

while True:
    message = input("Enter message to server: ")
    client_socket.sendto(message.encode(), server_address)

    if message.lower() == "bye":
        print("Client ended the conversation.")
        break

    data, server = client_socket.recvfrom(1024)
    reply = data.decode()
    print(f"Server says: {reply}")

    if reply.lower() == "bye":
        print("Server ended the conversation.")
        break

client_socket.close()