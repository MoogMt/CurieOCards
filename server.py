#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:47:10 2020

@author: moogmt
"""

import socket
import select

hote = ''
port = int( input("Enter the port to listen to: ") )

connexion_principale = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
connexion_principale.bind( ( hote, port) )
connexion_principale.listen( 5 )

print("Server is listing on port: {}".format( port ) )

serveur_on = True # handle the status of the server
connected_clients = [] # contains the ids of the connected clients
time_wait = 0.05 # in seconds

while serveur_on:
    # Listening for connexion demands from clients
    # We are listening to main cnnection in lecture mode, listening a maximum of timing
    asked_connexions, wlist, xlist = select.select([connexion_principale], [], [], time_wait )
    # Looping over connexions
    for connexion in asked_connexions:
        client_connexion, connexion_data = connexion.accept()
        # On ajoute le socket connecté à la liste des clients
        connected_clients.append( client_connexion )
    
    # Maintenant, on écoute la liste des clients connectés
    # Les clients renvoyés par select sont ceux devant être lus (recv)
    # On attend là encore 50ms maximum
    # On enferme l'appel à select.select dans un bloc try
    # En effet, si la liste de clients connectés est vide, une exception
    # Peut être levée
    clients_to_read = []
    try:
        clients_to_read, wlist, xlist = select.select( connected_clients, [], [], time_wait )
    except select.error:
        pass
    
    # Going round the clients, checking for messages
    for client in clients_to_read:
            # The client is a socket
            msg_received = client.recv( 1024 )
            # May plant if special characters
            msg_received = msg_received.decode( )
            print("Received {}".format( msg_received ) )
            client.send(b"5 / 5")
            if msg_received == "end":
                serveur_on = False


print("Closing connexion")
for client in connected_clients:
    client.close()

connexion_principale.close()