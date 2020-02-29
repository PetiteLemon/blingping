# blingping
client-server python script for "ping" over TCP or UDP.

# mission description
the original ping uses ICMP protocol to get IP end-points. It's not that useful though when:
  a. There's no actual NAT, but only proxy (therefore the last mile for ping would
  only be the proxy server and not the actual server behind).
  b. We want to check the firewall settings by testing the target TCP/UDP port,
  and not only by its IP.

This script is built from a client side and a server side.
The client should support several configurations such as protocol, timeout, packet-size and etc.

# assumptions
1. socket is write-ready always, as we have ethernet connection in mide, as opposed to modems.
  this effects the design in server handleing of messages, when reciveing a new message we ovveride the last one.

# credits
Originator: Roee Kashi
Code and design review: Yoav Marom
