import random
import time

#yesList = ["yes", "Yes", "YES", "y", "Y"]
#noList = ["no", "No", "NO", "n", "N"]

#simply for style
def textSpace():
    print("\n-------------------------------------------------------------------------------------------------------------------------------------------\n")

#allows users to name their Hero
def newHeroInfo():
    global heroName
    global heroAge
    print("\nWelcome adventurer to our land!")
    textSpace()
    heroName = input("What should your Hero be called?: ")
    heroAge = int(input("How old is your Hero?: "))
    print("\nWelcome "+ (heroName)+", I see that you\'re", (heroAge),"years old.")  
   
#confirms Hero info is correct
def newHeroInfoCheck():
    done = False     
    while (not done):
        heroInfo = input("Is that correct? (Y/N) ")
        if heroInfo.lower() in {"yes","y"}:
            print("Awesome!")
            done = True                 
        elif heroInfo.lower() in {"no","n"}:
            print("That\'s okay! Please input the correct info.")
            newHeroInfo()
        else:
            print("Please choose a proper reponse. (Y/N)")
            newHeroInfoCheck()

#Class storytime!
def newHeroClassStory():   
    textSpace()
    print("\nWelcome "+ (heroName)+", if you look before you, there are three glowing and floating items...")
    time.sleep(6)
    textSpace()
    print("In front of you, there is a Sword that belonged to a legendary fighter that gave their life in battle to defeat an Evil God...")
    time.sleep(8)
    textSpace()
    print("To your left, you see a Staff that belonged to a legendary mage that has discovered powerful spells, some even so powerful that prevent them from dying of natural cause...")
    time.sleep(10)
    textSpace()
    print("To your right, you see a Bow that belonged to a legendary archer that was known for their nimbleness, stealth, and accuracy. Legend has it, they could hit an apple from over 1000 feet...")
    time.sleep(10)
    textSpace()
    print('As you step closer, a voice from a distance says '+ (heroName)+' before you are weapons that belonged to dangerous warriors in their own craft.')
    print('"The time has come for you to decide in which footsteps you would like to follow. The Fighter, the Mage, or the Archer?"...')
    time.sleep(6)

def newHeroClass():   
    global heroClass 
    heroClass = input("Which warrior do you choose?: ")
    print("\nYou have chosen the mighty "+ (heroClass)+"!")
    newHeroClassCheck
        
   
#confirms Hero class is correct
def newHeroClassCheck():
    done = False     
    while (not done):
        heroClassInfo = input("Is that correct? (Y/N) ")
        if heroClassInfo.lower() in {"yes","y"}:
            print("Congratulations!!! I could sense in your heart that you shared some similarities like the legendary"+ (heroClass)+" warrior.")
            done = True
        elif heroClassInfo.lower() in {"no","n"}:
            textSpace()
            print("That\'s okay! Please carefully choose your warrior.")
            newHeroClass()
        else:
            textSpace()
            print("Please choose a proper choice. (Y/N)")
            newHeroClassCheck()

def main():
    newHeroInfo()
    newHeroInfoCheck()
    newHeroClassStory()
    newHeroClass()
    newHeroClassCheck()


if __name__ == "__main__":
    main()
