### All delays are removed for testing purposes :D ###
### need to make lists for weapons and stuff , also put print statements in variables so there is less code ###
import time
import sys
import random
from colorama import Fore
from colorama import Style



### Variables ###
delay = 2
hunger = 2
health = 10
weapon = "Rusty Sword"
weapon2 = ""



print("Welcome to our town , what is your name stranger? \n")
### Class , idk what they do , so i'm not touching them...yet ###
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
                r = random.randint(1,9)
                if r >= 6:
                    print("You caught the rabbit, you won't go hungry tonight.")
                    hunger += 1
                else:
                    print("You fail to catch the rabbit , it was too quick ,you are getting hungry.")
                    hunger -= 1
            print(f"Your hunger is now : {hunger}" )
        else:
            print("You ignore the rabbit,you are getting hungry.")
            hunger -= 1
    else:
        print("You decide not to investigate.")
        hunger -= 1
        print(f"Your hunger is now : {hunger}" )
    if hunger <= 0:
        print("You died from hunger")
        sys.exit()


def cave():
    global weapon
    global weapon2
    global hunger
    global health
    print("You see a cave entrance in the distance, it's starting to get dark and you should set up camp soon.")
    entrance = input("Would you like to go inside the cave or stay outside (cave/outside)\n")
    if entrance == "cave":
        print("You enter the cave and look around.")
        #time.sleep(delay)
        print("You see a pile of junk next to a couple of skulls, YOU HEAR GROWLING!!!\n")
        #time.sleep(delay)
        print("You see red eyes slowly creeping towards you! It's a frickin lion i guess")
        what_do = input("(fight/run): \n")
        if what_do == "fight":
            print(f"You draw your {weapon} and start slashing furiously!")
            for num in range(1):
                r = random.randint(2,6)
                health -= r
                print(f"""
                The Beast is dead!Congratulations!
                You took {r} {Fore.RED}damage{Style.RESET_ALL} 
                and have {health} {Fore.GREEN}health{Style.RESET_ALL} left.""")
                #time.sleep(delay)
                weapon = "Iron Sword"
                weapon2 = "Bow"
                hunger += 5
                print(f"You look around the cave and find an {weapon} and a {weapon2} with some arrows...Nice.")
                print("You decide to stay in the cave for the night and cook some lion meat.Delicious!")
        else:
            print("You run outside") # make things harder because it's dark and you can't see
            what_do_now = input(f"""It's dark , you can't stay here or you'll {Fore.RED}DIE!{Style.RESET_ALL}
            You can go back in the cave and fight or stay here and set camp.(fight/camp)\n""")
            if what_do_now == "fight":
                print("You go back inside , it's dark and hard to see.You start swinging you sword!")
                for num in range(1):
                    r = random.randint(8,10)
                    health -= r
                    if health <= 0:
                        print(f"You {Fore.RED}died{Style.RESET_ALL} fighting the frickin lion!")
                        sys.exit()
                    print(f"""
                    The Beast is dead!Congratulations!
                    You took {r} {Fore.RED}damage{Style.RESET_ALL} 
                    and have {health} {Fore.GREEN}health{Style.RESET_ALL} left.""")
                    # need an if statement for health
                #print(f"You look around the cave and find an {weapon} and a {weapon2} with some arrows...Nice.")
                #print("You decide to stay in the cave for the night and cook some lion meat.Delicious!")
            else:
                print("You set a camp outside")
                ##time.sleep(delay)
                print(f"You died.There was a {Fore.RED}frickin lion{Style.RESET_ALL} in the cave and it visited you while you were sleeping.")
                sys.exit()
    else:
        print("You set a camp outside")
        ##time.sleep(delay)
        print(f"You died.There was a {Fore.RED}frickin lion{Style.RESET_ALL} in the cave and it visited you while you were sleeping.")
        sys.exit()







if hunger <= 0:
    print("You died from hunger")
    sys.exit()

if health <= 0:
    print("You died!")
    sys.exit()

intro()
forest()
cave()
