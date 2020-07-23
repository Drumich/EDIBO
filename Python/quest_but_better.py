import time
import sys
import random
from colorama import Fore
from colorama import Style



### Variables ###
delay = 2
hunger = 1
health = 10
weapon = "Rusty Sword"
weapon2 = ""



print("Welcome to our town , what is your name stranger? \n")

# class player:
#     def __init__(self):
name = input(str("Enter your name:\n "))



def intro():
    print("Nice to meet you %s , our town has been under attack recently by mysterious creature , would you help us?" % name)
    #time.sleep(delay)
    start = input(str("(y/n)\n"))
    if start == "y":
        print("Excellent, let me tell you more about the creature!")
        #time.sleep(delay)
        print("The creature has been described as big,black,massive claws and teeth ,red eyed like...creature")
        #time.sleep(delay)
        print("Now follow me out of the town, %s" % name)
        #time.sleep(delay)
    else:
        print("Maybe next time.")
        sys.exit()
    
def forest():
    global hunger
    print("Alright %s , the creature was last seen heading into the forest , i can't go with you , but take this rusty blade.Good Luck !" % name)
    #time.sleep(delay)
    print("You start walking into the forest , you hear rumbling.")
    investigate = input("Do you want to investigate? (y/n)\n")
    if investigate == "y":
        print("You walk closer to the rumbling sounds.")
        #time.sleep(delay)
        action = input("You see a rabbit , would you try and catch it? (y/n)\n")
        if action == "y":
            print("You try to catch the rabbit.")
            #time.sleep(delay)
            for num in range(1):
                r = random.randint(1,11)
                if r >= 5:
                    print("You caught the rabbit, you won't go hungry tonight.")
                    hunger += 3
                else:
                    print("You fail to catch the rabbit , it was too quick ,you are getting hungry.")
                    hunger -= 1
        else:
            print("You ignore the rabbit,you are getting hungry.")
            hunger -= 1
    else:
        print("You decide not to investigate.")
    print(f"Your hunger is now : {hunger}" )


def cave():
    global weapon
    global hunger
    global health
    print("You see a cave entrance in the distance, it's getting dark and you should set up camp soon.")
    entrance = input("Would you like to go inside the cave or stay outside (cave/outside)\n")
    if entrance == "cave":
        print("You enter the cave and look around.")
        #time.sleep(delay)
        print("You see a pile of junk next to a couple of skulls, YOU HEAR GROWLING!!!\n")
        #time.sleep(delay)
        print("You see red eyes slowly creeping towards you! It's a frickin lion i guess")
        whatdo = input("(fight/run): \n")
        if whatdo == "fight":
            print(f"You draw your {weapon} and start slashing furiously!")
            for num in range(1):
                r = random.randint(1,4)
                health -= r
                print(f"""
                The Beast is dead!Congratulations!
                You took {r} damage and have {health} {Fore.GREEN}health{Style.RESET_ALL} left.""")




    #else:
        #stay outside






if hunger <= 0:
    print("You died from hunger")
    sys.exit()

if health <= 0:
    print("You died!")
    sys.exit()

intro()
forest()
cave()


