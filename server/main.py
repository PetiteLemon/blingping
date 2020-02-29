import socket
import logging
from common import config


def listenToTcp(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)



def listenToUdp(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        logging.debug("Udp socket bind to: {}/{}".format(host, port))
        while True:
            data, peer = s.recvfrom(1024)
            logging.debug("got: {} from: {}".format(peer, data))
            s.sendto(data, peer)
            logging.debug("sent back")


if __name__ == '__main__':
#    logLevel = logging.DEBUG
    logLevel = logging.INFO
    logging.basicConfig(format=config.FORMAT_LOG, level=config.LEVEL_LOG)
    logging.info("hi im server")
    HOST = '0.0.0.0'
    PORT = 65432
    listenToUdp(HOST, PORT)