import time
import sys
import random
delay = 2

print("Welcome to our town , what is your name stranger? ")

# class player:
#     def __init__(self):
name = input(str("Enter your name: "))
        # self.weapon = "Rusty Sword"
        # self.weapon2 = ""
        # self.hunger= 0

def intro():
    print("Nice to meet you %s , our town has been under attack recently by mysterious creature , would you help us?" % name)
    # time.sleep(delay)
    # start = input(str("(y/n)"))
    # if start == "y":
    #     print("Excellent, let me tell you more about the creature!")
    #     time.sleep(delay)
    #     print("The creature has been described as big,black,massive claws and teeth ,red eyed like...creature")
    #     time.sleep(delay)
    #     print("Now follow me out of the town, %s" % name)
    #     time.sleep(delay)
    # else:
    #     sys.exit()
    
def forest():
    print("Alright %s , the creature was last seen heading into the forest , i can't go with you , but take this rusty blade.Good Luck !" % name)
    #time.sleep(delay)
    print("You start walking into the forest , you hear rumbling.")
    investigate = input("Do you want to investigate? (y/n)")
    if investigate == "y":
        print("You walk closer to the rumbling sounds.")
        #time.sleep(delay)
        action = input("You see a rabbit , would you try and catch it? (y/n)")
        if action == "y":
            print("You try to catch the rabbit.")
            #time.sleep(delay)
            for num in range(1):
                r = random.randint(1,11)
                if r >= 5:
                    print("You caught the rabbit.")
                else:
                    print("You fail to catch the rabbit , it was too quick.")
        else:
            print("You ignore the rabbit.")








intro()
forest()































