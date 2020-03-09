from time import sleep
def start():
    print("Welcome to 'Find the Ticket'")
    start = input("Press S to Start or anything else to quit: ")
    if start == "S" or start == "s":
        print("""The amusement park has opened a super cool ride and
you really want to ride it with your friends.
You already bought a ticket to go in but your younger sister took
it without you noticing yesturday and hid it somewhere.""")
        def living_room():
            print("You are in the living room. What would you like to do now?")
            action = input("""(Check Table, Sofa, TV, or go to Hallway or Kitchen?)
You only need to type the name of the object or place. """)
            if action == "Table" or action == "table":
                print("Checking table...")
                sleep(3)
                print("The ticket is not on the table...")
                living_room()
            elif action == "Sofa" or action == "sofa":
                print("Checking around the sofa...")
                sleep(2)
                print("Digging between the cushions...")
                sleep(4)
                print("Pulling out the cushions...")
                sleep(4)
                print("You checked the whole sofa but there wasn't any ticket there...")
                living_room()
            elif action == "TV" or action == "tv" or action == "Tv":
                print("Checking the TV...")
                sleep(2)
                print("The ticket isn't there...")
                living_room()
            elif action == "Hallway" or action == "hallway":
                print("Going to the hallway...")
                sleep(2)
                hallway1()
            elif action == "Kitchen" or action == "kitchen":
                print("Going to the kitchen...")
                sleep(3)
                kitchen()
            else:
                print("Invalid response...")
                living_room()
        def hallway1():
            print("You are now in the hallway. Where would you like to go?")
            action = input("Living room, Kitchen, Bathroom, Bedroom or More options? ")
            if action == "Living room" or action == "living room" or action == "livingroom" or action == "Livingroom" or action == "Living" or action == "living":
                print("Going back to the living room...")
                sleep(2)
                living_room()
            elif action == "Kitchen" or action == "kitchen":
                print("Going to the kitchen...")
                sleep(2)
                kitchen()
            elif action == "Bathroom" or action == "bathroom":
                print("Going to the bathroom...")
                sleep(2)
                bathroom1()
            elif action == "Bedroom" or action == "bedroom":
                print("Going to your bedroom...")
                sleep(3)
                bedroom()
            elif action == "More" or action == "more":
                hallway2()
            else:
                print("Invalid response...")
                hallway1()
        def hallway2():
            print("There are more bedrooms at the other end of the hallway.")
            action = input("""Type 'bed1' to go to your younger sister's bedroom,
'bed2' to go to your parent's bedroom, 'out' to check outside, or 'back' to go back.
(Type what's in the quotation marks.) """)
            if action == "bed1":
                print("Going to your sister's bedroom...")
                sleep(2)
                bed1()
            elif action == "bed2":
                print("Going to your parent's bedroom...")
                sleep(3)
                bed2()
            elif action == "out":
                print("Going outside...")
                sleep(2)
                print("There's no need to go outside. Your sister didn't go outside since the day she took your ticket.")
                sleep(4)
                print("Going back in...")
                sleep(2)
                hallway1()
            elif action == "back":
                hallway1()
            else:
                print("Invalid response...")
                hallway2()
        def kitchen():
            print("You are now in the kitchen. What would you like to do?")
            action = input("Check Table, Drawers, or go to Hallway or Living Room? ")
            if action == "Table" or action == "table":
                print("Checking table...")
                sleep(2)
                print("The ticket is not on the table...")
                kitchen()
            elif action == "Drawers" or action == "drawers":
                print("Checking all the drawers. Please wait...")
                sleep(7)
                print("The ticket isn't in any of these drawers...")
                kitchen()
            elif action == "Hallway" or action == "hallway":
                print("Going to the hallway...")
                sleep(2)
                hallway1()
            elif action == "Living room" or action == "living room" or action == "livingroom" or action == "Livingroom" or action == "Living" or action == "living":
                print("Going back to the living room...")
                sleep(2)
                living_room()
            else:
                print("Invalid response...")
                kitchen()
        def bathroom1():
            print("""At first glance, you can see that the ticket isn't in the bathroom.
However, there are some drawers in the bathroom where she might have hidden the ticket.""")
            action = input("Do you want to check in the drawers? (Yes/No) ")
            if action == "Yes" or action == "yes" or action == "Y" or action == "y":
                print("Checking the drawers...")
                sleep(5)
                print("Much to your dismay, the ticket is not in the drawers...")
                sleep(2)
                print("Leaving the bathroom...")
                sleep(2)
                hallway1()
            elif action == "No" or action == "no" or action == "N" or action == "n":
                print("Leaving the bathroom...")
                sleep(2)
                hallway1()
            else:
                print("Invalid response...")
                bathroom1()
        def bedroom():
            print("You are now in your bedroom. What would you like to do?")
            action = input("""Check Bed(bed), Drawer 1(draw1), Drawer 2(draw2), Closet(closet), or go Back(back)?
'Type what's in the brackets.' """)
            if action == "bed":
                print("Checking the bed. This could take a while...")
                sleep(10)
                print("There's no sign of the ticket on the bed, even after checking throughly...")
                bedroom()
            elif action == "draw1":
                print("Checking the big drawer...")
                sleep(5)
                print("Lots of clothes, but no ticket...")
                bedroom()
            elif action == "draw2":
                print("Checking the smaller drawer beside your bed...")
                sleep(4)
                print("""You found a drawing of your ticket done by your younger sister in the drawer
but you can't use it when you go in the amusement park.""")
                bedroom()
            elif action == "closet":
                print("Checking the closet...")
                sleep(1)
                print("It's empty...")
                bedroom()
            elif action == "back":
                print("Going back to the hallway...")
                sleep(2)
                hallway1()
            else:
                print("Invalid response...")
                bedroom()
        def bed1():
            print("You are now in your sister's bedroom. What would you like to do?")
            action = input("Check Bed, Closet, Drawer, or go Back? ")
            if action == "Bed" or action == "bed":
                print("Checking the bed...")
                sleep(3)
                print("No ticket, but there are some dolls on her bed.")
                checkdoll = input("Do you want to check her dolls? (Yes/No) ")
                if checkdoll == "Yes" or checkdoll == "yes" or checkdoll == "Y" or checkdoll == "y":
                    print("Checking...")
                    sleep(3)
                    print("One of her dolls has a zipper...")
                    sleep(1)
                    print("You open the zipper...")
                    sleep(1)
                    print("There's something inside!")
                    sleep(1)
                    print("You take it out...")
                    sleep(1)
                    print("You take a closer look at it...")
                    sleep(1)
                    print(".")
                    sleep(1)
                    print(".")
                    sleep(1)
                    print(".")
                    sleep(1)
                    print("""IT'S THE TICKET!!!
You found the ticket! Now you can go to the amusement park with your friends!
Congratulations, you won!""")
                    sleep(6)
                    print("Exiting application...")
                    sleep(3)
                elif checkdoll == "No" or checkdoll == "no" or checkdoll == "N" or checkdoll == "n":
                    bed1()
                else:
                    print("Invalid response...")
                    bed1()
            elif action == "Closet" or action == "closet":
                print("Checking the closet...")
                sleep(4)
                print("There's a lot of clothes here...")
                sleep(4)
                print("The ticket probably isn't in here...")
                bed1()
            elif action == "Drawer" or action == "drawer":
                print("Checking the drawer...")
                sleep(8)
                print("Lots of drawings, crayons, and glitter here, but no ticket...")
                bed1()
            elif action == "Back" or action == "back":
                print("Going back to the hallway...")
                sleep(2)
                hallway2()
            else:
                print("Invalid response...")
                bed1()
        def bed2():
            print("You are now in your parent's bedroom. What would you like to do?")
            action = input("Check Bed(bed), Drawer 1(draw1), Drawer 2(draw2), Drawer 3(draw3), Bathroom(bath), or go Back(back)? ")
            if action == "bed":
                print("Checking the bed...")
                sleep(4)
                print("You made the bed messy looking for the ticket only for it to not be there...")
                sleep(2)
                print("Cleaning up the bed...")
                sleep(4)
                bed2()
            elif action == "draw1":
                print("Checking the drawer...")
                sleep(4)
                print("Lots of your mom's clothes here, but no ticket...")
                bed2()
            elif action == "draw2":
                print("Checking the drawer...")
                sleep(4)
                print("Lots of your dad's clothes here, but no ticket...")
                bed2()
            elif action == "draw3":
                print("Checking the drawer...")
                sleep(4)
                print("Lots of junk here, but no ticket...")
                bed2()
            elif action == "bath":
                print("Going to the bathroom...")
                sleep(2)
                print("Checking the bathroom...")
                sleep(3)
                print("The ticket is not in the bathroom...")
                sleep(3)
                print("Leaving the bathroom...")
                sleep(2)
                bed2()
            elif action == "back":
                print("Going back to the hallway...")
                sleep(2)
                hallway2()
            else:
                print("Invalid response...")
                bed2()
        living_room()
start()