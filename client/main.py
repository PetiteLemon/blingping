import logging
from client import pingport
from common import config

if __name__ == '__main__':
    logging.basicConfig(format=config.FORMAT_LOG, level=config.LEVEL_LOG)
    logging.info("hi im client")
    ping = pingport.PingPort(host="localhost",
                             port=65432,
                             protocol="udp",
                             timeout=18)
    ping.start()
