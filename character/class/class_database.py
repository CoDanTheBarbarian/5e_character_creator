name = "name"
hit_die = "hit_die"
proficiencies = "proficiencies "
proficiency_choices = "proficiency choice "
class_abilities = "class abilities "
equipment = "starting equipment"


# still need to add 'class abilities' to every class other than barbarian

class_data = {
    "barbarian": {
        name: "barbarian",
        hit_die: 12,
        proficiencies: ["light armor", 
                          "medium armor", 
                          "heavy armor", 
                          "shield", 
                          "simple weapons", 
                          "martial weapons", 
                          "strength",
                          "constitution"],
        proficiency_choices: (
            ["animal handling", 
             "athletics", 
             "intimidation", 
             "nature", 
             "perception", 
             "survival"],
               2),
        class_abilities: ["rage", "unarmored defense"], # need to create a database for class abilities
        equipment: [],
        "rage charges": 2
        },
    "bard": {
        name: "bard",
        hit_die: 8,
        proficiencies: ["light armor", 
                          "simple weapons", 
                          "hand crossbow", 
                          "long sword", 
                          "rapier", 
                          "short sword", 
                          "dexterity", 
                          "charisma"],
        proficiency_choices: (
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
        class_abilities: ["spell casting", "bardic inspiration"],
        equipment: [],
        "spell casting ability": "charisma",
        "spell slots": {
            "cantrips": 4,
            "level 1": 2
            },
        "spells known": 4,
        "bardic die": 6
        },
    "cleric": {
        name: "cleric",
        hit_die: 8,
        proficiencies: ["light armor", 
                          "medium armor", 
                          "shield", 
                          "simple weapons", 
                          "wisdom", 
                          "charisma"],
        proficiency_choices: (
            ["history", 
             "insight", 
             "medicine", 
             "persuasion", 
             "religion"],
            2),
        class_abilities: ["spell casting", "divine domain"],
        equipment: [],
        "spell casting ability": "wisdom",
        "spell slots": {
            "cantrips": 3,
            "level 1": 2
            },
        "domain": ["list of domains"],
        "channel divinity charges": 0
        },
    "druid": {
        name: "druid",
        hit_die: 8,
        proficiencies: ["light armor", 
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
        proficiency_choices: (
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
        class_abilities: ["spell casting", "druidic"],
        equipment: [],
        "spell casting ability": "charisma",
        "spell slots": {
            "cantrips": 2,
            "level 1": 2
            },
        },
    "fighter": {
        name: "fighter",
        hit_die: 10,
        proficiencies: ["light armor", 
                          "medium armor", 
                          'heavy armor', 
                          'shield', 
                          'simple weapons', 
                          'martial_weapons', 
                          'strength', 
                          'constitution'],
        proficiency_choices: (
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
        class_abilities: ["fighting style", "second wind"],
        equipment: [],
        "fighting style": ["list of fighting styles"]
        },
    "monk": {
        name: "monk",
        hit_die: 8,
        proficiencies: ["simple weapons", 
                          "short sword", 
                          "strength",
                          "dexterity"],
        proficiency_choices: (
            ["acrobatics", 
             "athletics", 
             "history", 
             "insight", 
             "religion", 
             "stealth"],
               2),
        class_abilities: ["unarmored defense", "martial arts"],
        equipment: [],
        "ki points": 0
        },
    "paladin": {
        name: "paladin",
        hit_die: 10,
        proficiencies: [
            "light armor", 
            "medium armor", 
            "heavy armor", 
            "shield", 
            "simple weapons", 
            "martial_weapons", 
            "wisdom", 
            "charisma"
        ],
        proficiency_choices: (
            [
                "athletics", 
                "insight", 
                "intimidation", 
                "medicine", 
                "persuasion", 
                "religion"
            ], 2
        ),
        class_abilities: ["spell casting", "divine sense", "lay on hands"],
        equipment: [],
        "spell casting ability": "charisma",
        "spell slots": {},
        "lay on hands": "level x 5"
        },
    "ranger": {
        name: "ranger",
        hit_die: 10,
        proficiencies: [
            "light armor", 
            "medium armor", 
            "heavy armor", 
            "shield", 
            'simple_weapons', 
            'martial_weapons', 
            'strength', 
            'dexterity'
        ],
        proficiency_choices: (
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
        class_abilities: ["favored enemy", "natural explorer"],
        equipment: [],
        },
    "rogue": {
        name: "rogue",
        hit_die: 8,
        proficiencies: [
            "light armor", 
            "hand crossbow", 
            "long sword", 
            "rapier", 
            "short sword", 
            "simple_weapons", 
            "dexterity", 
            "intelligence"
        ],
        proficiency_choices: (
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
        class_abilities: ["expertise", "sneak attack", "thieves' cant"],
        equipment: [],
        "spell casting ability": "charisma",
        "spell slots": {
            "cantrips": 4,
            "level 1": 2
            },
        "sneak attack die": 6
        },
    "sorcerer": {
        name: "sorcerer",
        hit_die: 6,
        proficiencies: [
            'dagger', 
            'dart', 
            'sling', 
            'quarterstaff', 
            'light crossbow', 
            'constitution', 
            'charisma'
        ],
        proficiency_choices: (
            [
                "deception", 
                "insight", 
                "intimidation", 
                "persuasion", 
                "religion"
            ], 2
        ),
        class_abilities: ["spell casting", "sorcerous origin"],
        equipment: [],
        "spell casting ability": "charisma",
        "spell slots": {
            "cantrips": 4,
            "level 1": 2
            },
        "spells known": 2,
        "origin": ["draconic", "wild magic"]
        },
    "warlock": {
        name: "warlock",
        hit_die: 8,
        proficiencies: [
            'light_armor', 
            'simple weapons', 
            'wisdom', 
            'charisma'
        ],
        proficiency_choices: (
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
        class_abilities: ["otherworldy patron", "pact magic"],
        equipment: [],
        "spell casting ability": "charisma",
        "spell slots": {
            "cantrips": 2,
            "level 1": 2
            },
        "spells known": 2,
        "patron": ["list of patrons"]
        },
    "wizard": {
        name: "wizard",
        hit_die: 6,
        proficiencies: [
            'dagger', 
            'dart', 
            'sling', 
            'quarterstaff', 
            'light crossbow', 
            'intelligence', 
            'wisdom'
        ],
        proficiency_choices: (
            [
                "history", 
                "insight", 
                "investigation", 
                "medicine", 
                "religion"
            ], 2
        ),
        class_abilities: ["spell casting", "arcane recovery"],
        equipment: [],
        "spell casting ability": "intelligence",
        "spell slots": {
            "cantrips": 3,
            "level 1": 2
            },
        }
    }
