name = "class name"  # <-- string
hit_die = "hit_die"  # <-- integer
proficiencies = "proficiencies "  # <-- list of strings
proficiency_choices = "proficiency choice "  # <-- tuple containing a list of choices and an integer (the number of choices)
class_abilities = "class abilities "  # <-- list of strings pointing to an as of yet unmade class ability database.
equipment = "starting equipment"  # <-- list of strings pointing to weapons and armor database.
spell_casting_ability = "spell casting ability"  # <-- string (one of the six core stats)
spell_slots = "spell slots"  # <-- dictionary with updated values for the character self.spell_slots dictionary
spells_known = "spells known"  # <-- integer, the number of spells to choose from the spell list

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
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 4,
            "level 1": 2
            },
        spells_known: 4,
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
        spell_casting_ability: "wisdom",
        spell_slots: {
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
        spell_casting_ability: "charisma",
        spell_slots: {
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
        spell_casting_ability: "charisma",
        spell_slots: {},
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
        spell_casting_ability: "charisma",
        spell_slots: {
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
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 4,
            "level 1": 2
            },
        spells_known: 2,
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
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 2,
            "level 1": 2
            },
        spells_known: 2,
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
        spell_casting_ability: "intelligence",
        spell_slots: {
            "cantrips": 3,
            "level 1": 2
            },
        }
    }

class Class:
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment):
        self.name = name
        self.hit_die = hit_die
        self.proficiencies = proficiencies
        self.prof_choice = prof_choice_list
        self.class_abilities = class_abilities
        self.starting_equipment = starting_equipment

class Barbarian(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, rage_charges):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.rage = rage_charges

class Bard(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, spells_known, bardic_die):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known
        self.bardic_die = bardic_die

class Cleric(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, domain, channel_divinity_slots):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.domain = domain
        self.channel = channel_divinity_slots

class Druid(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots

class Fighter(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, fighting_style):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.fighting_style = fighting_style

class Monk(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, ki_points):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.ki = ki_points

class Paladin(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots,):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots

class Ranger(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)

class Rogue(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment,sneak_attack_die):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.sneak_attack_die = sneak_attack_die

class Sorcerer(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, spells_known, origin):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known
        self.origin = origin

class Warlock(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, spells_known, patron):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known
        self.patron = patron

class Wizard(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots,):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
