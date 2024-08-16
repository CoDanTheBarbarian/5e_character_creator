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
        "class abilities": [],
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
        "class abilities": [],
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
        "class abilities": [],
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
        "class abilities": [],
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
        "class abilities": [],
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
        "class abilities": [],
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
        "class abilities": [],
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
        "class abilities": [],
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
        "class abilities": [],
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
        "class abilities": [],
    }
    }