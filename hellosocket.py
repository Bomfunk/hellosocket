import socket
import datetime


def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)

    print(f"Server listening on port {port}...")

    while True:
        client_socket, client_address = server_socket.accept()

        print(f"Connection from {client_address}")

        message = datetime.datetime.now().\
            strftime("Hello world! v1.3.0 %Y-%m-%d %H:%M:%S\n")
        client_socket.send(message.encode("utf-8"))

        client_socket.close()


if __name__ == "__main__":
    port_number = 12345
    start_server(port_number)
