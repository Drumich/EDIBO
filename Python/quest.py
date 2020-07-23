```
import time

delay = 5
#time.sleep(delay)
def intro():
    print("There's a bear terrorising our little village")
    intro.quest = input("Would you like to go on a quest and help us?: (yes/no)")
    intro.name = input(str("Tell me your name Adventurer : "))


def cave():
    print(str(input("""We've been walking for a day , 
    would you like to set up camp inside this cave or stay outside of the cave? :
    (cave/outside)
    """)))



if intro.quest.lower().strip() == "yes":
    print("Great , follow me into this forest where the bear was last seen.")
    time.sleep(delay)

    if cave() == "cave":
        print("I won't go any farther %s , you're on your own now.Good Luck!" % name)
        print("You enter the cave alone, it's dark and smells.You sense presence of something \n...something scary")
    else:
        print("You set up camp outside of the cave!")


else:
    print("Maybe next time?")

```
