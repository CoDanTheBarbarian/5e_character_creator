from weapon_and_armor_database import *

class MeleeWeapon:
    def __init__(self, name, weapon_type, damage_die, damage_type, bonus_attribute, properties):
        self.name = name
        self.weapon_type = weapon_type
        self.damage_die = damage_die
        self.damage_type = damage_type
        self.bonus_attribute = bonus_attribute
        self.properties = properties
    
    def get_damage_mod(self):
        return getattr(self, "bonus_attribute")
    
    def __repr__(self) -> str:
        return self.name

def create_melee_weapon(weapon_name):
    weapon_data = melee_weapon_stats[weapon_name]
    weapon_object = MeleeWeapon(
            weapon_name, 
            weapon_data[weapon_type],
            weapon_data[damage_die], 
            weapon_data[damage_type], 
            weapon_data[core_attribute], 
            weapon_data[weapon_properties]
            )
    return weapon_object

class VersatileMeleeWeapon(MeleeWeapon):
    def __init__(self, name, weapon_type, damage_die, damage_type, bonus_attribute, properties, versatile_damage_die):
        super().__init__(name, weapon_type, damage_die, damage_type, bonus_attribute, properties)
        self.versatile_die = versatile_damage_die

    def __repr__(self) -> str:
        return self.name

def create_versatile_melee_weapon(weapon_name):
    weapon_data = versatile_melee_weapon_stats[weapon_name]
    weapon_object= VersatileMeleeWeapon(
            weapon_name, 
            weapon_data[weapon_type],
            weapon_data[damage_die], 
            weapon_data[damage_type], 
            weapon_data[core_attribute], 
            weapon_data[weapon_properties],
            weapon_data[versatile_die]
            )
    return weapon_object
    

class RangedWeapon(MeleeWeapon):
    def __init__(self, name, weapon_type, damage_die, damage_type, bonus_attribute, properties, range):
        super().__init__(name, weapon_type, damage_die, damage_type, bonus_attribute, properties)
        self.range = range

    def __repr__(self) -> str:
        return self.name

def create_ranged_weapon(weapon_name):
    weapon_data = ranged_weapon_stats[weapon_name]
    weapon_object = RangedWeapon(
            weapon_name, 
            weapon_data[weapon_type],
            weapon_data[damage_die], 
            weapon_data[damage_type], 
            weapon_data[core_attribute], 
            weapon_data[weapon_properties],
            weapon_data[range]
            )
    return weapon_object

class VersatileRangedWeapon(RangedWeapon):
    def __init__(self, name, weapon_type, damage_die, damage_type, bonus_attribute, properties, range, versatile_damage_die):
        super().__init__(name, weapon_type, damage_die, damage_type, bonus_attribute, properties, range)
        self.versatile_die = versatile_damage_die

    def __repr__(self) -> str:
        return self.name

def create_versatile_ranged_weapon(weapon_name):
    weapon_data = veratile_ranged_weapon_stats[weapon_name]
    weapon_object = VersatileRangedWeapon(
            weapon_name, 
            weapon_data[weapon_type],
            weapon_data[damage_die], 
            weapon_data[damage_type], 
            weapon_data[core_attribute], 
            weapon_data[weapon_properties],
            weapon_data[range],
            weapon_data[versatile_die]
            )
    return weapon_object

class Armor:
    def __init__(self, name, armor_type, ac, dex_mod, dex_max, stealth_penalty, strength_min):
        self.name = name
        self.armor_type = armor_type
        self.ac = ac
        self.dex_mod = dex_mod
        self.dex_max = dex_max
        self.stealth_penalty = stealth_penalty
        self.strength_min = strength_min

    def __repr__(self) -> str:
        return self.name

def create_armor(armor_name):
    armor_data = armor_stats[armor_name]
    armor_object = Armor(
            armor_name,
            armor_data[armor_type],
            armor_data[ac],
            armor_data[dex_mod],
            armor_data[dex_max],
            armor_data[stealth_penalty],
            armor_data[strength_min]
                             )
    return armor_object

def create_weapon(name):
    if name in melee_weapon_stats.keys():
        return create_melee_weapon(name)
    elif name in versatile_melee_weapon_stats.keys():
        return create_versatile_melee_weapon(name)
    elif name in ranged_weapon_stats.keys():
        return create_ranged_weapon(name)
    elif name in veratile_ranged_weapon_stats.keys():
        return create_versatile_ranged_weapon(name)