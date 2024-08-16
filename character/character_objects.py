from stat_database import *

def get_background_profs(background):
    profs = backgrounds[background]
    return profs

class Character:
    def __init__(self, name, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8, ac=10, level=1, xp=0,):
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
        self.ac = ac + self.get_ability_mod("dexterity")
        self.proficiencies = proficiency_status.copy()
        self.damage_resistance = damage_resistances.copy()
        self.inventory = []
        self.equipped_items = []
        self.spell_casting_ability = None
        self.spell_slots = {}
        self.spell_list = []

    # Universal attribute getter

    def get_attribute(self, attribute):
        attr = getattr(self, attribute)
        print(attr)

    # Methods dealing with the 6 core stats and their associated abilities

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

    def decrease_core_stat(self, core_stat, number):
        if core_stat == "strength":
            self.strength -= number
        elif core_stat == "dexterity":
            self.dex -= number
        elif core_stat == "constitution":
            self.con -= number
        elif core_stat == "intelligence":
            self.int -= number
        elif core_stat == "wisdom":
            self.wis -= number
        elif core_stat == "charisma":
            self.charisma -= number

    def get_skill_core_ability(self, skill):
        return skills_core_stat[skill]

    def get_skill_bonus(self, skill):
        skill_ability = self.get_skill_core_ability(skill)
        if self.proficiencies[skill] == True:
            return self.proficiency_bonus + self.get_ability_mod(skill_ability)
        return self.get_ability_mod(skill_ability)

    # Methods dealing with proficiency dictionaries, i.e. 'self.proficiencies' and 'self.damage_resistance'

    def apply_background_bonus(self):
        background = self.background
        bonus = get_background_profs(background)
        self.gain_proficiency(bonus)

    def gain_damage_resistance(self, damage_type):
        self.damage_resistance[damage_type] = True

    def gain_proficiency(self, prof_list):
        for prof in prof_list:
            self.proficiencies[prof] = True

    def gain_proficiency_choice(self, options_list, number_of_choices):
        pass

    # Methods dealing with inventory and equipping an item
    
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

    # Methods for applying race and subrace stats

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
            self.apply_subrace_bonus(self.sub_race)
    
    def apply_subrace_bonus(self, subrace):
        self.sub_race = subrace.subrace
        if subrace.stat_bonus:
            for stat, bonus in subrace.stat_bonus:
                self.increase_core_stat(stat, bonus)
        if subrace.proficiencies:
            for proficiency in subrace.proficiencies:
                self.gain_proficiency(proficiency)
        if subrace.resistances:
            for resistance in subrace.resistances:
                self.gain_damage_resistance(resistance)
        if subrace.prof_choices:
            self.gain_proficiency_choice(subrace.prof_choices[0], subrace.prof_choices[1])
        if isinstance(subrace, DragonColor):
            self.color = subrace.subrace
            self.breath_shape = subrace.breath_shape
            self.breath_size = subrace.breath_size
            self.breath_type = subrace.breath_type

    # spells and spell list methods

    def populate_spell_list(self, self_class):
        self.spell_list = spell_list[self_class]

    def spell_attack(self):
        return self.proficiency_bonus + self.get_ability_mod(self.spell_casting_ability)
    
    def spell_save_dc(self):
        return 8 + self.spell_attack()
    



class Race:
    def __init__(self, race, speed, stat_bonus, proficiencies, resistances, prof_choices, subraces):
        self.race = race
        self.speed = speed
        self.stat_bonus = stat_bonus
        self.proficiencies = proficiencies
        self.resistance = resistances
        self.prof_choices = prof_choices
        self.subraces = subraces

class SubRace:
    def __init__(self, subrace, stat_bonus, proficiencies, resistances, hp_bonus, speed_bonus):
        self.subrace = subrace
        self.stat_bonus = stat_bonus
        self.proficiencies = proficiencies
        self.resistances = resistances
        self.hp_bonus = hp_bonus
        self.speed_bonus = speed_bonus

class DragonColor(SubRace):
    def __init__(self, subrace, stat_bonus, proficiencies, resistances, hp_bonus, speed_bonus, breath_shape, breath_size, breath_type):
        super().__init__(subrace, stat_bonus, proficiencies, resistances, hp_bonus, speed_bonus)
        self.breath_shape = breath_shape
        self.breath_size = breath_size
        self.breath_type = breath_type
