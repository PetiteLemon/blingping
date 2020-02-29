import socket
import logging


class TcpServer:
    def __init__(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            logging.info('TCP server Binds to: {}'.format((host, port)))
            s.listen()
            conn, addr = s.accept()
            logging.info('TCP server accepted connection with: {}'.format(addr))
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
