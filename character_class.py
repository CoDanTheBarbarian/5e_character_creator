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

# add a list for damage types and create a dictionary for 'damage type resistances' to add to character init



saving_throw_proficiencies = {ability: False for ability in core_abilities}
proficiency_dict = {item: False for item in skill_list + proficiencies}


class Character:
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        self.name = name
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

    def get_skill_bonus(self, skill):
        if self.proficiencies[skill] == True:
            return self.proficiency_bonus + self.get_ability_mod(skill_core_stat[skill])
        return self.get_ability_mod(skill_core_stat[skill])
    
    def get_saving_throw_mod(self, ability):
        if self.saving_throws[ability] == True:
            return self.proficiency_bonus + self.get_ability_mod(ability)
        return self.get_ability_mod(ability)

class Barbarian(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 12
        self.hp = 12 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, medium_armor, heavy_armor, shield] + simple_weapons + martial_weapons)
        self.gain_saving_throw([strength, constitution])
        # 2 skill proficiencies of choice from animal handling, athletics, intimidation, nature, perception and survival

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

class Fighter(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 10
        self.hp = 10 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, medium_armor, heavy_armor, shield] + simple_weapons + martial_weapons)
        self.gain_saving_throw([strength, constitution])
        # 2 skill proficiences from acrobatics, animal handling, athletics, history, insight, intimidation, perception and survival

class Paladin(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 10
        self.hp = 10 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, medium_armor, heavy_armor, shield] + simple_weapons + martial_weapons)
        self.gain_saving_throw([wisdom, charisma])
        # 2 skill proficiencies from athletics, insight, intimidation, medicine, persuasion and religion

class Ranger(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 10
        self.hp = 10 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, medium_armor, heavy_armor, shield] + simple_weapons + martial_weapons)
        self.gain_saving_throw([strength, dexterity])
        # 3 skill proficiencies from animal handling, athletics, insight, investigation, nature, perception, stealth and survival

class Rogue(Character):
    def __init__(self, name, level=1, xp=0, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        super().__init__(name, level, xp, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.hit_die = 8
        self.hp = 8 + self.get_ability_mod(constitution)
        self.gain_proficiency([light_armor, crossbow_hand, longsword, rapier, shortsword] + simple_weapons)
        self.gain_saving_throw([dexterity, intelligence])
        # 4 from acrobatics, athletics, deception, insight, intimidation, investigation, perception, performance, persuasion, sleight of hand and stealth

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