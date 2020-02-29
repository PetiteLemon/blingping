import socket
from client import protocolclient


class TcpClient(protocolclient.ProtocolClient):
    def __init__(self, host, port, packet_size, timeout):
        super().__init__(host, port, packet_size, timeout)
        # TODO handle failed pings (try-except)

    def _create_socket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self._host, self._port))

    def send_on_socket(self, message):
        self.socket.sendall(message.encode())

    def receive_on_socket(self):
        return self.socket.recv(self._packet_size)
