from database import *

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
        self.proficiencies = proficiency_dict.copy()
        self.saving_throws = saving_throw_proficiencies.copy()
        self.damage_resistance = damage_resistances.copy()
        self.equipment = []

    def get_ability_mod(self, ability):
        if ability == strength:
            return (self.strength // 2) - 5
        if ability == dexterity:
            return (self.dex // 2) - 5
        if ability == constitution:
            return (self.con // 2) - 5
        if ability == intelligence:
            return (self.int // 2) - 5
        if ability == wisdom:
            return (self.wis // 2) - 5
        if ability == charisma:
            return (self.charisma // 2) - 5

    
    def gain_proficiency(self, prof_list):
        for prof in prof_list:
            self.proficiencies[prof] = True

    def gain_saving_throw(self, ability_list):
        for ability in ability_list:
            self.saving_throws[ability] = True

    def gain_damage_resistance(self, damage_type):
        self.damage_resistance[damage_type] = True


    def get_skill_bonus(self, skill):
        if self.proficiencies[skill] == True:
            return self.proficiency_bonus + self.get_ability_mod(skill_core_stat[skill])
        return self.get_ability_mod(skill_core_stat[skill])
    
    def get_saving_throw_mod(self, ability):
        if self.saving_throws[ability] == True:
            return self.proficiency_bonus + self.get_ability_mod(ability)
        return self.get_ability_mod(ability)
    
    def choose_race(self, race):
        if race == dwarf:
            self.race = dwarf
            self.speed = 25
            self.con += 2
            self.gain_proficiency([battleaxe, handaxe, light_hammer, warhammer])
            self.gain_damage_resistance(damage_type_poison)
        if race == elf:
            self.race = elf
            self.speed = 30
            self.dex += 2
            self.gain_proficiency([perception])
        if race == halfling:
            self.race = halfling
            self.speed = 25
            self.dex += 2
        if race == human:
            self.race = human
            self.speed = 30
            self.strength += 1
            self.dex += 1
            self.con += 1
            self.int += 1
            self.wis += 1
            self.charisma +=1
        if race == dragonborn:
            self.race = dragonborn
            self.speed = 30
            self.strength += 2
            self.charisma += 1
        if race == gnome:
            self.race = gnome
            self.speed = 25
            self.int += 2
        if race == half_elf:
            self.race = half_elf
            self.speed = 30
            self.charisma += 2
            # +1 to two abilities of choice, need to figure this out with standard input
            # gain 2 proficeincies from the dictionary 'ability_list', again figure out with standard input
        if race == half_orc:
            self.race = half_orc
            self.speed = 30
            self.strength += 2
            self.con += 1
        if race == tiefling:
            self.race = tiefling
            self.speed = 30
            self.int += 1
            self.charisma += 2
            self.gain_damage_resistance(damage_type_fire)

    def choose_subrace(self, sub_race):
        if sub_race == hill_dwarf:
            self.sub_race = hill_dwarf
            self.wis += 1
            self.hp += 1 * self.level
        if sub_race == mountain_dwarf:
            self.sub_race = mountain_dwarf
            self.strength += 2
            self.gain_proficiency([light_armor, medium_armor])
        if sub_race == high_elf:
            self.sub_race = high_elf
            self.int += 1
            self.gain_proficiency([longsword, shortsword, shortbow, longbow])
        if sub_race == wood_elf:
            self.sub_race = wood_elf
            self.speed = 35
            self.wis += 1
            self.gain_proficiency([longsword, shortsword, shortbow, longbow])
        if sub_race == drow_elf:
            self.sub_race = drow_elf
            self.charisma += 1
            self.gain_proficiency([rapier, shortsword, crossbow_hand])
        if sub_race == lightfoot_halfling:
            self.sub_race = lightfoot_halfling
            self.charisma += 1
        if sub_race == stout_halfling:
            self.sub_race = stout_halfling
            self.con += 1
            self.gain_damage_resistance(damage_type_poison)
        if sub_race == forest_gnome:
            self.sub_race = forest_gnome
            self.dex += 1
        if sub_race == rock_gnome:
            self.sub_race == rock_gnome
            self.con += 1

    def choose_background(self, background):
        if background == background_acolyte:
            self.gain_proficiency([insight, religion])
        if background == background_charlatan:
            self.gain_proficiency([deception, sleight_of_hand])
        if background == background_criminal:
            self.gain_proficiency([deception, stealth])
        if background == background_entertainer:
            self.gain_proficiency([acrobatics, performance])
        if background == background_folk_hero:
            self.gain_proficiency([animal_handling, survival])
        if background == background_guild_artisan:
            self.gain_proficiency([insight, persuasion])
        if background == background_hermit:
            self.gain_proficiency([medicine, religion])
        if background == background_noble:
            self.gain_proficiency([history, persuasion])
        if background == background_outlander:
            self.gain_proficiency([athletics, survival])
        if background == background_sage:
            self.gain_proficiency([arcana, history])
        if background == background_sailor:
            self.gain_proficiency([athletics, perception])
        if background == background_soldier:
            self.gain_proficiency([athletics, intimidation])
        if background == background_urchin:
            self.gain_proficiency([sleight_of_hand, stealth])

# begin defining the child object 'class'(Character)

class Barbarian(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 12
        self.hp = 12 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, medium_armor, heavy_armor, shield] + simple_weapons + martial_weapons)
        self.gain_saving_throw([strength, constitution])
        # 2 skill proficiencies of choice from animal handling, athletics, intimidation, nature, perception and survival
    def choose_race(self, race):
        pass
    def choose_subrace(self, sub_race):
        pass
    def choose_background(self, background):
        pass

class Bard(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 8
        self.hp = 8 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, crossbow_hand, longsword, rapier, shortsword] + simple_weapons)
        self.gain_saving_throw([dexterity, charisma])
        self.spell_casting_ability = charisma
        self.spell_attack = (self.proficiency_bonus + self.get_ability_mod(self.spell_casting_ability))
        self.spell_save_dc = 8 + self.spell_attack
        # 3 skill proficiencies of choice
    def choose_race(self, race):
        pass
    def choose_subrace(self, sub_race):
        pass
    def choose_background(self, background):
        pass

class Cleric(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 8
        self.hp = 8 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, medium_armor, shield] + simple_weapons)
        self.gain_saving_throw([wisdom, charisma])
        self.spell_casting_ability = wisdom
        self.spell_attack = (self.proficiency_bonus + self.get_ability_mod(self.spell_casting_ability))
        self.spell_save_dc = 8 + self.spell_attack
        # 2 skill proficiencies from history, insight, medicine, persuasion and religion
    def choose_race(self, race):
        pass
    def choose_subrace(self, sub_race):
        pass
    def choose_background(self, background):
        pass

class Druid(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 8
        self.hp = 8 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, medium_armor, shield, club, dagger, dart, javelin, mace, quarterstaff, scimitar, sickle, sling, spear])
        self.gain_saving_throw([intelligence, wisdom])
        self.spell_casting_ability = wisdom
        self.spell_attack = (self.proficiency_bonus + self.get_ability_mod(self.spell_casting_ability))
        self.spell_save_dc = 8 + self.spell_attack
        # 2 skill proficiencies from arcana, animal handling, insight, medicine, nature, perception, religion or survival
    def choose_race(self, race):
        pass
    def choose_subrace(self, sub_race):
        pass
    def choose_background(self, background):
        pass

class Fighter(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 10
        self.hp = 10 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, medium_armor, heavy_armor, shield] + simple_weapons + martial_weapons)
        self.gain_saving_throw([strength, constitution])
        # 2 skill proficiences from acrobatics, animal handling, athletics, history, insight, intimidation, perception and survival
    def choose_race(self, race):
        pass
    def choose_subrace(self, sub_race):
        pass
    def choose_background(self, background):
        pass

class Paladin(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 10
        self.hp = 10 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, medium_armor, heavy_armor, shield] + simple_weapons + martial_weapons)
        self.gain_saving_throw([wisdom, charisma])
        # 2 skill proficiencies from athletics, insight, intimidation, medicine, persuasion and religion
    def choose_race(self, race):
        pass
    def choose_subrace(self, sub_race):
        pass
    def choose_background(self, background):
        pass

