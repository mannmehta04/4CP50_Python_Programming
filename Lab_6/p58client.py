import socket

def client_program():
    host = socket.gethostname()
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter message to send to server: ")
        client_socket.send(message.encode())

        if message.lower() == 'bye':
            break

        data = client_socket.recv(1024).decode()
        print(f"Received from server: {data}")

    client_socket.close()


if __name__ == '__main__':
    client_program()