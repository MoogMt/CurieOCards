#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 00:49:44 2020

@author: moogmt
"""

import random

# Limitations values
accepted_colors = ["black","red","none"]
accepted_shapes = ["trefle","pique","carreau","coeur","atout","joker"]
accepted_values = ["As","Roi","Dame","Cavalier","Valet","10","9","8","7","6","5","4","3","2","1", # Standard Values
                   "21", "20" "19", "18", "17", "16", "15", "14", "13", "12", "11", "Excuse",  # Tarot
                   "none"] # For joker  

class StdCard:
    """
    Class defining a game server
        -> color : color of the card
        -> shape : shape of the cards
        -> value : value of the card
    """
    
    default_color = "none"
    default_shape = "joker"
    default_value = "none"
    
    # Builder
    def __init__( self, color=default_color, shape=default_shape, value=default_value ) :
        if color in accepted_colors and shape in accepted_shapes and value in accepted_values :
            self.color = color
            self.shape = shape
            self.value = value
            return
        else :
            print("Issue creating card with caracteristics - color: " + color + " shape: " + shape + " value: " + value )
            return
        
    # Accessors methods
    def get_color( self ):
        """Method that returns the color"""
        return self.color
    def get_shape( self ):
        """Method that returns the shape'"""
        return self.shape
    def get_value( self ):
        """Method that returns the value"""
        return self.value
    def get_all( self ):
        """Method that returns all informations"""
        return self.color, self.shape, self.value
    
    # Modifyers
    def set_color( self, new_color ):
        """Method that modifies the hostna me of the server"""
        if new_color in accepted_colors :
            self.color = new_color
            return
        else:
            print("The value " + new_color + " is not accepted for standard cards.")
            print("Accepted values are: " + accepted_colors )
            return
        return
    def set_shape( self, new_shape ):
        """Method that modifies the hostname of the server"""
        if new_shape in accepted_shapes :
            self.shape = new_shape
            return
        else:
            print("The value " + new_shape + " is not accepted for standard cards.")
            print("Accepted values are: " + accepted_shapes )
        return
    def set_value( self, new_value ):
        """Method that modifies the hostname of the server"""
        if new_value in accepted_values :
            self.port = new_value
            return
        else:
            print("The value " + new_value + " is not accepted for standard cards.")
            print("Accepted values are: " + accepted_values )
        return
    def set_all( self, new_color, new_shape, new_value ):
        self.set_color( new_color )
        self.set_shape( new_color )
        self.set_value( new_color )
        return
    
    def print_all( self ):
        print("color: " + str(self.get_color())+"; shape: " + str(self.get_shape()) + "; value: " + str( self.get_value()) + ";" )
        return
    

def appendCardByValues( deck, color, shape, accepted_values):
    for value in accepted_values:
        deck.append( StdCard( color, shape, value) )
    return 
    
reduced_colors = ["black","red"]
reduced_shapes = ["trefle","pique","carreau","coeur"]
reduced_values = ["As","Roi","Dame","Valet","10","9","8","7" ] 
black_shapes = [ "trefle", "pique" ]
red_shapes   = [ "carreau", "coeur" ]
# Create the reduced deck
def initReducedDeck():
    deck = []
    for shape in reduced_shapes:
        if shape in black_shapes  :
            appendCardByValues( deck, "black", shape, reduced_values )
        else:
            appendCardByValues( deck, "red", shape, reduced_values )
    return deck

standard_colors = reduced_colors
standard_shapes = reduced_shapes
standard_values = ["As","Roi","Dame","Valet","10","9","8","7","6","5","4","3","2"] 
def initStandardDeck():
    deck = []
    for shape in standard_shapes:
            if shape in standard_shapes :
                appendCardByValues( deck, "black", shape, standard_values )
            else:
                appendCardByValues( deck, "red", shape, standard_values )
    return deck
def initStandardDeckWithJoker():
    deck = initStandardDeck()
    for i in range(2):
        deck.append( StdCard("none","joker","none") )
    return deck

tarot_colors = reduced_colors
tarot_shapes = reduced_shapes
tarot_values = ["As","Roi","Dame","Cavalier","Valet","10","9","8","7","6","5","4","3","2"] 
def initTarotDeck():
    deck = []
    for shape in standard_shapes:
            if shape in standard_shapes :
                appendCardByValues( deck, "black", shape, standard_values )
            else:
                appendCardByValues( deck, "red", shape, standard_values )
    # Adding the atouts
    for i in range(1,22):
        deck.append( StdCard( "none", "atout", str(i) ) )
    # Adding the excuse
    deck.append( StdCard( "none", "atout", "Excuse" ) )    
    return deck

def printAllDeck( deck ):
    for card in deck:
        card.print_all()
    return

def shuffleCards( deck, n ):
    for i in range(n):
        random.shuffle( deck )
    return deck

def dealCards( deck, n_players, n_cards_per_players ):
    hands = []
    deck2 = deck
    for player in range(n_players):
        player_hand = []
        for card in range( n_cards_per_players ):
            player_hand.append( deck[0] )
            deck2.pop(0)
        hands.append( player_hand )
    return hands, deck2