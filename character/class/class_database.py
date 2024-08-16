# still need to add 'class abilities' to every class other than barbarian

class_data = {
    "barbarian": {
        "name": "barbarian",
        "hit die": 12,
        "proficiencies": ["light armor", 
                          "medium armor", 
                          "heavy armor", 
                          "shield", 
                          "simple weapons", 
                          "martial weapons", 
                          "strength",
                          "constitution"],
        "proficiency choice": (
            ["animal handling", 
             "athletics", 
             "intimidation", 
             "nature", 
             "perception", 
             "survival"],
               2),
        "class abilities": ["rage", "unarmored defense"], # need to create a database for class abilities
        "starting equipment": [],
        "rage charges": 2
        },
    "bard": {
        "name": "bard",
        "hit die": 8,
        "proficiencies": ["light armor", 
                          "simple weapons", 
                          "hand crossbow", 
                          "long sword", 
                          "rapier", 
                          "short sword", 
                          "dexterity", 
                          "charisma"],
        "proficiency choice": (
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
             'persausion'], 
             3),
        "class abilities": ["spell casting", "bardic inspiration"],
        "starting equipment": [],
        "spell casting ability": "charisma",
        "spell slots": {
            "cantrips": 4,
            "level 1": 2
            },
        "spells known": 4,
        "bardic die": 6
        },
    "cleric": {
        "name": "cleric",
        "hit die": 8,
        "proficiencies": ["light armor", 
                          "medium armor", 
                          "shield", 
                          "simple weapons", 
                          "wisdom", 
                          "charisma"],
        "proficiency choice": (
            ["history", 
             "insight", 
             "medicine", 
             "persuasion", 
             "religion"],
            2),
        "class abilities": ["spell casting", "divine domain"],
        "starting equipment": [],
        "spell casting ability": "wisdom",
        "spell slots": {
            "cantrips": 3,
            "level 1": 2
            },
        "domain": ["list of domains"],
        "channel divinity charges": 0
        },
    "druid": {
        "name": "druid",
        "hit die": 8,
        "proficiencies": ["light armor", 
                          "medium armor", 
                          "shield", 
                          "club", 
                          'dagger', 
                          'dart', 
                          'javelin', 
                          'mace', 
                          'quarterstaff', 
                          'scimitar', 
                          'sickle', 
                          'sling', 
                          'spear', 
                          "intelligence", 
                          "wisdom"],
        "proficiency choice": (
            ["arcana", 
             "animal handling", 
             "insight", 
             "medicine", 
             "nature", 
             "perception", 
             "religion", 
             "survival"], 
             2
             ),
        "class abilities": ["spell casting", "druidic"],
        "starting equipment": [],
        "spell casting ability": "charisma",
        "spell slots": {
            "cantrips": 2,
            "level 1": 2
            },
        },
    "fighter": {
        "name": "fighter",
        "hit die": 10,
        "proficiencies": ["light armor", 
                          "medium armor", 
                          'heavy armor', 
                          'shield', 
                          'simple weapons', 
                          'martial_weapons', 
                          'strength', 
                          'constitution'],
        "proficiency choice": (
            [
                "acrobatics", 
                "animal handling", 
                "athletics", 
                "history", 
                "insight", 
                "intimidation", 
                "perception", 
                "survival"
            ], 2
        ),
        "class abilities": ["fighting style", "second wind"],
        "starting equipment": [],
        "fighting style": ["list of fighting styles"]
        },
    "monk": {
        "name": "monk",
        "hit die": 8,
        "proficiencies": ["simple weapons", 
                          "short sword", 
                          "strength",
                          "dexterity"],
        "proficiency choice": (
            ["acrobatics", 
             "athletics", 
             "history", 
             "insight", 
             "religion", 
             "stealth"],
               2),
        "class abilities": ["unarmored defense", "martial arts"],
        "starting equipment": [],
        "ki points": 0
        },
    "paladin": {
        "name": "paladin",
        "hit die": 10,
        "proficiencies": [
            "light armor", 
            "medium armor", 
            "heavy armor", 
            "shield", 
            "simple weapons", 
            "martial_weapons", 
            "wisdom", 
            "charisma"
        ],
        "proficiency choice": (
            [
                "athletics", 
                "insight", 
                "intimidation", 
                "medicine", 
                "persuasion", 
                "religion"
            ], 2
        ),
        "class abilities": ["spell casting", "divine sense", "lay on hands"],
        "starting equipment": [],
        "spell casting ability": "charisma",
        "spell slots": {},
        "lay on hands": "level x 5"
        },
    "ranger": {
        "name": "ranger",
        "hit die": 10,
        "proficiencies": [
            "light armor", 
            "medium armor", 
            "heavy armor", 
            "shield", 
            'simple_weapons', 
            'martial_weapons', 
            'strength', 
            'dexterity'
        ],
        "proficiency choice": (
            [
                "animal handling", 
                "athletics", 
                "insight", 
                "investigation", 
                "nature", 
                "perception", 
                "stealth", 
                "survival"
            ], 3
        ),
        "class abilities": ["favored enemy", "natural explorer"],
        "starting equipment": [],
        },
    "rogue": {
        "name": "rogue",
        "hit die": 8,
        "proficiencies": [
            "light armor", 
            "hand crossbow", 
            "long sword", 
            "rapier", 
            "short sword", 
            "simple_weapons", 
            "dexterity", 
            "intelligence"
        ],
        "proficiency choice": (
            [
                "acrobatics", 
                "athletics", 
                "deception", 
                "insight", 
                "intimidation", 
                "investigation", 
                "perception", 
                "performance", 
                "persuasion", 
                "sleight of hand", 
                "stealth"
            ], 4
        ),
        "class abilities": ["expertise", "sneak attack", "thieves' cant"],
        "starting equipment": [],
        "spell casting ability": "charisma",
        "spell slots": {
            "cantrips": 4,
            "level 1": 2
            },
        "sneak attack die": 6
        },
    "sorcerer": {
        "name": "sorcerer",
        "hit die": 6,
        "proficiencies": [
            'dagger', 
            'dart', 
            'sling', 
            'quarterstaff', 
            'light crossbow', 
            'constitution', 
            'charisma'
        ],
        "proficiency choice": (
            [
                "deception", 
                "insight", 
                "intimidation", 
                "persuasion", 
                "religion"
            ], 2
        ),
        "class abilities": ["spell casting", "sorcerous origin"],
        "starting equipment": [],
        "spell casting ability": "charisma",
        "spell slots": {
            "cantrips": 4,
            "level 1": 2
            },
        "spells known": 2,
        "origin": ["draconic", "wild magic"]
        },
    "warlock": {
        "name": "warlock",
        "hit die": 8,
        "proficiencies": [
            'light_armor', 
            'simple weapons', 
            'wisdom', 
            'charisma'
        ],
        "proficiency choice": (
            [
                "arcana", 
                "deception", 
                "history", 
                "intimidation", 
                "investigation", 
                "nature", 
                "religion"
            ], 2
        ),
        "class abilities": ["otherworldy patron", "pact magic"],
        "starting equipment": [],
        "spell casting ability": "charisma",
        "spell slots": {
            "cantrips": 2,
            "level 1": 2
            },
        "spells known": 2,
        "patron": ["list of patrons"]
        },
    "wizard": {
        "name": "wizard",
        "hit die": 6,
        "proficiencies": [
            'dagger', 
            'dart', 
            'sling', 
            'quarterstaff', 
            'light crossbow', 
            'intelligence', 
            'wisdom'
        ],
        "proficiency choice": (
            [
                "history", 
                "insight", 
                "investigation", 
                "medicine", 
                "religion"
            ], 2
        ),
        "class abilities": ["spell casting", "arcane recovery"],
        "starting equipment": [],
        "spell casting ability": "intelligence",
        "spell slots": {
            "cantrips": 3,
            "level 1": 2
            },
        }
    }
