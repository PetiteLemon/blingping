import socket
import logging


class UdpServer:
    def __init__(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((host, port))
            logging.debug("Udp socket bind to: {}/{}".format(host, port))
            while True:
                data, peer = s.recvfrom(1024)
                logging.debug("got: {} from: {}".format(data, peer))
                s.sendto(data, peer)
                logging.debug("sent back")
