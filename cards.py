#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 00:49:44 2020

@author: moogmt
"""

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
    def _get_color( self ):
        """Method that returns the color"""
        return self.color
    def _get_shape( self ):
        """Method that returns the shape'"""
        return self.shape
    def _get_value( self ):
        """Method that returns the value"""
        return self.value
    
    # Modifyers
    def _set_color( self, new_color ):
        """Method that modifies the hostna me of the server"""
        if new_color in accepted_colors :
            self.color = new_color
        else:
            print("The value " + new_color + " is not accepted for standard cards.")
            print("Accepted values are: " + accepted_colors )
        return
    def _set_shape( self, new_shape ):
        """Method that modifies the hostname of the server"""
        if new_shape in accepted_shapes :
            self.shape = new_shape
        else:
            print("The value " + new_shape + " is not accepted for standard cards.")
            print("Accepted values are: " + accepted_shapes )
        return
    def _set_value( self, new_value ):
        """Method that modifies the hostname of the server"""
        if new_value in accepted_values :
            self.port = new_value
        else:
            print("The value " + new_value + " is not accepted for standard cards.")
            print("Accepted values are: " + accepted_values )
        return
    
def initReducedDeck():
    return
    
def initStandardDeck():
    return

def initTarotDeck():
    return

def shuffleCards():
    return

def dealCards( deck, n_players, n_cards_per_players ):
    return