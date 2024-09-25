import socket

def server_program():
    host = socket.gethostname()
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, address = server_socket.accept()
    print(f"Connection from: {address}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received from client: {data}")
        response = input("Enter response to client: ")
        conn.send(response.encode())

    conn.close()


if __name__ == '__main__':
    server_program()