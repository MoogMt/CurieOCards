#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:14:32 2020

@author: moogmt
"""

class Server:
    """
    Class defining a game server
        -> hostname: the IP of the server (default "localhost")
        -> port : port where the server listens
        -> nb_connexion : number of connexion that are available by the server
    """
    
    # Default values
    default_hostname = "localhost"
    default_port = 2002
    default_nb_connexion = 5
    
    # Builder
    def __init__( self, hostname=default_hostname, port=default_port, nb_connexion=default_nb_connexion ) :
        """Constructeur de notre classe"""
        self.hostname = hostname
        self.port = port
        self.nb_connexion = nb_connexion
        
    # Accessors methods
    def _get_hostname( self ):
        """Method that returns the hostname"""
        return self.hostname
    def _get_port( self ):
        """Method that returns the port of the server'"""
        return self.port
    def _get_nb_connexion( self ):
        """Method that returns the port of the server'"""
        return self.nb_conexion
    
    # Modifyers
    def _set_hostname( self, new_hostname ):
        """Method that modifies the hostname of the server"""
        self.hostname = new_hostname
        return
    def _set_port( self, new_port ):
        """Method that modifies the hostname of the server"""
        self.port = new_port
        return
    def _set_nb_connexion( self, new_nb_connexion ):
        """Method that modifies the hostname of the server"""
        self.port = new_nb_connexion
        return