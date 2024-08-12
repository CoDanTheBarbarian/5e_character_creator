from character_class import *

class Dwarf(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.speed = 25
        self.__con += 2
        
class HillDwarf(Dwarf):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.__wis += 1
        if self.__con > 0:
            self.hp += (self.__con * 1)

class MountainDwarf(Dwarf):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.__strength += 2
        self.proficiencies["light armor"] = True
        self.proficiencies["medium armor"] = True

class Elf(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.speed = 30
        self.__dex += 2
        self.proficiencies["perception"] = True

class HighElf(Elf):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.__int += 1

class WoodElf(Elf):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.__wis += 1
        self.speed = 35

class Drow(Elf):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.__charisma += 1

class Halfling(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.__dex += 2
        self.speed = 25

class Lightfoot(Halfling):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.__charisma += 1

class Stout(Halfling):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.__con += 1

class Human(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.__strength += 1
        self.__dex += 1
        self.__con += 1
        self.__int += 1
        self.__wis += 1
        self.__charisma += 1
        self.speed = 30

class Dragonborn(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.speed = 30
        self.__strength += 2
        self.__charisma += 1

class Gnome(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.speed = 25
        self.__int += 2

class ForestGnome(Gnome):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.__dex += 1

class RockGnome(Gnome):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.__con += 1

class HalfElf(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.speed = 30
        self.__charisma += 2
        # +1 to two abilities of choice, need to figure this out with standard input
        # gain 2 proficeincies from the dictionary 'ability_list', again figure out with standard input

class HalfOrc(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.speed = 30
        self.__strength += 2
        self.__con += 1

class Tiefling(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.speed = 30
        self.__int += 1
        self.__charisma += 2
        # add a list for damage resistances so you can add fire resistance to that list. Initialize that list in the character class