#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:17:52 2020

@author: moogmt

# Inspired by the the tutorial on python at:
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/234698-gerez-les-reseaux
"""

import socket

hote = str( input("Enter the IP to connect to: ") )
port = int( input("Enter the port to connect to: ") )

connexion_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
check = True
try:
    connexion_server.connect((hote, port))
    print("Connexion established with the server ", str(hote) ," on port ", str(port) )
    msg_to_send = ""
    while msg_to_send != "End":
        # Reading message
        msg_to_send = str(input("> "))
        if msg_to_send == "" :
            continue
        if msg_to_send == "End" :
            print("Closing connexion, goodbye!")
            connexion_server.send( str("End").encode() )
            connexion_server.close()
            break
        # Sending message 
        connexion_server.send( msg_to_send.encode() )
        # Getting the answer
        msg_received = connexion_server.recv(1024).decode()
        if msg_received != "Ok" :
            print("Server shutdown: Communication issue.")
            connexion_server.close()
            break
except socket.error:
    print("Connexion could not be established. Check host and/or port.")
