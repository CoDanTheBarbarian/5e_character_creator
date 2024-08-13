# Races and associated Sub Races

races = {
    "Dwarf": 
            ["Hill Dwarf", "Mountain Dwarf"],
    "Elf": 
            ["High Elf", "Wood Elf", "Dark Elf"], 
    "Halfling": 
            ["Lightfoot Halfling", "Stout Halfling"],
    "Human": 
            [],
    "Dragonborn":
            ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White"],
    "Gnome":
        ["Forest Gnome", "Rock Gnome"],
    "Half ELf":
        [],
    "Half Orc":
        [],
    "Tiefling":
        []
}

#backgrounds

backgrounds = {
    "Acolyte Background": "Acolyte",
    "Charlatan Background": "Charlatan",
    "Criminal Background": "Criminal",
    "Entertainer Background": "Entertainer",
    "Folk Hero Background": "Folk Hero",
    "Guild Artisan Background": "Guild Artisan",
    "Hermit Background": "Hermit",
    "Noble Background": "Noble",
    "Outlander Background": "Outlander",
    "Sage Background": "Sage",
    "Sailor Background": "Sailor",
    "Soldier Background": "Soldier",
    "Urchin Background": "Urchin"
}

# Core Abilities and associated Skills

cores_and_skills = {
    "Strength": 
        ["Saving Throw", "Athletics"],
    "Dexterity":
        ["Saving Throw", "Acrobatics", "Sleight of Hand", "Stealth"],
    "Constitution":
        ["Saving Throw"],
    "Intelligence":
        ["Saving Throw", "Arcana", "History", "Investigation", "Nature", "Religion"],
    "Wisdom":
        ["Saving Throw", "Animal Handling", "Insight", "Medicine", "Perception", "Survival"],
    "Charisma":
        ["Saving Throw", "Deception", "Intimidation", "Performance", "Persausion"]
}
proficiency_status = {
    'athletics': False, 
    'acrobatics': False, 
    'sleight of hand': False, 
    'stealth': False, 
    'arcana': False, 
    'history': False, 
    'investigation': False, 
    'nature': False, 
    'religion': False, 
    'animal handling': False, 
    'insight': False, 
    'medicine': False, 
    'percption': False, 
    'survival': False, 
    'deception': False, 
    'intimidation': False, 
    'performance': False, 
    'persuasion': False, 
    'light armor': False, 
    'medium armor': False, 
    'heavy armor': False, 
    'shield': False, 
    'club': False, 
    'dagger': False, 
    'greatclub': False, 
    'handaxe': False, 
    'javelin': False, 
    'light hammer': False, 
    'mace': False, 
    'quarterstaff': False, 
    'sickle': False, 
    'spear': False, 
    'unarmed strike': False, 
    'light crossbow': False, 
    'dart': False, 
    'short bow': False, 
    'sling': False, 
    'battle axe': False, 
    'flail': False, 
    'glaive': False, 
    'great axe': False, 
    'great sword': False, 
    'halberd': False, 
    'lance': False, 
    'long sword': False, 
    'maul': False, 
    'morning star': False, 
    'pike': False, 
    'rapier': False, 
    'scimitar': False, 
    'short sword': False, 
    'trident': False, 
    'war pick': False, 
    'warhammer': False, 
    'whip': False, 
    'blow gun': False, 
    'hand crossbow': False, 
    'heavy crossbow': False, 
    'long bow': False, 
    'net': False
    }
# damage types

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

# weapons and armor

light_armor = "light armor"
medium_armor = "medium armor"
heavy_armor = "heavy armor"
shield = "shield"

simple_weapon = "simple weapon"
martial_weapon = "martial weapon"

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

simple_weapons = [
    club,
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
    sling
    ]

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
    net
    ]

# weapon properties

ammunition = "Ammunition: requires ammo to use, one ammo per use."
finesse = "Finesse: choose whether to use strength or dex modifier for attack and damage rolls"
heavy = "Heavy: small and tiny creatures have disacvantage on attack rolls"
light = "Light: ideal for two weapon fighting"
loading = "Loading: you can fire only one piece of ammo when you use an action, bonus action or reaction, regardless of how many attacks you have."
ranged = "Ranged: ranged weapon, with normal and long range. When attacking beyond normal range you have disadvantage"
reach = "Reach: add 5 feet to your reach while using this weapon"
special = "Special:"
thrown = "Thrown: throw this weapon for a ranged attack, using same modifier as a melee attack with this weapon."
two_handed = "Two Handed: requires two hands to wield"
versatile = "Versatile: can be used with one or two hands, rolling a different damage die for each option"

weapon_properties = [
    ammunition,
    finesse,
    heavy,
    light,
    loading,
    ranged,
    reach,
    special,
    thrown,
    two_handed,
    versatile
]

# create weapon dictionary where each key is a weapon each weapons value is a dictionary of weapon attributes

damage_die = "d"
damage_type = "damage"
bonus_attribute = "+"
properties = "weapon properties"

