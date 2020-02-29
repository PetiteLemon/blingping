import socket
from client import protocolclient


class UdpClient(protocolclient.ProtocolClient):
    def __init__(self, host, port, packet_size):
        super().__init__(host, port, packet_size)

    def _create_socket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.connect((self._host, self._port))

    def send_on_socket(self, message):
        self.socket.send(message.encode())

    def receive_on_socket(self):
        return self.socket.recvfrom(self._packet_size)
