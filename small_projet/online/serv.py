#!/usr/bin/python
# -*-coding:utf-8 -*

import socket
import time

connection_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection_principale.bind(('', 12800))
connection_principale.listen(5)

connection_client, infos_connection = connection_principale.accept()

while 1:
    if not infos_connection == None:
        print(infos_connection)
    time.sleep(2)