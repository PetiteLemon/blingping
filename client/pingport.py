import logging
import time
from client import udpclient, tcpclient


class PingPort:
    def __init__(self, **kwargs):
        logging.debug("kwargs:{}".format(kwargs))
        self._kwargs = kwargs

        self._message = self.__set_attribute("message", 'bling ping')
        self._sleep_between_pings = self.__set_attribute("sleep_between_pings", 1)
        self._choose_protocol()
        self._stopped = False

    def _choose_protocol(self):
        protocol_name = self.__set_attribute("protocol", "tcp")
        self._protocol = {"tcp": tcpclient.TcpClient, "udp": udpclient.UdpClient}[protocol_name]
        self._protocol = self._protocol(
            host=self.__set_attribute("host", "localhost"),
            port=self.__set_attribute("port", 9123),
            packet_size=self.__set_attribute("packetSize", 1024),
            timeout=self.__set_attribute("timeout", 20))

    def start(self):
        while not self._stopped:
            self._protocol.send_on_socket(message=self._message)
            received = self._protocol.receive_on_socket()
            if received:
                logging.info("ping:{}".format(received))
            else:
                logging.info("ping FAIL")
            time.sleep(self._sleep_between_pings)

    def stop(self):
        self._stopped = True
        self._protocol.stop()

    def __set_attribute(self, key, default):
        return default if key not in self._kwargs else self._kwargs[key]