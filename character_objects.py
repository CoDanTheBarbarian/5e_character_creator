from stat_database import *

def get_background_profs(background):
    profs = backgrounds[background]
    return profs

class Character:
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8, ac=10):
        self.name = name
        self.race = None
        self.sub_race = None
        self.background = None
        self.speed = 0
        self.hp = 0
        self.proficiency_bonus = 2
        self.level = level
        self.xp = xp
        self.strength = strength
        self.dex = dexterity
        self.con = constitution
        self.int = intelligence
        self.wis = wisdom
        self.charisma = charisma
        self.ac = ac
        self.proficiencies = proficiency_status.copy()
        self.damage_resistance = damage_resistances.copy()
        self.inventory = []
        self.equipped_items = []
        self.spell_slots = []
        self.spell_list = []

    def apply_background_bonus(self):
        background = self.background
        bonus = get_background_profs(background)
        self.gain_proficiency(bonus)

    def get_ability_mod(self, ability):
        ability = getattr(self, ability)
        return (ability // 2) -5
    
    def increase_core_stat(self, core_stat, number):
        if core_stat == "strength":
            self.strength += number
        elif core_stat == "dexterity":
            self.dex += number
        elif core_stat == "constitution":
            self.con += number
        elif core_stat == "intelligence":
            self.int += number
        elif core_stat == "wisdom":
            self.wis += number
        elif core_stat == "charisma":
            self.charisma += number

    def get_skill_core_ability(self, skill):
        return skills_core_stat[skill]
    
    def gain_proficiency(self, prof_list):
        for prof in prof_list:
            self.proficiencies[prof] = True

    def gain_damage_resistance(self, damage_type):
        self.damage_resistance[damage_type] = True

    def get_skill_bonus(self, skill):
        skill_ability = self.get_skill_core_ability(skill)
        if self.proficiencies[skill] == True:
            return self.proficiency_bonus + self.get_ability_mod(skill_ability)
        return self.get_ability_mod(skill_ability)
    
    def add_to_inventory(self, object):
        self.inventory.append(object)

    def remove_from_inventory(self, object):
        self.inventory.remove(object)

    def equip_armor(self, armor):
        self.inventory.remove(armor)
        self.equipped_items.append(armor)
        self.ac = armor.ac
        if armor.dex_mod:
            if armor.dex_max == None:
                self.ac += self.dex
            else:
                if self.dex > armor.dex_max:
                    self.ac += armor.dex_max
                self.ac += self.dex

    def gain_proficiency_choice(self, options_list, number_of_choices):
        pass
    
    def apply_race_bonus(self, race):
        self.race = race.race
        self.speed = race.speed
        if race.stat_bonus:
            for stat, bonus in race.stat_bonus:
                self.increase_core_stat(stat, bonus)
        if race.proficiencies:
            for proficiency in race.proficiencies:
                self.gain_proficiency(proficiency)
        if race.resistances:
            for resistance in race.resistances:
                self.gain_damage_resistance(resistance)
        if race.prof_choices:
            self.gain_proficiency_choice(race.prof_choices[0], race.prof_choices[1])
        if race.subraces:
            pass # not sure how to finish this without an apply sub race method.