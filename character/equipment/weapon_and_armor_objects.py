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
        weapon_object = VersatileRangedWeapon(
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

class Armor:
    def __init__(self, name, armor_type, ac, dex_mod, dex_max, stealth_dis, strength_min):
        self.name = name
        self.armor_type = armor_type
        self.ac = ac
        self.dex_mod = dex_mod
        self.dex_max = dex_max
        self.stealth_disad = stealth_dis
        self.strength_minimum = strength_min

def create_armor(armor_stats_dict):
    armor_list = []
    for armor in armor_stats_dict:
        armor_object = Armor(
            armor,
            armor_stats_dict[armor]["armor type"],
            armor_stats_dict[armor]["ac"],
            armor_stats_dict[armor]["dex mod"],
            armor_stats_dict[armor]["dex max"],
            armor_stats_dict[armor]["stealth disadvantage"],
            armor_stats_dict[armor]["strength requirement"]
                             )
        armor_list.append(armor_object)
    return armor_list
