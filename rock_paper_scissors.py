#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:14:59 2020

@author: aronj23
"""

import random
import os
import time
import sys

PlayScore = 0
CompScore = 0
Rounds = 1
 
def clear():
    os.system("clear")
 
# Set of instructions for Rock-Paper-Scissors
def rps_instructions():
 
    print()
    print("Instructions for Rock-Paper-Scissors : ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()
 
# Set of instructions for Rock-Paper-Scissors-Lizard-Spock
def rpsls_instructions():
 
    print()
    print("Instructions for Rock-Paper-Scissors-Lizard-Spock : ")
    print()
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("Rock crushes Lizard")
    print("Lizard poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitates Lizard")
    print("Lizard eats Paper")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")
    print("Rock crushes Scissors")
    print()
 
def rps():
    global Rounds
    global rps_table
    global game_map
    global name
    global PlayScore
    global CompScore
 
    # Game Loop for each game of Rock-Paper-Scissors
    while True:
 
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instructions")
        print("Enter \"Rock\" (\"r\"),\"Paper\" (\"p\") or \"Scissors\" (\"s\") to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
        if PlayScore < 5 and CompScore < 5:
            print("Round: " + str(Rounds))
        print("Score is: " + str(PlayScore) + "|" + str(CompScore))
        print()
 
        # Player Input
        inp = input("Enter your move : ")
 
        if inp.lower() == "help":
            clear()
            rps_instructions()
            continue
        elif inp.lower() == "exit":
            clear()
            break  
        elif inp.lower() == "rock" or inp.lower() == "r":
            player_move = 0
        elif inp.lower() == "paper" or inp.lower() == "p":
            player_move = 1    
        elif inp.lower() == "scissors" or inp.lower() == "s":
            player_move = 2
        else:
            clear()
            print("Wrong Input!!")
            rps_instructions()  
            continue
 
        print("Computer making a move....")
 
        print()
        time.sleep(2)
 
        # Get the computer move randomly
        comp_move = random.randint(0, 2)
 
        # Print the computer move
        print("Computer chooses ", game_map[comp_move].upper())
 
        # Find the winner of the match
        winner = rps_table[player_move][comp_move]
 
        # Declare the winner 
        if winner == player_move:
            print(name, "WINS!!!")
            PlayScore = PlayScore + 1
            #print("Score is:" + str(PlayScore) + "|" + str(CompScore))
            #if PlayScore > 4:
             #   print(name, "Wins the game!")
              #  sys.exit()
        elif winner == comp_move:
            print("COMPUTER WINS!!!")
            CompScore = CompScore + 1
            #print("Score is:" + str(PlayScore) + "|" + str(CompScore))
            #if CompScore > 4:
             #   print("Computer wins the game, better luck next time!")
              #  sys.exit()
             
        else:
            print("TIE GAME")
 
        print()
        time.sleep(2)
        clear()
        #print("Score is: " + str(PlayScore) + "|" + str(CompScore))
        if CompScore > 4:
                print("Computer wins the game, better luck next time!")
                sys.exit()
        elif PlayScore > 4:
            print(name, "Wins the game!")
            sys.exit()
        elif PlayScore < 5 and CompScore < 5:
            Rounds = Rounds + 1
 
def rpsls():
     
    global rpsls_table
    global game_map
    global name
    global PlayScore
    global CompScore
 
    # Game Loop for each game of Rock-Paper-Scissors-Lizard-Spock
    while True:
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instructions")
        print("Enter \"Rock\" (\"r\"),\"Paper\" (\"p\"),\"Scissors\" (\"s\"),\"Lizard\" (\"l\"), or \"Spock\" (\"sp\") to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
        if PlayScore < 5 and CompScore < 5:
            print("Round: " + str(Rounds))
        print("Score is: " + str(PlayScore) + "|" + str(CompScore))
        print()
 
        # Player Input
        inp = input("Enter your move : ")
 
        if inp.lower() == "help":
            clear()
            rpsls_instructions()
            continue
        elif inp.lower() == "exit":
            clear()
            break  
        elif inp.lower() == "rock" or inp.lower() == "r":
            player_move = 0
        elif inp.lower() == "paper" or inp.lower() == "p":
            player_move = 1    
        elif inp.lower() == "scissors" or inp.lower() == "s":
            player_move = 2
        elif inp.lower() == "lizard" or inp.lower() == "l":
            player_move = 3
        elif inp.lower() == "spock": or inp.lower() == "sp"
            player_move = 4
        else:
            clear()
            print("Wrong Input!!")
            rps_instructions()  
            continue
 
 
        print("Computer making a move....")
 
        comp_move = random.randint(0, 4)
        print()
        time.sleep(2)
 
        print("Computer chooses ", game_map[comp_move].upper())
 
        winner = rpsls_table[player_move][comp_move]
        print()
        if winner == player_move:
            print(name, "wins this round!")
            PlayScore = PlayScore + 1
            print("Score is:" + str(PlayScore) + "|" + str(CompScore))
            if PlayScore > 4:
                print(name, "Wins the game!")
                sys.exit()
        elif winner == comp_move:
            print("COMPUTER wins this round!")
            CompScore = CompScore + 1
            print("Score is:" + str(PlayScore) + "|" + str(CompScore))
            if CompScore > 4:
                print("Computer wins the game, better luck next time!")
                sys.exit()  
        else:
            print("TIE round!")      
        print()
        time.sleep(2)
        #clear()
 
# The main function
if __name__ == '__main__':
 
    # The mapping between moves and numbers
    game_map = {0:"rock", 1:"paper", 2:"scissors", 3:"lizard", 4:"Spock"}
 
    # Win-lose matrix for traditional game
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
    

    
    # This creates a "table", where -1 means a draw, 1 means that that the 
 
    # Win-lose matrix for new version of the game
    rpsls_table = [[-1, 1, 0, 0, 4],[1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]
 
     
    name = input("Enter your name: ")
 
    # The GAME LOOP
    while True:
 
        # The Game Menu
        print()
        print("Let's Play!!!")
        print("Which version of Rock-Paper-Scissors?")
        print("Enter 1 to play Rock-Paper-Scissors")
        print("Enter 2 to play Rock-Paper-Scissors-Lizard-Spock")
        print("Enter 3 to quit")
        print()
 
        # Try block to handle the player choice 
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong Choice")   
            continue
 
        # Play the traditional version of the game
        if choice == 1:
            rps()
 
        # Play the new version of the game
        elif choice == 2:
            rpsls()
 
        # Quit the GAME LOOP    
        elif choice == 3:
            break
 
        # Other wrong input
        else:
            clear()
            print("Wrong choice. Read instructions carefully.")
 
                            
