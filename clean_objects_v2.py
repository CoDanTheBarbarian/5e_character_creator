from clean_database_v2 import *
from weapon_and_armor_database import *

class Character:
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8, ac=10):
        self.name = name
        self.race = None
        self.sub_race = None
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

    def get_ability_mod(self, ability):
        ability = getattr(self, ability)
        return (ability // 2) -5
    
    def get_core_ability(self, skill):
        return skills_core_stat[skill]
    
    def gain_proficiency(self, prof_list):
        for prof in prof_list:
            self.proficiencies[prof] = True

    def gain_damage_resistance(self, damage_type):
        self.damage_resistance[damage_type] = True

    def get_skill_bonus(self, skill):
        skill_ability = self.get_core_ability(skill)
        if self.proficiencies[skill] == True:
            return self.proficiency_bonus + self.get_ability_mod(skill_ability)
        return self.get_ability_mod(skill_ability)
            
    
class MeleeWeapon:
    def __init__(self, name, weapon_type, damage_die, damage_type, bonus_attribute, properties):
        self.name = name
        self.weapon_type = weapon_type
        self.damage_die = damage_die
        self.damage_type = damage_type
        self.bonus_attribute = bonus_attribute
        self.properties = properties

def create_melee_weapons(melee_stat_dict):
    melee_weapons = []
    for weapon in melee_stat_dict:
        weapon_object = MeleeWeapon(
            weapon, 
            melee_stat_dict[weapon]['weapon type'],
            melee_stat_dict[weapon]['damage die'], 
            melee_stat_dict[weapon]['damage type'], 
            melee_stat_dict[weapon]['bonus attribute'], 
            melee_stat_dict[weapon]['properties']
            )
        melee_weapons.append(weapon_object)
    return melee_weapons

class VersatileMeleeWeapon(MeleeWeapon):
    def __init__(self, name, weapon_type, damage_die, damage_type, bonus_attribute, properties, versatile_damage_die):
        super().__init__(name, weapon_type, damage_die, damage_type, bonus_attribute, properties)
        self.two_handed_damage_die = versatile_damage_die

def create_versatile_melee_weapons(versatile_melee_stat_dict):
    versatile_melee_weapons = []
    for weapon in versatile_melee_stat_dict:
        weapon_object = VersatileMeleeWeapon(
            weapon, 
            versatile_melee_stat_dict[weapon]['weapon type'],
            versatile_melee_stat_dict[weapon]['damage die'], 
            versatile_melee_stat_dict[weapon]['damage type'], 
            versatile_melee_stat_dict[weapon]['bonus attribute'], 
            versatile_melee_stat_dict[weapon]['properties'],
            versatile_melee_stat_dict[weapon]['two handed damage die']
            )
        versatile_melee_weapons.append(weapon_object)
    return versatile_melee_weapons

class RangedWeapon(MeleeWeapon):
    def __init__(self, name, weapon_type, damage_die, damage_type, bonus_attribute, properties, range):
        super().__init__(name, weapon_type, damage_die, damage_type, bonus_attribute, properties)
        self.range = range

def create_ranged_weapons(ranged_stat_dict):
    ranged_weapons = []
    for weapon in ranged_stat_dict:
        weapon_object = RangedWeapon(
            weapon, 
            ranged_stat_dict[weapon]['weapon type'],
            ranged_stat_dict[weapon]['damage die'], 
            ranged_stat_dict[weapon]['damage type'], 
            ranged_stat_dict[weapon]['bonus attribute'], 
            ranged_stat_dict[weapon]['properties'],
            ranged_stat_dict[weapon]['range']
            )
        ranged_weapons.append(weapon_object)
    return ranged_weapons

class VersatileRangedWeapon(RangedWeapon):
    def __init__(self, name, weapon_type, damage_die, damage_type, bonus_attribute, properties, range, versatile_damage_die):
        super().__init__(name, weapon_type, damage_die, damage_type, bonus_attribute, properties, range)
        self.two_handed_damage_die = versatile_damage_die

def create_versatile_ranged_weapons(versatile_ranged_stat_dict):
    versatile_ranged_weapons = []
    for weapon in versatile_ranged_stat_dict:
        weapon_object = RangedWeapon(
            weapon, 
            versatile_ranged_stat_dict[weapon]['weapon type'],
            versatile_ranged_stat_dict[weapon]['damage die'], 
            versatile_ranged_stat_dict[weapon]['damage type'], 
            versatile_ranged_stat_dict[weapon]['bonus attribute'], 
            versatile_ranged_stat_dict[weapon]['properties'],
            versatile_ranged_stat_dict[weapon]['range'],
            versatile_ranged_stat_dict[weapon]['two handed damage die']
            )
        versatile_ranged_weapons.append(weapon_object)
    return versatile_ranged_weapons