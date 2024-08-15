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