class Ranger(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 10
        self.hp = 10 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, medium_armor, heavy_armor, shield] + simple_weapons + martial_weapons)
        self.gain_saving_throw([strength, dexterity])
        # 3 skill proficiencies from animal handling, athletics, insight, investigation, nature, perception, stealth and survival
    def choose_race(self, race):
        pass
    def choose_subrace(self, sub_race):
        pass
    def choose_background(self, background):
        pass

class Rogue(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 8
        self.hp = 8 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, crossbow_hand, longsword, rapier, shortsword] + simple_weapons)
        self.gain_saving_throw([dexterity, intelligence])
        # 4 from acrobatics, athletics, deception, insight, intimidation, investigation, perception, performance, persuasion, sleight of hand and stealth
    def choose_race(self, race):
        pass
    def choose_subrace(self, sub_race):
        pass
    def choose_background(self, background):
        pass

class Sorcerer(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 6
        self.hp = 6 + self.get_ability_mod(constitution)
        self.gain_proficiency([dagger, dart, sling, quarterstaff, crossbow_light])
        self.gain_saving_throw([constitution, charisma])
        self.spell_casting_ability = charisma
        self.spell_attack = (self.proficiency_bonus + self.get_ability_mod(self.spell_casting_ability))
        self.spell_save_dc = 8 + self.spell_attack
        # 2 from arcana, deception, insight, intimidation, persuasion and religion
    def choose_race(self, race):
        pass
    def choose_subrace(self, sub_race):
        pass
    def choose_background(self, background):
        pass

class Warlock(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 8
        self.hp = 8 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor] + simple_weapons)
        self.gain_saving_throw([wisdom, charisma])
        self.spell_casting_ability = charisma
        self.spell_attack = (self.proficiency_bonus + self.get_ability_mod(self.spell_casting_ability))
        self.spell_save_dc = 8 + self.spell_attack
        # 2 from arcana, deception, history, intimidation, investigation, nature and religion
    def choose_race(self, race):
        pass
    def choose_subrace(self, sub_race):
        pass
    def choose_background(self, background):
        pass

