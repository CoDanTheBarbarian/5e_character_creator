from character.character_objects import *
def parse_name(name):
    response = input("Character name: " + name + "\nConfirm? (y/n) ")
    if response == "n":
        name = input("What is your new character's name? ")
        parse_name(name)
    elif response == "y":
        print(f"Excellent! Marking {name} to your character sheet.")
    else:
        print("Please enter 'y' or 'n'")
        parse_name(name)
def main():
    print("Welcome to my character creator. Let's make a new character!")
    name = input("First things first, what is your new character's name? ")
    parse_name(name)
    character = Character(name)





    
if __name__ == "__main__":
    main()