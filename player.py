#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 00:49:44 2020

@author: moogmt
"""

class Player:
    """
    Class defining a game server
        -> username : username of the player
        -> ip_adr : IP adress of the player
    """
    
    # Builder
    def __init__( self, username, ip ) :
        self.username = username
        self.ip_adr = ip
        return
        
    # Accessors methods
    def get_username( self ):
        """Method that returns the color"""
        return self.username
    def get_ip( self ):
        """Method that returns the shape'"""
        return self.ip_adr
    def get_all( self ):
        """Method that returns all informations"""
        return self.username, self.ip_adr
    
    # Modifyers
    def set_username( self, new_username ):
        """Method that modifies username of the user"""
        self.username = new_username
        return
    def set_ip( self, new_ip ):
        """Method that modifies IP of the user"""
        self.ip_adr = new_ip
        return
    def set_all( self, new_username, new_ip ):
        self.set_username( new_username )
        self.set_ip( new_ip )
        return

    def print_username( self ):
        print( "username: "+ str( self.get_username() ) + ";" )
        return
    def print_ip( self ):
        print("ip adress: " + str( self.get_ip() ) )
        return
    def print_all( self ):
        print( "username: " + str(self.get_username())+"; ip: " + str(self.get_ip()) + ";" )
        return
    
    