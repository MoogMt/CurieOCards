#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:17:52 2020

@author: moogmt

# Inspired by the the tutorial on python at:
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/234698-gerez-les-reseaux
and
https://www.geeksforgeeks.org/simple-chat-room-using-python/
"""

import socket
import select
import sys
from _thread import *

host = str( input("Enter the host IP: ") )
if host == "" :
    host = "localhost"
port = int( input("Enter the port to listen to: ") )


connexion_nb = int( input("Maximum number of connexions: ") )
if connexion_nb < 1:
    connexion_nb = 5

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
server.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 ) # unsure about what this does...

server.bind( ( str(host), port ) )

socks = [server]
server.listen( connexion_nb )
devices={}

print("Server is listening on port: {}".format( port ) )

serveur_on = True # handle the status of the server
connected_clients = [] # contains the ids of the connected clients
time_wait = 0.05 # in seconds

while serveur_on:
    # Listening for connexion demands from clients
    # We are listening to main conection in lecture mode, listening a maximum of timing
    asked_connexions, wlist, xlist = select.select( socks, [], [], time_wait )
    # Looping over connexions
    for connexion in asked_connexions:
        client_connexion, client_addr = connexion.accept()
        # On ajoute le socket connecté à la liste des clients
        connected_clients.append( client_connexion )
    
    try:
        clients_to_read, wlist, xlist = select.select( connected_clients, [], [], time_wait )
        for client in clients_to_read:
            # Receiving client name
            client_name = str( client.recv( 1024 ).decode( ) )
            if client_name == "End" :
                print("Client interuption.")
                serveur_on = False
            else:
                print("New connexion, client name: "+client_name ) 
                # Confirming reception
                client.send( str( "Ok" ).encode() )
    except select.error:
        print("Server error: client connexion error.")


print("Closing client connexion")
for client in connected_clients:
    client.close()

server.close()

sys.exit(0)