

class ProtocolClient:
    def __init__(self, host, port, packet_size):
        self._socket = None
        self._host = host
        self._port = port
        self._packet_size = packet_size
        self._create_socket()

    @property
    def socket(self):
        if not self._socket:
            self._create_socket()
        return self._socket

    def _create_socket(self):
        raise NotImplemented

    def send_on_socket(self, message):
        raise NotImplemented

    def receive_on_socket(self):
        raise NotImplemented
