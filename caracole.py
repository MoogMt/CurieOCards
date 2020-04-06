#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:45:20 2020

@author: moogmt
"""

import cards
import player

# Get Point Values
#=============================================================================#
def getPointValue( card ):
    max_n_point = len( cards.standard_values )
    for i_val in range( max_n_point ):
        if cards.standard_values[i_val] == card.value:
            if i_val == 8:
                return 0
            elif i_val == 0 :
                return 1
            else:
                return max_n_point - i_val - 1
def getPointValueHand( hand ):
    points = 0
    for card in hand:
        points += getPointValue( card )
    return points
#=============================================================================#

#=============================================================================#
class CaracolePlayer( Player ):
    """
    Class defining a game server
        -> username : username of the player
        -> ip_adr : IP adress of the player
    """
    """
        Builder
    """
    def __init__( self, username, ip, hand ) :
        self.username = username
        self.ip_adr = ip
        self.hand = hand
        return
    """  
        Accessors methods
    """
    def get_hand( self ):
        """Method that returns the shape'"""
        return self.hand
    def get_pointValueHand( self ):
        """ Method get """
        return getPointValueHand( self.get_hand() )
    def get_all( self ):
        """Method that returns all informations"""
        return self.username, self.ip_adr, self.hand
    """
        Modifyers
    """
    def set_hand( self, new_hand ):
        """Method that modifies IP of the user"""
        self.hand = new_hand
        return
    def set_all( self, new_username, new_ip, new_hand ):
        self.set_username( new_username )
        self.set_ip( new_ip )
        self.set_hand( new_hand )
        return
    """
        Printers
    """
    def print_hand( self ):
        print("Cards: ")
        for card in self.hand: 
            card.print_all()
        return
    def print_all( self ):
        print("username: " + str(self.get_username())+"; ip: " + str(self.get_ip()) +  ";" )
        self.print_hand()
        return    
#=============================================================================#


n_cards_player = 7

def caracoleRound( n_players ):
    return

def caracoleGame( n_players, n_shuffle, n_deck, limit_point_loose ):
    deck = cards.initSeveralDecksWithJoker()
    if len(deck) >= n_cards_player*n_players:
        print( "The number of cards is not large enough for the number of players" )
        return False
    hands, deck = cards.dealCards( deck, n_players, n_cards_player )
    max_point=0
    # The Caracole lasts as long as no player reaches 100
    while max_point < limit_point_loose:
        player_points = caracoleRound( )
        max_point = max( player_points )
    # Determines who wins and looses
    winners, loosers = [], []
    for player in players:
        if getPointValueHand( player.get_hand() ) < limit_point_loose :
            winners.append( player.get_username() )
        else : 
            loosers.append( player.get_username() )
    return winners, loosers, players, points
