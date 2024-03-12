######################################
#### DnD: The Lone Wolf Campaigns ####
######################################

import character
import os
from time import sleep

selections = ["New Character", "New Campaign", "View Character", "View Campaign"]

def main():
    os.system('clear && tput civis')
    print("##### Welcome to DnD: The Lone Wolf Campaigns #####   " )
    sleep(3)    
    main_menu()

def spinner(message):
    animation = ['|', '/', '-', '\\', '|', '/', '-', '\\']
    for i in range(3):
        for frame in animation:
            print(f"{message} {frame}", end='\r')
            sleep(0.25)
    
def new_character():
    os.system('clear')
    os.system('tput civis')
    spinner("Creating new character")
    os.system('clear')
    player = character.DnDCharacter()
    print(player)
    sleep(3)
    os.system('tput cnorm')

def new_campaign():
    print("New Campaign")

def view_character():
    print("View Character")

def view_campaign():
    pass

actions = [new_character, new_campaign, view_character, view_campaign]

def main_menu():
    os.system('clear && tput cnorm')
    [print(f"{index + 1}) {selection}") for index, selection in enumerate(selections)]
    selection = input("\n Make a selection >>> ")
    try:
        actions[int(selection) - 1]()
        
    except(Exception):
        print("\n That isn't an option right now, try again.")
        sleep(3)
        main_menu()

if __name__ == '__main__':
    main()
