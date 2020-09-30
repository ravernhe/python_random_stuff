#!/usr/bin/python
# -*-coding:utf-8 -*

import socket

connection_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_serv.connect(('localhost', 12800))