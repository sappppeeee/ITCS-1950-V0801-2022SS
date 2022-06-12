# Text Base Game
# Mohammed Shourov
# 6-4-2022
# ITCS 1950 V0801 2022SS - Intro to Game Development
# Homework 6 - Project 1 skeleton

# imports module
import random
import time
import string
import sys

# intro function
def intro():
  print('------------------------------------------------------------------------')
  print('--------------------------Dungeons And Bosses---------------------------')
  print('''Imagine if you are summoned into a medieval world as an adventurer,
           who has been exlporeing dungeons, leveling up and becoming more 
           powerful to reach the end of the dungeons to conquer it. And you 
           have finaly reached the last level/boss. And  you don't know what 
           to expect as your going into theboss room.''')
  # put a time delay
  print('''This text-based game revolves around you solving math problems
           to defeating the RPG boss. The program will randomly pick a boss
           for you (from Black Dragon, Hell Hound, and The White Witch).
           First, you will enter your name into the program. Then, you
           will input the difficulty level to determine the difficulty of
           the math problems(From Easy =+,- / Medium = +,-,* / Hard = +,-,*, %).
           Then you will have to choose Class or Character. But Class of
           Character comes with a special ability and turns limits. However,
           you only have to get three right answers(Unless you choose the Warrior
           Class or Character for which you only need two right answers).''')
  print('------------------------------------------------------------------------')
  # put a time delay
  print('------------------------------Ganme Rules:------------------------------')
  print('Get 3 righ answer to defeat the Boss / 2 righ answer for Warrior.')
  print('''Pick difficulty : Easy / Medium / Hard
              :  +,- /  +,-,* / +,-,*,/''')
  # put a time delay
  print('''  Pick class/     : Warrior, Assassin
  character       : Mage and Berserker.

                  Class/Character Rules:
  Warrior -     | 4 Turns | 
  Assassin -    | 3 Turns | Dice roll (1-5)/ not Dice roll if dragon.
  Mage -        | 2 Turns | Dice roll (1-3)
  Berserker -   | 4 Turns | Dice roll (1-10)''')
  print('------------------------------------------------------------------------')

# name function 
def name():
  playername = input('Enter Your Game Name:')
  print('------------------------------------------------------------------------')
  print('------------------------------------------------------------------------')
  print('              Welcome Dungeons And Bosses:', playername)
# random_boss function
def random_boss():
  print('Randomly spawning A Boss...')
  # put a time delay
  randomboss1 = random.randint(1, 3) #randomize the boss
  if 1 == randomboss1:
    print('-------------------------------Hell Hound-------------------------------')
  if 2 == randomboss1:
    print('----------------------------The White Witch-----------------------------')
  if 3 == randomboss1:
    print('------------------------------Black Dragon------------------------------')
  print('work in progress....')

# dice_roll function
def dice_roll():
  print('work in progress....')
# character_selection function
def character_selection():
  print('work in progress....')
# math_problems function
def math_problems():
  setscore = 0
  print('work in progress....')

# main function
def main():
  intro()
  # put a time delay
  name()
  random_boss()
  dice_roll()
  character_selection()
  math_problems()

main()