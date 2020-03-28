#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:17:52 2020

@author: moogmt

# Inspired by the the tutorial on python at:
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/234698-gerez-les-reseaux
"""

import socket
import select
import sys

host = str( input("Enter the host IP: ") )
port = int( input("Enter the port to listen to: ") )

connexion_nb = int( input("Maximum number of connexions: ") )
if connexion_nb < 1:
    connexion_nb = 5

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
#server.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
server.bind( ( host, port) )
socks = [server]
server.listen( connexion_nb )
devices={}

print("Server is listening on port: {}".format( port ) )

serveur_on = True # handle the status of the server
connected_clients = [] # contains the ids of the connected clients
time_wait = 0.05 # in seconds

clients_names = []
while serveur_on:
    # Listening for connexion demands from clients
    # We are listening to main conection in lecture mode, listening a maximum of timing
    asked_connexions, wlist, xlist = select.select( socks, [], [], time_wait )
    # Looping over connexions
    for connexion in asked_connexions:
        client_connexion, connexion_data = connexion.accept()
        # On ajoute le socket connecté à la liste des clients
        connected_clients.append( client_connexion )
    
    # Looping over connexions
    clients_to_read = []
    check = True
    try:
        clients_to_read, wlist, xlist = select.select( connected_clients, [], [], time_wait )
        for client in clients_to_read:
            # Receiving client name
            client_name = client.recv( 1024 ).decode( )
            print("New connexion, client name: ", client_name )
            
            # Confirming reception
            client.send( str( "Ok" ).encode() )
            # Confirming Username
            client.send( str( "Username: " + client_name ).encode() )
            # Registering username
            clients_to_read.append( client_name )
            
            # Message
            msg_received = client.recv( 1024 ).decode( )
            
            # If receive End, then stop the server
            if msg_received == "End":
                serveur_on = False
    except select.error:
        print("Server error: client connexion error.")


print("Closing connexion")
for client in connected_clients:
    client.close()

server.close()

sys.exit(0)