# Core Abilities and associated Skills

skills_core_stat = {
    "athletics": "strength",
    "acrobatics": "dexterity",
    "sleight of hand": "dexterity",
    "stealth": "dexterity",
    "arcana": "intelligence",
    "history": "intelligence",
    "investigation": "intelligence",
    "nature": "intelligence",
    "religion": "intelligence",
    "animal handling": "wisdom",
    "insight": "wisdom",
    "medicine": "wisdom",
    "perception": "wisdom",
    "survival": "wisdom",
    "deception": "charisma",
    "intimidation": "charisma",
    "performance": "charisma",
    "persuasion": "charisma"
}

# The dictionary of possible proficiencies and their equivalent default status of False.

proficiency_status = {
    'strength': False, 
    'dexterity': False, 
    'constitution': False, 
    'intelligence': False, 
    'wisdom': False, 
    'charisma': False,
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
    'perception': False, 
    'survival': False, 
    'deception': False, 
    'intimidation': False, 
    'performance': False, 
    'persuasion': False, 
    'light armor': False, 
    'medium armor': False, 
    'heavy armor': False, 
    'shield': False,
    'simple weapons': False,
    "martial weapons": False, 
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

# The dictionary of possible background choices

backgrounds = {
    "Acolyte": ["insight", "religion"],
    "Charlatan": ["deception", "sleight of hand"],
    "Criminal": ["deception", "stealth"],
    "Entertainer": ["acrobatics", "performance"],
    "Folk hero": ["animal handling", "survival"],
    "Guild artisan": ["insight", "persuasion"],
    "Hermit": ["medicine", "religion"],
    "Noble": ["history", "persuasion"],
    "Outlander": ["athletics", "survival"],
    "Sage": ["arcana", "history"],
    "Sailor": ["athletics", "perception"],
    "Soldier": ["athletics", "intimidation"],
    "Urchin": ["sleight of hand", "stealth"]
}

# The dictionary of possible damage types

damage_types = {
    "damage type":
    ["acid", 
     "bludgeoning", 
     "cold", 
     "fire", 
     "force", 
     "lightning", 
     "necrotic", 
     "piercing", 
     "poison",
     "psychic",
     "radiant",
     "slashing",
     "thunder"]
}

# The dictionary of possible damage resistances and whether they are active 'True' or not 'False' (default is False)

damage_resistances = {
    'acid': False, 
    'bludgeoning': False, 
    'cold': False, 
    'fire': False, 
    'force': False, 
    'lightning': False, 
    'necrotic': False, 
    'piercing': False, 
    'poison': False, 
    'psychic': False, 
    'radiant': False, 
    'slashing': False, 
    'thunder': False
    }

# spell slot dictionary

spell_slots_dict = {
    "cantrips": 0,
    "level 1": 0,
    "level 2": 0,
    "level 3": 0,
    "level 4": 0,
    "level 5": 0,
    "level 6": 0,
    "level 7": 0,
    "level 8": 0,
    "level 9": 0,
}

# class specific spell lists

spell_list = {
    "barbarian": [],
    "bard": [],
    "cleric": [],
    "druid": [],
    "fighter": [],
    "paladin": [],
    "ranger": [],
    "rogue": [],
    "sorcerer": [],
    "warlock": [],
    "wizard": [],
}

# list of simple and martial weapons

simple_weapons = ['simple weapons', 
                  'club', 
                  'dagger', 
                  'greatclub', 
                  'handaxe', 
                  'javelin', 
                  'light hammer', 
                  'mace', 
                  'quarterstaff', 
                  'sickle', 
                  'spear', 
                  'unarmed strike', 
                  'light crossbow', 
                  'dart', 
                  'short bow', 
                  'sling']

martial_weapons = ['martial weapons', 
                   'battle axe', 
                   'flail', 
                   'glaive', 
                   'great axe', 
                   'great sword', 
                   'halberd', 
                   'lance', 
                   'long sword', 
                   'maul', 
                   'morning star', 
                   'pike', 
                   'rapier', 
                   'scimitar', 
                   'short sword', 
                   'trident', 
                   'war pick', 
                   'warhammer', 
                   'whip', 
                   'blow gun', 
                   'hand crossbow', 
                   'heavy crossbow', 
                   'long bow', 
                   'net']