class Wizard(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 6
        self.hp = 6 + self.get_ability_mod(constitution)
        self.gain_proficiency([dagger, dart, sling, quarterstaff, crossbow_light])
        self.gain_saving_throw([intelligence, wisdom])
        self.spell_casting_ability = intelligence
        self.spell_attack = (self.proficiency_bonus + self.get_ability_mod(self.spell_casting_ability))
        self.spell_save_dc = 8 + self.spell_attack
        # 2 from arcana, history, insight, investigation, medicine and religion
    def choose_race(self, race):
        pass
    def choose_subrace(self, sub_race):
        pass
    def choose_background(self, background):
        pass

# begin the weapons class

# need to write methods that properly handle the tuple 'damage_die' and 'versatile_damage_die' to account for multiple dice

class MeleeWeapon:
    def __init__(self, name, damage_die, damage_type, bonus_attribute, properties):
        self.name = name
        self.damage_die = damage_die
        self.damage_type = damage_type
        self.bonus_attribute = bonus_attribute
        self.properties = properties

class VersatileMeleeWeapon(MeleeWeapon):
    def __init__(self, name, damage_die, damage_type, bonus_attribute, properties, versatile_damage_die):
        super().__init__(name, damage_die, damage_type, bonus_attribute, properties)
        self.two_handed_damage_die = versatile_damage_die

class RangedWeapon(MeleeWeapon):
    def __init__(self, name, damage_die, damage_type, bonus_attribute, properties, range):
        super().__init__(name, damage_die, damage_type, bonus_attribute, properties)
        self.range = range

class VersatileRangedWeapon(RangedWeapon):
    def __init__(self, name, damage_die, damage_type, bonus_attribute, properties, range, versatile_damage_die):
        super().__init__(name, damage_die, damage_type, bonus_attribute, properties, range)
        self.two_handed_damage_die = versatile_damage_die

def create_melee_weapons(melee_stat_dict):
    melee_weapons = []
    for weapon in melee_stat_dict:
        weapon_object = MeleeWeapon(
            weapon, 
            melee_stat_dict[weapon][damage_die], 
            melee_stat_dict[weapon][damage_type], 
            melee_stat_dict[weapon][bonus_attribute], 
            melee_stat_dict[weapon][properties]
            )
        melee_weapons.append(weapon_object)
    return melee_weapons

def create_versatile_melee_weapons(versatile_melee_stat_dict):
    versatile_melee_weapons = []
    for weapon in versatile_melee_stat_dict:
        weapon_object = VersatileMeleeWeapon(
            weapon, 
            versatile_melee_stat_dict[weapon][damage_die], 
            versatile_melee_stat_dict[weapon][damage_type], 
            versatile_melee_stat_dict[weapon][bonus_attribute], 
            versatile_melee_stat_dict[weapon][properties], 
            versatile_melee_stat_dict[weapon][versatile_damage_die]
            )
        versatile_melee_weapons.append(weapon_object)
    return versatile_melee_weapons

def create_ranged_weapons(ranged_stat_dict):
    ranged_weapons = []
    for weapon in ranged_stat_dict:
        weapon_object = RangedWeapon(
            weapon, 
            ranged_stat_dict[weapon][damage_die], 
            ranged_stat_dict[weapon][damage_type], 
            ranged_stat_dict[weapon][bonus_attribute], 
            ranged_stat_dict[weapon][properties], 
            ranged_stat_dict[weapon][range]
            )
        ranged_weapons.append(weapon_object)
    return ranged_weapons

def create_versatile_ranged_weapons(versatile_ranged_stat_dict):
    versatile_ranged_weapons = []
    for weapon in versatile_ranged_stat_dict:
        weapon_object = VersatileRangedWeapon(
            weapon, 
            versatile_ranged_stat_dict[weapon][damage_die], 
            versatile_ranged_stat_dict[weapon][damage_type], 
            versatile_ranged_stat_dict[weapon][bonus_attribute],
            versatile_ranged_stat_dict[weapon][properties], 
            versatile_ranged_stat_dict[weapon][range], 
            versatile_ranged_stat_dict[weapon][versatile_damage_die]
            )
        versatile_ranged_weapons.append(weapon_object)
    return versatile_ranged_weapons