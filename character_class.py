strength = "strength"
dexterity = "dexterity"
constitution = "constitution"
intelligence = "intelligence"
wisdom = "wisdom"
charisma = "charisma"
core_abilities = [strength, dexterity, constitution, intelligence, wisdom, charisma]

athletics = "athletics"
acrobatics = "acrobatics"
sleight_of_hand = "sleight of hand"
stealth = "stealth"
arcana = "arcana"
history = "history"
investigation = "investigation"
nature = "nature"
religion = "religion"
animal_handling = "animal handling"
insight = "insight"
medicine = "medicine"
perception = "percption"
survival = "survival"
deception = "deception"
intimidation = "intimidation"
performance = "performance"
persuasion = "persuasion"

skill_list = [
    athletics, 
    acrobatics, 
    sleight_of_hand, 
    stealth, 
    arcana, 
    history, 
    investigation, 
    nature, 
    religion, 
    animal_handling, 
    insight, 
    medicine, 
    perception, 
    survival, 
    deception, 
    intimidation, 
    performance, 
    persuasion]

skill_core_stat = {athletics: strength, 
    acrobatics: dexterity, 
    sleight_of_hand: dexterity, 
    stealth: dexterity, 
    arcana: intelligence, 
    history: intelligence, 
    investigation: intelligence, 
    nature: intelligence, 
    religion: intelligence, 
    animal_handling: wisdom, 
    insight: wisdom, 
    medicine: wisdom, 
    perception: wisdom, 
    survival: wisdom, 
    deception: charisma, 
    intimidation: charisma, 
    performance: charisma, 
    persuasion: charisma}

light_armor = "light armor"
medium_armor = "medium armor"
heavy_armor = "heavy armor"
shield = "shields"

club = "club"
dagger = "dagger"
greatclub = "greatclub"
handaxe = "handaxe"
javelin = "javelin"
light_hammer = "light hammer"
mace = "mace"
quarterstaff = "quarterstaff"
sickle = "sickle"
spear = "spear"
unarmed_strike = "unarmed strike"
crossbow_light = "light crossbow"
dart = "dart"
shortbow = "short bow"
sling = "sling"
simple_weapons = [club,
    dagger,
    greatclub,
    handaxe,
    javelin,
    light_hammer,
    mace,
    quarterstaff,
    sickle,
    spear,
    unarmed_strike,
    crossbow_light,
    dart,
    shortbow,
    sling]
battleaxe = "battle axe"
flail = "flail"
glaive = "glaive"
greataxe = "great axe"
greatsword = "great sword"
halberd = "halberd"
lance = "lance"
longsword = "long sword"
maul = "maul"
morningstar = "morning star"
pike = "pike"
rapier = "rapier"
scimitar = "scimitar"
shortsword = "short sword"
trident = "trident"
war_pick = "war pick"
warhammer = "warhammer"
whip = "whip"
blowgun = "blow gun"
crossbow_hand = "hand crossbow"
crossbow_heavy = "heavy crossbow"
longbow = "long bow"
net = "net"
martial_weapons = [
    battleaxe,
    flail,
    glaive,
    greataxe,
    greatsword,
    halberd,
    lance,
    longsword,
    maul,
    morningstar,
    pike,
    rapier,
    scimitar,
    shortsword,
    trident,
    war_pick,
    warhammer,
    whip,
    blowgun,
    crossbow_hand,
    crossbow_heavy,
    longbow,
    net,]

proficiencies = [light_armor, medium_armor, heavy_armor, shield] + simple_weapons + martial_weapons


damage_type_acid = "acid damage"
damage_type_bludgeon = "bludgeoning damage"
damage_type_cold = "cold damage"
damage_type_fire = "fire damage"
damage_type_force = "force damage"
damage_type_lightning = "lightning damage"
damage_type_necrotic = "necrotic damage"
damage_type_piercing = "piercing damage"
damage_type_poison = "poison damage"
damage_type_psychic = "psychic damage"
damage_type_radiant = "radiant damage"
damage_type_slashing = "slashing damage"
damage_type_thunder = "thunder damage"
damage_types = [
    damage_type_acid,
    damage_type_bludgeon, 
    damage_type_cold, 
    damage_type_fire, 
    damage_type_force, 
    damage_type_lightning, 
    damage_type_necrotic, 
    damage_type_piercing,
    damage_type_poison,
    damage_type_psychic,
    damage_type_radiant,
    damage_type_slashing,
    damage_type_thunder
    ]

saving_throw_proficiencies = {ability: False for ability in core_abilities}
proficiency_dict = {item: False for item in skill_list + proficiencies}
damage_resistances = {damage_type: False for damage_type in damage_types}

dwarf = "dwarf"
elf = "elf"
halfling = "halfling"
human = "human"
dragonborn = "dragonborn"
gnome = "gnome"
half_elf = "half elf"
half_orc = "half orc"
tiefling = "tiefling"
list_of_races = [
    dwarf,
    elf,
    halfling,
    human,
    dragonborn,
    gnome,
    half_elf,
    half_orc,
    tiefling
]
hill_dwarf = "hill dwarf"
mountain_dwarf = "mountain dwarf"
high_elf = "high elf"
wood_elf = "wood elf"
drow_elf= "drow elf"
lightfoot_halfling = "lightfoot halfling"
stout_halfling = "stout halfling"
forest_gnome = "forest gnome"
rock_gnome = "rock nome"
list_of_subraces = [
    hill_dwarf,
    mountain_dwarf,
    high_elf,
    wood_elf,
    drow_elf,
    lightfoot_halfling,
    stout_halfling,
    forest_gnome,
    rock_gnome
]

class Character:
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
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
        self.proficiencies = proficiency_dict.copy()
        self.saving_throws = saving_throw_proficiencies.copy()
        self.damage_resistance = damage_resistances.copy()

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