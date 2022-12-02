import time
from dialoguePackage import aDialogue
from weaponPackage import backpack, dagger, backpack_list

#   this is scene has the introduction and tavern scene

t = 4  # t is for time, and its the amount of seconds in between every line

def dialogue_tutorial():
    print("*THIS IS YOUR DIALOGUE TUTORIAL*")
    time.sleep(t)
    print("You will be prompted with multiple dialogue options when entering conversation")
    time.sleep(t)
    print("To continue the conversation, type the number of the dialogue option you want to say")
    time.sleep(t)
    print("When in dialogue, you cannot leave until the conversation is done")
    time.sleep(t)
    print("*THIS IS THE END OF YOUR DIALOGUE TUTORIAL*")
    time.sleep(t)


def scene1():
    username = input("Enter your name: ").title()
    print("??????: Welcome to Consulatia, " + username + ", I am Les")
    time.sleep(t)
    print("Les: It's your luck day! I chose you to become the next hero of Consulatia!")
    time.sleep(t)
    print("Les: It's your task to take down the evil demon lord who's trying to take over the land!")
    time.sleep(t)
    print("Les: It wouldn't be very epic of me to send you into this world with no information so let me give you some basics!")
    time.sleep(t)
    print("Les: You're currently located in the small village of Woodside, which is just outside the Elderwood Forest.")
    time.sleep(t)
    print("Les: I'm gifting you this dagger! Make sure to use it well on your travels.")
    time.sleep(t)
    print("*YOU HAVE RECEIVED DAGGER*")

    backpack["dagger"].append(dagger)  # this appends the dagger function to the list in the backpack
    backpack_list.append("dagger")  # this adds the string dagger to allow for the use input to read it later on

    time.sleep(t)
    print("Les: Good luck! You don't want to be seeing me again!")
    time.sleep(t)
    print("You wake up in an unfamiliar room...")
    time.sleep(t)
    print("You realize that you're at an inn, and decide to head downstairs")
    time.sleep(t)
    dialogue_tutorial() # this runs your dialogue tutorial
    aDialogue.getTree('tavern').callAnswer()  # this runs the dialogue for tavern

#  scene1()
