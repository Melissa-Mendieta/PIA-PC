#!/usr/bin/python3

import socket
import argparse


def Encabezado(target,port):
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #sock.connect((params.target,params.port))
    sock.connect((target,port))
    sock.settimeout(2)

    targetBytes = target.encode()
    http_get = b"GET /index.html HTTP/1.1\r\nHost: "+targetBytes+b"\r\nAccept: */*\r\n\r\n"
    data = ''
    try:
        sock.sendall(http_get)
        data = sock.recvfrom(1024)
        print(data[0].decode())
    except socket.error:
        print("Socket error ",socket.errno)
    finally:
        print("Cerrando conexión")
        sock.close()