# Races and associated Sub Races

races = {
    "dwarf": 
            ["hill dwarf", "mountain dwarf"],
    "elf": 
            ["high elf", "wood elf", "dark elf"], 
    "halfling": 
            ["lightfoot halfling", "stout halfling"],
    "human": 
            [],
    "dragonborn":
            ["black", "blue", "brass", "bronze", "copper", "gold", "green", "red", "silver", "white"],
    "gnome":
        ["forest gnome", "rock gnome"],
    "half elf":
        [],
    "half orc":
        [],
    "tiefling":
        []
}

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
    "persausion": "charisma"
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

# The dictionary of possible background choices

backgrounds = {
    "background": 
    ["acolyte", 
     "charlatan", 
     "criminal", 
     "entertainer", 
     "folk hero",
     "guild artisan",
     "hermit",
     "noble",
     "outlander",
     "sage",
     "sailor",
     "soldier",
     "urchin"] 
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
    