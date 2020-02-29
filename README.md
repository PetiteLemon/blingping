# blingping
client&amp;server for ping with ports, meant to test firewall

# original mission description
The mission is to build a client-server python script for "ping" over TCP or UDP(configurable).

Ping uses ICMP protocol to get IP end-points. It's not that useful though when:
  a. There's no actual NAT, but only proxy (therefore the last mile for ping would
  only be the proxy server and not the actual server behind).
  b. We want to check the firewall settings by testing the target TCP/UDP port,
  and not only by its IP.

The script is built from a client side and a server side.

The client should support several configurations such as protocol, timeout, packet-
size and etc.

mission credit: Roee Kashi
