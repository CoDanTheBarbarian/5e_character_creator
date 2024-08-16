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

race_stats = {
    "dwarf": {
        "speed": 25, 
        "ability bonus": [("constitution", 2)],
        "proficiencies": ['battle axe', 'handaxe', "light hammer", "warhammer"],
        "resistances": ["poison"],
        "prof choices": [],
        "sub races": races["dwarf"]
        },
    "elf": {
        "speed": 30, 
        "ability bonus": [("dexterity", 2)],
        "proficiencies": ["perception"],
        "resistances": [],
        "prof choices": [],
        "sub races": races["elf"]
        }, 
    "halfling": {
        "speed": 25, 
        "ability bonus": [("dexterity", 2)],
        "proficiencies": [],
        "resistances": [],
        "prof choices": [],
        "sub races": races["halfling"]
        },
    "human": {
        "speed": 30, 
        "ability bonus": [("strength", 1), 
                          ("dexterity", 1), 
                          ("constitution", 1), 
                          ("intelligence", 1), 
                          ("wisdom", 1), 
                          ("charisma", 1)],
        "proficiencies": [],
        "resistances": [],
        "prof choices": [],
        "sub races": races["human"]
        },
    "dragonborn": {
        "speed": 30, 
        "ability bonus": [("strength", 2), ("charisma", 1)],
        "proficiencies": [],
        "resistances": [],
        "prof choices": [],
        "sub races": races["dragonborn"]},
    "gnome": {
        "speed": 25, 
        "ability bonus": [("dexterity", 2)],
        "proficiencies": [],
        "resistances": [],
        "prof choices": [],
        "sub races": races["halfling"]
        },
    "half elf": {
        "speed": 30, 
        "ability bonus": [("charisma", 2)],
        "proficiencies": [],
        "resistances": [],
        "prof choices": [
            (
            ['athletics', 
            'acrobatics', 
            'sleight of hand', 
            'stealth', 
            'arcana', 
            'history', 
            'investigation', 
            'nature', 
            'religion', 
            'animal handling', 
            'insight', 
            'medicine', 
            'perception', 
            'survival', 
            'deception', 
            'intimidation', 
            'performance', 
            'persausion'], 2)],
        "sub races": races["half elf"]
        },
    "half orc": {
        "speed": 30, 
        "ability bonus": [("strength", 2), ("constitution", 1)],
        "proficiencies": [],
        "resistances": [],
        "prof choices": [],
        "sub races": races["half orc"]
        },
    "tiefling": {
        "speed": 30, 
        "ability bonus": [("intelligence", 1), ("charisma", 2)],
        "proficiencies": [],
        "resistances": ["fire"],
        "prof choices": [],
        "sub races": races["tiefling"]
        }
}

sub_race_stats = {
    "hill dwarf": {
        "stat bonus": [("wisdom", 1)],
        "proficiencies": [],
        "resistances": [],
        "hp bonus": "hp += 1 * self.level",
        "speed bonus": None
        },
    "mountain dwarf": {
        "stat bonus": [("strength", 2)],
        "proficiencies": ['light armor', 'medium armor'],
        "resistances": [],
        "hp bonus": None,
        "speed bonus": None
        },
    "high elf": {
        "stat bonus": [("intelligence", 1)],
        "proficiencies": ['long sword', "short sword", "long bow", "short bow"],
        "resistances": [],
        "hp bonus": None,
        "speed bonus": None
        },
    "wood elf": {
        "stat bonus": [("wisdom", 1)],
        "proficiencies": ['long sword', "short sword", "long bow", "short bow"],
        "resistances": [],
        "hp bonus": None,
        "speed bonus": 5
        },
    "dark elf": {
        "stat bonus": [("charisma", 1)],
        "proficiencies": ['rapier', "short sword", "hand crossbow"],
        "resistances": [],
        "hp bonus": None,
        "speed bonus": None
        },
    "lightfoot halfling": {
        "stat bonus": [("charisma", 1)],
        "proficiencies": [],
        "resistances": [],
        "hp bonus": None,
        "speed bonus": None
        },
    "stout halfling": {
        "stat bonus": [("charisma", 1)],
        "proficiencies": [],
        "resistances": ["poison"],
        "hp bonus": None,
        "speed bonus": None
        },
    "black": {
        "stat bonus": [],
        "proficiencies": [],
        "resistances": ["acid"],
        "hp bonus": None,
        "speed bonus": None,
        "breath shape": "line",
        "breath size": (5, 30),
        "breath type": "acid"
        },
    "blue": {
        "stat bonus": [],
        "proficiencies": [],
        "resistances": ["lightning"],
        "hp bonus": None,
        "speed bonus": None,
        "breath shape": "line",
        "breath size": (5, 30),
        "breath type": "lightning"
        },
    "brass": {
        "stat bonus": [],
        "proficiencies": [],
        "resistances": ["fire"],
        "hp bonus": None,
        "speed bonus": None,
        "breath shape": "line",
        "breath size": (5, 30),
        "breath type": "fire"
        },
    "bronze": {
        "stat bonus": [],
        "proficiencies": [],
        "resistances": ["lightning"],
        "hp bonus": None,
        "speed bonus": None,
        "breath shape": "line",
        "breath size": (5, 30),
        "breath type": "lightning"
        },
    "copper": {
        "stat bonus": [],
        "proficiencies": [],
        "resistances": ["acid"],
        "hp bonus": None,
        "speed bonus": None,
        "breath shape": "line",
        "breath size": (5, 30),
        "breath type": "acid"
        },
    "gold": {
        "stat bonus": [],
        "proficiencies": [],
        "resistances": ["fire"],
        "hp bonus": None,
        "speed bonus": None,
        "breath shape": "cone",
        "breath size": (15,),
        "breath type": "fire"
        },
    "green": {
        "stat bonus": [],
        "proficiencies": [],
        "resistances": ["poison"],
        "hp bonus": None,
        "speed bonus": None,
        "breath shape": "cone",
        "breath size": (15,),
        "breath type": "poison"
        },
    "red": {
        "stat bonus": [],
        "proficiencies": [],
        "resistances": ["fire"],
        "hp bonus": None,
        "speed bonus": None,
        "breath shape": "cone",
        "breath size": (15,),
        "breath type": "fire"
        },
    "silver": {
        "stat bonus": [],
        "proficiencies": [],
        "resistances": ["cold"],
        "hp bonus": None,
        "speed bonus": None,
        "breath shape": "cone",
        "breath size": (15,),
        "breath type": "cold"
        },
    "white": {
        "stat bonus": [],
        "proficiencies": [],
        "resistances": ["cold"],
        "hp bonus": None,
        "speed bonus": None,
        "breath shape": "cone",
        "breath size": (15,),
        "breath type": "cold"
        },
    "forest gnome": {
        "stat bonus": [("dexterity", 1)],
        "proficiencies": [],
        "resistances": [],
        "hp bonus": None,
        "speed bonus": None
        },
    "rock gnome": {
        "stat bonus": [("constitution", 1)],
        "proficiencies": [],
        "resistances": [],
        "hp bonus": None,
        "speed bonus": None
        }
}

