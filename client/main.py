import time
import logging
import threading
from client import pingport
from common import config


if __name__ == '__main__':
    logging.basicConfig(format=config.FORMAT_LOG, level=config.LEVEL_LOG)
    logging.info("hi im client")
    ping = pingport.PingPort(host="localhost",
                             port=65432,
                             protocol="udp",
                             timeout=18)
    TIMED = False

    if TIMED:
        x = threading.Timer(0, ping.start)
        x.start()
        time.sleep(4)
        ping.stop()
        x.join()
    else:
        x = threading.Timer(0, ping.start)
        x.start()

# TODO expose params to command line
