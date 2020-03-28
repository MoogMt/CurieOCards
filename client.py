#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:17:52 2020

@author: moogmt

# Inspired by the the tutorial on python at:
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/234698-gerez-les-reseaux
"""

import socket

hote = "localhost"
port = int( input("Enter the port to connect to: ") )

connexion_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
check = True
try:
    connexion_server.connect((hote, port))
except socket.error:
    print("Error in connexion")
    check = False
    pass

if check:
    print("Connexion établie avec le serveur ", str(hote) ,"sur le port ", str(port) )
    msg_to_send = ""
    while msg_to_send != str("end"):
        msg_to_send = str(input("> "))
        # Peut planter si vous tapez des caractères spéciaux
        msg_to_send = msg_to_send.encode()
        # On envoie le message
        connexion_server.send( msg_to_send )
        msg_recu = connexion_server.recv(1024)
        
        print( msg_recu.decode() ) # Là encore, peut planter s'il y a des accents

    print("Fermeture de la connexion")
    connexion_server.close()