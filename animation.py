
import time
from os import system, name

def hand():
    print("       *******        ")
    print("      * #   # *       ")
    print("     *    ^    *      ")
    print("       * === *        ")
    print("       *******        ")
    print("          ||          ")
    print("    ======||======    ")
    print("          ||          ")
    print("          ||          ")
    print("          /\          ")
    print("         /  \         ")
    print("       _/    \_       ")

def hand1():
    print("       *******        ")
    print("      * #   # *       ")
    print("     *    ^    *      ")
    print("       * --- *        ")
    print("       *******        ")
    print("          ||          ")
    print("          ||          ")
    print("         /||\         ")
    print("        / || \        ")
    print("       /  /\  \       ")
    print("         /  \         ")
    print("       _/    \_       ")

i =1
while i<50:
    system('cls')
    hand()
    time.sleep(.5)
    system('cls')
    hand1()
    time.sleep(.5)
    i+=1

# use command for execute