from database.stat_database import *
from database.race_subrace import *
from cli import *


def get_background_profs(background):
    profs = backgrounds[background]
    return profs

class Character:
    def __init__(self, name, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8, ac=10, level=1, xp=0,):
        self.name = name
        self.race = None
        self.race_info = []
        self.subrace = None
        self.c_class = None
        self.subclass = None
        self.class_info = []
        self.class_abilities = {}
        self.background = None
        self.speed = 0
        self.hp = 0
        self.hit_die = 0
        self.proficiency_bonus = 2
        self.level = level
        self.xp = xp
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.ac = ac
        self.proficiencies = proficiency_status.copy()
        self.damage_resistance = damage_resistances.copy()
        self.inventory = []
        self.weapon = None
        self.armor = None
        self.shield = None
        self.equipped_items = []
        self.spell_casting_ability = None
        self.spell_slots = spell_slots_dict.copy()
        self.spell_list = []

    def __repr__(self) -> str:
        return self.name
    
    def assign_stat(self, stat, stat_num):
        if stat == "strength":
            self.strength = stat_num
            print(f"{stat} set to {stat_num}")
        elif stat == "dexterity":
            self.dexterity = stat_num
            print(f"{stat} set to {stat_num}")
        elif stat == "constitution":
            self.constitution = stat_num
            print(f"{stat} set to {stat_num}")
        elif stat == "intelligence":
            self.intelligence = stat_num
            print(f"{stat} set to {stat_num}")
        elif stat == "wisdom":
            self.wisdom = stat_num
            print(f"{stat} set to {stat_num}")
        elif stat == "charisma":
            self.charisma = stat_num
            print(f"{stat} set to {stat_num}")

    # Universal attribute getter

    def get_attribute(self, attribute):
        if getattr(self, attribute) == []:
            return None
        return getattr(self, attribute)

    # Methods dealing with the 6 core stats and their associated abilities
    def get_saving_throw(self, core_stat):
        if core_stat == "strength":
            if self.proficiencies["strength"] == True:
                return self.get_ability_mod("strength") + self.proficiency_bonus
            return self.get_ability_mod("strength")
        elif core_stat == "dexterity":
            if self.proficiencies["dexterity"] == True:
                return self.get_ability_mod("dexterity") + self.proficiency_bonus
            return self.get_ability_mod("dexterity")
        elif core_stat == "constitution":
            if self.proficiencies["constitution"] == True:
                return self.get_ability_mod("constitution") + self.proficiency_bonus
            return self.get_ability_mod("constitution")
        elif core_stat == "intelligence":
            if self.proficiencies["intelligence"] == True:
                return self.get_ability_mod("intelligence") + self.proficiency_bonus
            return self.get_ability_mod("intelligence")
        elif core_stat == "wisdom":
            if self.proficiencies["wisdom"] == True:
                return self.get_ability_mod("wisdom") + self.proficiency_bonus
            return self.get_ability_mod("wisdom")
        elif core_stat == "charisma":
            if self.proficiencies["charisma"] == True:
                return self.get_ability_mod("charisma") + self.proficiency_bonus
            return self.get_ability_mod("charisma")

    def get_ability_mod(self, ability):
        ability = getattr(self, ability)
        return (ability // 2) -5
    
    def increase_core_stat(self, core_stat, number):
        if core_stat == "strength":
            self.strength += number
        elif core_stat == "dexterity":
            self.dexterity += number
        elif core_stat == "constitution":
            self.constitution += number
        elif core_stat == "intelligence":
            self.intelligence += number
        elif core_stat == "wisdom":
            self.wisdom += number
        elif core_stat == "charisma":
            self.charisma += number

    def decrease_core_stat(self, core_stat, number):
        if core_stat == "strength":
            self.strength -= number
        elif core_stat == "dexterity":
            self.dexterity -= number
        elif core_stat == "constitution":
            self.constitution -= number
        elif core_stat == "intelligence":
            self.intelligence -= number
        elif core_stat == "wisdom":
            self.wisdom -= number
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
    def get_weapon_proficiencies(self):
        prof = []
        for sw in simple_weapons:
            if self.proficiencies[sw] == True:
                prof.append(sw)
        for mw in martial_weapons:
            if self.proficiencies[mw] == True:
                prof.append(mw)
        return prof
    def apply_background(self, background):
        self.background = background
        bonus = get_background_profs(self.background)
        self.gain_proficiency(bonus)

    def gain_damage_resistance(self, damage_type):
        self.damage_resistance[damage_type] = True

    def gain_proficiency(self, prof_list):
        for prof in prof_list:
            if prof == "simple weapons":
                for i in simple_weapons:
                    self.proficiencies[i] = True
            elif prof == "martial weapons":
                for j in martial_weapons:
                    self.proficiencies[j] = True
            else:
                self.proficiencies[prof] = True

    # Methods dealing with inventory and equipping an item
    
    def add_to_inventory(self, object):
        self.inventory.append(object)

    def remove_from_inventory(self, object):
        self.inventory.remove(object)

    def equip_armor(self, armor):
        if armor.strenth_min:
            if self.get_ability_mod("strength") < armor.strength_min:
                raise Exception("Strength too low to equip")
        self.inventory.remove(armor)
        self.equipped_items.append(armor)
        self.ac = armor.ac
        if armor.dex_mod:
            if armor.dex_max == None:
                self.ac += self.dexterity
            else:
                if self.dex > armor.dex_max:
                    self.ac += armor.dex_max
                self.ac += self.dexterity

    def equip_shield(self, shield):
        if self.weapon:
            if "two handed" in self.weapon.properties and "versatile" not in self.weapons.properties:
                raise Exception("Can not equip shield while wielding a two handed weapon.")
        self.shield = shield

    def equip_weapon(self, weapon):
        if self.weapon:
            unequipped_weapon = self.weapon.pop()
            self.inventory.append(unequipped_weapon)
        self.weapon.append(weapon)

    # Methods for applying race and subrace stats

    def apply_race_bonus(self, race):
        self.race = race.race
        self.speed = race.speed
        if race.stat_bonus:
            for stat, bonus in race.stat_bonus:
                self.increase_core_stat(stat, bonus)
        if race.proficiencies:
            self.gain_proficiency(race.proficiencies)
        if race.resistances:
            for resistance in race.resistances:
                self.gain_damage_resistance(resistance)
        if race.prof_choices:
            print("Looks like you have some options for skill proficiencies to gain from your race.")
            gain_proficiency_choices(self, race.prof_choices[0], race.prof_choices[1])
    
    def apply_subrace_bonus(self, subrace):
        self.subrace = subrace.subrace
        if subrace.stat_bonus:
            for stat, bonus in subrace.stat_bonus:
                self.increase_core_stat(stat, bonus)
        if subrace.proficiencies:
            self.gain_proficiency(subrace.proficiencies)
        if subrace.resistances:
            for resistance in subrace.resistances:
                self.gain_damage_resistance(resistance)
        self.hp_bonus = subrace.hp_bonus
        self.speed_bonus = subrace.speed_bonus
        if self.race == "dragonborn":
            self.race_info.append(f"Breath shape: {subrace.breath_shape}")
            self.race_info.append(f"Breath size: {subrace.breath_size}")
            self.race_info.append(f"Breath type: {subrace.breath_type}")

    # Methods for applying class stats

    def apply_class(self, class_data):
        self.c_class = class_data.class_name
        self.hit_die = class_data.hit_die
        if class_data.proficiencies:
            self.gain_proficiency(class_data.proficiencies)
        if class_data.prof_choice:
            print("Looks like you have some options for skill proficiencies to gain from your class.")
            gain_proficiency_choices(self, class_data.prof_choice[0], class_data.prof_choice[1])
        self.class_info = class_data.class_info
        if class_data.spell_casting_ability:
            self.spell_casting_ability = class_data.spell_casting_ability
        if class_data.spell_slots:
            for spell_type in class_data.spell_slots:
                self.spell_slots[spell_type] = class_data.spell_slots[spell_type]
        self.class_abilities = class_data.class_abilities


    # spells and spell list methods

    def populate_spell_list(self, self_class):
        self.spell_list = spell_list[self_class]

    def spell_attack_bonus(self):
        return self.proficiency_bonus + self.get_ability_mod(self.spell_casting_ability)
    
    def spell_save_dc(self):
        return 8 + self.spell_attack_bonus()
    