melee_weapon_stats = {
    club: {damage_die: (4,),
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength,
    properties: [light]},
    
    greatclub: {damage_die: (8,),
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength,
    properties: [two_handed]},
    
    mace: {damage_die: (6,),
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength,
    properties: []},
    
    sickle: {damage_die: (4,),
    damage_type: damage_type_slashing,
    bonus_attribute: strength,
    properties: [light]},
    
    flail: {damage_die: (8,),
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength,
    properties: []},
    
    glaive: {damage_die: (10,),
    damage_type: damage_type_slashing,
    bonus_attribute: strength,
    properties: [heavy, reach, two_handed]},
    
    greataxe: {damage_die: (12,),
    damage_type: damage_type_slashing,
    bonus_attribute: strength,
    properties: [heavy, two_handed]},
    
    greatsword: {damage_die: (6, 6),
    damage_type: damage_type_slashing,
    bonus_attribute: strength,
    properties: [heavy, two_handed]},
    
    halberd: {damage_die: (10,),
    damage_type: damage_type_slashing,
    bonus_attribute: strength,
    properties: [heavy, reach, two_handed]},
    
    lance: {damage_die: (12,),
    damage_type: damage_type_piercing,
    bonus_attribute: strength,
    properties: [reach, special]},
    
    maul: {damage_die: (6, 6),
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength,
    properties: [heavy, two_handed]},
    
    morningstar: {damage_die: (8,),
    damage_type: damage_type_piercing,
    bonus_attribute: strength,
    properties: []},
    
    pike: {damage_die: (10,),
    damage_type: damage_type_piercing,
    bonus_attribute: strength,
    properties: [heavy, reach, two_handed]},

    rapier: {damage_die: (8,),
    damage_type: damage_type_piercing,
    bonus_attribute: (strength, dexterity),
    properties: [finesse]},

    scimitar: {damage_die: (6,),
    damage_type: damage_type_slashing,
    bonus_attribute: (strength, dexterity),
    properties: [finesse, light]},

    shortsword: {damage_die: (6,),
    damage_type: damage_type_piercing,
    bonus_attribute: (strength, dexterity),
    properties: [finesse, light]},

    war_pick: {damage_die: (8,),
    damage_type: damage_type_piercing,
    bonus_attribute: strength,
    properties: []},

    whip: {damage_die: (4,),
    damage_type: damage_type_slashing,
    bonus_attribute: (strength, dexterity),
    properties: [finesse, reach]},
}

range = "range"

ranged_weapon_stats = {
    crossbow_light: {damage_die: (8,),
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    properties: [ammunition, ranged, loading, two_handed],
    range: (80, 320)},

    dart: {damage_die: (4,),
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    properties: [finesse, thrown],
    range: (20, 60)},

    shortbow: {damage_die: (6,),
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    properties: [ammunition, ranged, two_handed],
    range: (80, 320)},

    sling: {damage_die: (4,),
    damage_type: damage_type_bludgeon,
    bonus_attribute: dexterity,
    properties: [ammunition, ranged],
    range: (80, 320)},

    blowgun: {damage_die: (1,),
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    properties: [ammunition, ranged, loading],
    range: (25, 100)},

    crossbow_hand: {damage_die: (6,),
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    properties: [ammunition, ranged, light, loading],
    range: (30, 120)},

    crossbow_heavy: {damage_die: (10,),
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    properties: [ammunition, ranged, heavy, loading, two_handed],
    range: (100, 400)},

    longbow: {damage_die: (8,),
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    properties: [ammunition, ranged, heavy, two_handed],
    range: (150, 600)},

    net: {damage_die: (8,),
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    properties: [special, thrown],
    range: (5, 15)},
}

thrown_weapon_stats = {
    dagger: {damage_die: (4,),
    damage_type: damage_type_piercing,
    bonus_attribute: (strength, dexterity),
    properties: [finesse, light, thrown],
    range: (20, 60)},
    
    handaxe: {damage_die: (6,),
    damage_type: damage_type_slashing,
    bonus_attribute: strength,
    properties: [light, thrown],
    range: (20, 60)},

    javelin: {damage_die: (6,),
    damage_type: damage_type_piercing,
    bonus_attribute: strength,
    properties: [thrown],
    range: (30, 120)},

    light_hammer: {damage_die: (4,),
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength,
    properties: [light, thrown],
    range: (20, 60)},
}

versatile_damage_die = "d"

versatile_melee_weapon_stats = {
    quarterstaff: {damage_die: (6,),
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength,
    properties: [versatile],
    versatile_damage_die: (8,)},

    battleaxe: {damage_die: (8,),
    damage_type: damage_type_slashing,
    bonus_attribute: strength,
    properties: [versatile],
    versatile_damage_die: (10,)},

    longsword: {damage_die: (8, ),
    damage_type: damage_type_slashing,
    bonus_attribute: strength,
    properties: [versatile],
    versatile_damage_die: (10,)},

    warhammer: {damage_die: (8,),
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength,
    properties: [versatile],
    versatile_damage_die: (10,)}
}

versatile_ranged_weapon_stats = {
    trident: {damage_die: (6,),
    damage_type: damage_type_piercing,
    bonus_attribute: strength,
    properties: [thrown, versatile],
    range: (20, 60),
    versatile_damage_die: (8,)},

    spear: {damage_die: (6,),
    damage_type: damage_type_piercing,
    bonus_attribute: strength,
    properties: [thrown, versatile],
    range: (20, 60),
    versatile_damage_die: (8,)}
}

# creates iterables to insert into certain arguments for character class

proficiencies = [light_armor, medium_armor, heavy_armor, shield] + simple_weapons + martial_weapons
saving_throw_proficiencies = {ability: False for ability in core_abilities}
proficiency_dict = {item: False for item in skill_list + proficiencies}
damage_resistances = {damage_type: False for damage_type in damage_types}