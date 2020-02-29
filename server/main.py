import logging, select, socket
from common import config
from server import udpserver, tcpserver


def looper():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('0.0.0.0', 65432))

    udp_inputs = [udp_socket]
    udp_outputs = []
    udp_messages = {}
    while udp_inputs:
        readable, writable, exceptional = select.select(udp_inputs, udp_outputs, udp_inputs)
        for s in readable:
            logging.info("in readable")
            data, peer = s.recvfrom(1024)
            if data:
                udp_outputs.append(s)
                udp_messages.update({s: (data, peer)})
        for s in writable:
            if s in udp_outputs:
                message = udp_messages[s]
                logging.info("in writable:{}".format(message))
                s.sendto(message[0], message[1])
                udp_outputs.remove(s)
        for s in exceptional:
            logging.info("exception on: {}".format(s))
            udp_inputs.remove(s)
            if s in udp_outputs:
                udp_outputs.remove(s)
                del udp_messages[s]
            s.close()


# the only propose of select is to tell me if my next action (read, write) will block.
# so, Im only going into the "s in readable" if there is ALREADY a letter, so I know I wont be blocking.

# we assume that s is always writable, so imissidtly after getting a message in readable, it will pop out in writable
# on the sam iteration

'''
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            outputs.remove(s)
        else:
            s.send(next_msg)

    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
'''

if __name__ == '__main__':
    logging.basicConfig(format=config.FORMAT_LOG, level=config.LEVEL_LOG)
    logging.info("hi im server")
    looper()
    # udpserver.UdpServer('0.0.0.0', port=65432)
    # tcpserver.TcpServer('0.0.0.0', port=65432)

