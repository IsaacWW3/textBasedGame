import random
import string
import time
import sys

string.ascii_lowercase

t = 2

''' the character class holds the variables for both the player and enemies, I originally planned for this to be 
    more advanced, but instead opted to make it more simple and develop systems such as the dialogue tree '''


class Character:
    def __init__(self, hp: int, atk: int):
        self.hp = hp
        self.atk = atk


# this is setting the variables for the player
player = Character(100, 0)

# this is setting the variables for the enemy
slime = Character(50, 5)
bandit = Character(75, 10)
Dragorath = Character(75, 20)

# --------------------------------------------------------------------------------------------------------------------
# this is a list of the enemy types in string form
# these two lists must be in the exact same order, otherwise the name and values won't line up
enemy_name = ['slime', 'bandit', 'Dragorath']
enemy_type = [slime, bandit, Dragorath]

e = 0  # this will  be the index for enemy_type and enemy_name list

# -------------------------------------------------------------------------------------------------------------------
def change_e_pos():
    global e
    e += 1


def change_e_neg():
    global e
    e -= 1

# --------------------------------------------------------------------------------------------------------------------
# variables for setting the weapons to different variable
def dagger():
    player.atk = 10


def iron_sword():
    player.atk = 15


def steel_sword():
    player.atk = 25


def god():
    player.atk = 100

# ---------------------------------------------------------------------------------------------------------------------
# this is your backpack dictionary, each value is a list, and the weapon function gets appended to the list
backpack = {
    "dagger": [],
    "iron sword": [],
    "steel sword": [],
    "god": []
}
# this is a normal list that stores the string in the same order of the backpack
backpack_list = []
# ---------------------------------------------------------------------------------------------------------------------
'''
Below is all of the original code where I worked on developing appending the backpack, parts are required for the code
to work properly
#  backpack["dagger"].append(dagger)
#  backpack_list.append("dagger")

#  backpack["iron sword"].append(iron_sword)
#  backpack_list.append("iron sword")

#  backpack["steel sword"].append(steel_sword)
# backpack_list.append("steel sword")


#  backpack["god"].append(god)
# backpack_list.append("god)


#  print(backpack["god"][0]())
#  backpack["god"][0]()
'''

# --------------------------------------------------------------------------------------------------------------------
#  this function is for checking if the player or enemy is dead, and if they aren't it prints their health

def dead_check():
    global fight
    if enemy_type[e].hp <= 0:

        time.sleep(t)

        print(enemy_name[e], "health is now 0")

        time.sleep(t)

        print("You successfully killed", enemy_name[e])
        player.hp = 100

        time.sleep(t)

        print("Your health has recovered to", player.hp)
        fight = False

    elif player.hp <= 0:
        time.sleep(t)

        print(enemy_name[e], "health is now", enemy_type[e].hp)
        time.sleep(t)

        print("Your health is now 0")
        time.sleep(t)
        print("Game over!")
        exit()  # this terminates the program if the player hits zero health
    else:
        time.sleep(t)
        print(enemy_name[e], "health is now", enemy_type[e].hp)
        time.sleep(t)
        print("Your health is now", player.hp)

# ---------------------------------------------------------------------------------------------------------------------
def weapon_select():  # this function is for selecting a weapon
    print("You weapon choices are", *backpack_list, sep=", ")

    loop = False
    while not loop:
        weapon_choice = input("Please select your weapon: ").lower()
        for i in backpack_list:  # this translates to for (index in list)
            if weapon_choice in i:  # if user input in index
                loop = True  # this sets the loop to true, breaking the while loop
                print("You have chosen to use your", i)  # this prints the item that is stored at the index
                backpack[i][0]()  # this calls the dic through a list and through a dictionary
                break
        if not loop:  # this runs after the for loop, and is a final check to say enter a valid input, because they clearly didn't if this runs
            print("Please enter a valid input")


# -------------------------------------------------------------------------------------------------------------------

def combat():  # this function is for combat
    global fight
    fight = True  # setting fight to True to trigger the while loop later one
    print("You have entered combat against " + enemy_name[e] + "!")  # the + enemy_name[e] + allows for cleaner formatting mid-text
    weapon_select()  # this calls the weapon selection function from above

    while fight is True:
        # this generates a random letter
        random_letter = random.choice(string.ascii_lowercase)

        time.sleep(t)

        print("Press " + random_letter + " to attack!")  # this tells the user which randomly generated button to press

        user_attack = input("Press the button: ").lower()  # this is where the actual input is stored

        if user_attack in random_letter:  # this runs a check for the user input to see if it matches the randomly generated number
            time.sleep(t)

            print("You attack " + enemy_name[e] + " for", player.atk, "damage!")  # I know the formatting for this one is weird, but it just works

            enemy_type[e].hp -= player.atk  # enemy hp minus plater attack ez

            time.sleep(t)

            dead_check()
            if player.hp > 0 and enemy_type[e].hp > 0:
                print(enemy_name[e], "attacks you for", enemy_type[e].atk,
                      "damage!")  # this prints how much damage you will take

                player.hp -= enemy_type[e].atk  # player health minus enemy attack

                dead_check()

        else:  # this is for if the player puts the wrong character, it's all more of the same
            time.sleep(t)

            print("Your attack failed!!")

            time.sleep(t)

            print(enemy_name[e], "attacks you for", enemy_type[e].atk, "damage!")

            player.hp -= enemy_type[e].atk

            dead_check()

#  combat()
