import logging, select, socket
from common import config


def looper():
    udps = create_udp_sockets()
    tcps = create_tcp_sockets()
    tcp_connections = {}

    while True:
        keys = [*udps] + [*tcps] + [*tcp_connections]
        readable, writable, exceptional = select.select(keys, keys, keys)

        handle_udps(udps, readable, writable, exceptional)
        handle_tcps(tcps, tcp_connections, readable, writable, exceptional)
        handle_tcp_connections(tcp_connections, readable, writable, exceptional)


def create_udp_sockets():
    udps = {}
    for port in range(65400, 65500):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind(('0.0.0.0', port))
        udps[udp_socket] = None
    return udps


def create_tcp_sockets():
    tcps = {}
    for port in range(65400, 65500):
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.setblocking(False)
        tcp_socket.bind(('0.0.0.0', port))
        tcp_socket.listen()
        tcps[tcp_socket] = None
    return tcps


def handle_udps(udps, readable, writable, exceptional):
    keys_to_remove = []
    for s in udps:
        if s in readable:
            data, peer = s.recvfrom(1024)
            logging.info("reading udp:{}".format(data, peer))
            udps[s] = {"data": data, "peer": peer}
        if s in writable and udps[s]:
            message = udps[s]
            s.sendto(message["data"], message["peer"])
            udps[s] = None
        if s in exceptional:
            logging.exception("exception on udp: {}".format(s))
            keys_to_remove.append(s)
            s.close()  # TODO do we want to close the udp socket ?

    for k in keys_to_remove:
        del udps[k]


def handle_tcps(tcps, tcp_connections, readable, writable, exceptional):
    keys_to_remove = []
    for s in tcps:
        if s in readable:
            connection, client_address = s.accept()
            connection.setblocking(False)
            tcp_connections[connection] = None
            logging.info("tcp accepting client:{}".format(client_address))
        if s in writable:
            pass
        if s in exceptional:
            logging.exception("exception on tcp: {}".format(s))
            keys_to_remove.append(s)
            s.close()

    for k in keys_to_remove:
        del tcp_connections[k]


def handle_tcp_connections(tcp_connections, readable, writable, exceptional):
    keys_to_remove = []
    for s in tcp_connections:
        if s in readable:
            data = s.recv(1024)
            if data:
                tcp_connections[s] = data
            else:
                logging.info("removing tcp_connections: {}".format(s))
                tcp_connections[s] = None
                keys_to_remove.append(s)
                s.close()

        if s in writable and tcp_connections.get(s):
            logging.info("writing to tcp_connections:{}".format(tcp_connections[s]))
            s.send(tcp_connections[s])
            tcp_connections[s] = None
        if s in exceptional:
            logging.info("exception on tcp_connections: {}".format(s))
            keys_to_remove.append(s)
            s.close()

    for k in keys_to_remove:
        del tcp_connections[k]


if __name__ == '__main__':
    logging.basicConfig(format=config.FORMAT_LOG, level=config.LEVEL_LOG)
    logging.info("hi im server")
    looper()
