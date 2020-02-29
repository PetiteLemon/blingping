import logging
import socket
from client import protocolclient


class UdpClient(protocolclient.ProtocolClient):
    def __init__(self, host, port, packet_size, timeout):
        super().__init__(host, port, packet_size, timeout)

    def _create_socket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.connect((self._host, self._port))

    def send_on_socket(self, message):
        self.socket.send(message.encode())

    def receive_on_socket(self):
        try:
            return self.socket.recvfrom(self._packet_size)
        except Exception as e:
            logging.debug("failed to rec from socket: {}".format(e))
            return