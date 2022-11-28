import time
from weaponPackage import combat, change_e_pos, backpack, backpack_list, iron_sword
from dialoguePackage import aDialogue

# this scene is the journey to frostfall and includes the battle of frostfall

t = 4
# -----------------------------------------------------------------------------------------------------------
# is the combat tutorial function to allow the code to be more clean and organized
def combat_tutorial():
    print("*THIS IS YOUR COMBAT TUTORIAL*")
    time.sleep(t)
    print("When entering combat you will first be able to select a weapon available in your backpack")
    time.sleep(t)
    print("You will be prompted to press a random letter on you keyboard to initiate an attack")
    time.sleep(t)
    print("If the wrong key is pressed, your attack will fail and you will take damage"
          "\n" "but if the correct key is pressed you will attack first, followed by the enemy's attack")
    time.sleep(t)
    print("Combat will last until you or your opponent dies, your death will result in game over")
    time.sleep(t)
    print("At the end of combat your health will restore to its maximum")
    time.sleep(t)
    print("Do be careful though! Your opponent can launch one last attack when at 0 health!")
    time.sleep(t)
    print("*TUTORIAL END*")
    time.sleep(t)
# --------------------------------------------------------------------------------------------------------------

def scene2():
    # the journey to frostfall
    print("You start your journey to Frostfall, walking down the main road")
    time.sleep(t)
    print("The journey proves uneventful with no traders or other people in sight")
    time.sleep(t)
    print("Out of a bush enters a slime!")
    time.sleep(t)
    print("You have entered combat with slime!")
    time.sleep(t)

    combat_tutorial()  # this calls the function that is a combat tutorial
    combat()  # this calls the combat function with the slime as the enemy

    time.sleep(t)
    print("You continue to walk down the road, realizing that there should have been at least one trader by now")
    time.sleep(t)
    print("Suddenly, you see a bandit in the road up ahead")
    time.sleep(t)
    print("Remembering what Les said, you decide its time to be a hero")
    time.sleep(t)
    print("You enter combat with the bandit!")

    change_e_pos()  # this increases the e var by 1 making the enemy type a bandit
    combat()  # this iteration of the combat function should run with the bandit as the enemy
    time.sleep(t)

    # -------------------------------------------------------------------------------------------
    # the arrival in frostfall
    print("Finally after a long day of walking and fighting you arrive at Frostfall")
    time.sleep(t)
    print("You see plumes of smoke rising from the inside of the walls, and sounds of combat can be heard inside")
    time.sleep(t)
    print("Running inside the city, you see a soldier on the ground, lifeless and bloody")
    time.sleep(t)
    print("You notice his iron sword on the ground, while it may not be the best weapon, its certainly an improvement")
    time.sleep(t)

    print("*YOU HAVE RECEIVED IRON SWORD*")
    backpack["iron sword"].append(iron_sword)  # this adds the sword to the player backpack
    backpack_list.append("iron sword")

    print("Running through the debris you see soldiers fighting off a horde of monsters")
    time.sleep(t)
    print("In the center of the town you see a large figure")
    time.sleep(t)
    print("You notice 1 man in shining silver armor standing off against him")
    time.sleep(t)
    print('Large figure: *diabolical laughter* "You stand no chance hero... This is your finale stand"')
    time.sleep(t)
    print('Unknown Hero: "Your destruction ends here Dragorath"')
    time.sleep(t)
    print("You watch as the hero lunges at Dragorath, only to get grabbed and thrown through several buildings")
    time.sleep(t)
    print('Dragorath raises his hands up and looks up to the sky, bellowing "NOW WHOS GONNA STOP ME!?"')
    time.sleep(t)
    print("Fear strikes your heart, but knowing the world is depending on you to save it, you step forward ready to face off againt Dragorath")
    time.sleep(t)
    print("Realizing these may be your last moments of life, you deeply inhale trying to calm yourself when-")
    time.sleep(t)
    print('Large flash of light followed by a figure whos outline you can barely make out')
    time.sleep(t)
    print('Upon a closer look you see that this figure appears to be wearing robes')
    time.sleep(t)
    print('After another large flash of light you notice Dragorath holding his side, where blood appears to be flowing out of a wound')
    time.sleep(t)
    print('Wizard: "Dragorath you stand no chance! Back down"')
    time.sleep(t)
    print("Dragorath roars in rage, and in his attempt to escape sprints directly toward you")
    time.sleep(t)

    change_e_pos()  # this again increases e by 1, which is the index for the enemy type, this makes it Dragorath
    combat()

    time.sleep(t)
    print("Dragorath falls to the ground, fatally wounded from your battle")
    time.sleep(t)
    print('Dragorath: "At least it wasnt Chris Pra- I mean Mari- err I mean that wizard who ended me!"')
    time.sleep(t)
    print('Dragorath: "You dont know what you got yourself involved with tiny mortal"')
    time.sleep(t)
    print('Dragorath: "The Demon Lord grows restless, and soon plans to take the entire region of Consulatia over!" *evil laughter*')
    time.sleep(t)
    print("Dragorath melts to dust, leaving only his helmet behind")
    time.sleep(t)
    print('Wizard: "Nice work"')
    time.sleep(t)
    # ---------------------------------------------------------------------------------------------------
    aDialogue.getTree('frostfall').callAnswer()  # this runs the conversation with the wizard, Kexus

# scene2()
