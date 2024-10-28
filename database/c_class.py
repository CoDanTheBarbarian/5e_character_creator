class_name = "class name"  # <-- string
hit_die = "hit_die"  # <-- integer
proficiencies = "proficiencies "  # <-- list of strings
prof_choices = "proficiency choice "  # <-- tuple containing a list of choices and an integer (the number of choices)
class_abilities = "class abilities "  # <-- list of strings pointing to an as of yet unmade class ability database.
equipment = "starting equipment"  # <-- list of strings pointing to weapons and armor database.
spell_casting_ability = "spell casting ability"  # <-- string (one of the six core stats)
spell_slots = "spell slots"  # <-- dictionary with updated values for the character self.spell_slots dictionary
spells_known = "spells known"  # <-- integer, the number of spells to choose from the spell list
rage_charges = "rage charges"
bardic_die = "bardic die"
domain = "domain"
channel_divinity_charges = "channel divinity charges"
fighting_style = "fighting style"
ki_points = "ki points"
lay_on_hands = "lay on hands"
sneak_attack = "sneak attack die"
origin = "sorcerous origin"
patron = "patron"

class_data = {
    "barbarian": {
        class_name: "barbarian",
        hit_die: 12,
        proficiencies: ["light armor", 
                          "medium armor", 
                          "heavy armor", 
                          "shield", 
                          "simple weapons", 
                          "martial weapons", 
                          "strength",
                          "constitution"],
        prof_choices: (
            ["animal handling", 
             "athletics", 
             "intimidation", 
             "nature", 
             "perception", 
             "survival"],
               2),
        class_abilities: ["rage", "unarmored defense"], # need to create a database for class abilities
        equipment: ["testing", "testing", "one two three"],
        rage_charges: 2
        },
    "bard": {
        class_name: "bard",
        hit_die: 8,
        proficiencies: ["light armor", 
                          "simple weapons", 
                          "hand crossbow", 
                          "long sword", 
                          "rapier", 
                          "short sword", 
                          "dexterity", 
                          "charisma"],
        prof_choices: (
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
             'persuasion'], 
             3),
        class_abilities: ["spell casting", "bardic inspiration"],
        equipment: ["testing", "testing", "one two three"],
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 4,
            "level 1": 2
            },
        spells_known: 4,
        bardic_die: 6
        },
    "cleric": {
        class_name: "cleric",
        hit_die: 8,
        proficiencies: ["light armor", 
                          "medium armor", 
                          "shield", 
                          "simple weapons", 
                          "wisdom", 
                          "charisma"],
        prof_choices: (
            ["history", 
             "insight", 
             "medicine", 
             "persuasion", 
             "religion"],
            2),
        class_abilities: ["spell casting", "divine domain"],
        equipment: ["testing", "testing", "one two three"],
        spell_casting_ability: "wisdom",
        spell_slots: {
            "cantrips": 3,
            "level 1": 2
            },
        domain: ["list of domains"],
        channel_divinity_charges: 0
        },
    "druid": {
        class_name: "druid",
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
        prof_choices: (
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
        equipment: ["testing", "testing", "one two three"],
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 2,
            "level 1": 2
            },
        },
    "fighter": {
        class_name: "fighter",
        hit_die: 10,
        proficiencies: ["light armor", 
                          "medium armor", 
                          'heavy armor', 
                          'shield', 
                          'simple weapons', 
                          'martial_weapons', 
                          'strength', 
                          'constitution'],
        prof_choices: (
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
        equipment: ["testing", "testing", "one two three"],
        fighting_style: ["list of fighting styles"]
        },
    "monk": {
        class_name: "monk",
        hit_die: 8,
        proficiencies: ["simple weapons", 
                          "short sword", 
                          "strength",
                          "dexterity"],
        prof_choices: (
            ["acrobatics", 
             "athletics", 
             "history", 
             "insight", 
             "religion", 
             "stealth"],
               2),
        class_abilities: ["unarmored defense", "martial arts"],
        equipment: ["testing", "testing", "one two three"],
        ki_points: 0
        },
    "paladin": {
        class_name: "paladin",
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
        prof_choices: (
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
        equipment: ["testing", "testing", "one two three"],
        spell_casting_ability: "charisma",
        spell_slots: {},
        lay_on_hands: "level x 5"
        },
    "ranger": {
        class_name: "ranger",
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
        prof_choices: (
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
        equipment: ["testing", "testing", "one two three"],
        },
    "rogue": {
        class_name: "rogue",
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
        prof_choices: (
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
        equipment: ["testing", "testing", "one two three"],
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 4,
            "level 1": 2
            },
        sneak_attack: 6
        },
    "sorcerer": {
        class_name: "sorcerer",
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
        prof_choices: (
            [
                "deception", 
                "insight", 
                "intimidation", 
                "persuasion", 
                "religion"
            ], 2
        ),
        class_abilities: ["spell casting", "sorcerous origin"],
        equipment: ["testing", "testing", "one two three"],
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 4,
            "level 1": 2
            },
        spells_known: 2,
        origin: ["draconic", "wild magic"]
        },
    "warlock": {
        class_name: "warlock",
        hit_die: 8,
        proficiencies: [
            'light_armor', 
            'simple weapons', 
            'wisdom', 
            'charisma'
        ],
        prof_choices: (
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
        equipment: ["testing", "testing", "one two three"],
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 2,
            "level 1": 2
            },
        spells_known: 2,
        patron: ["list of patrons"]
        },
    "wizard": {
        class_name: "wizard",
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
        prof_choices: (
            [
                "history", 
                "insight", 
                "investigation", 
                "medicine", 
                "religion"
            ], 2
        ),
        class_abilities: ["spell casting", "arcane recovery"],
        equipment: ["testing", "testing", "one two three"],
        spell_casting_ability: "intelligence",
        spell_slots: {
            "cantrips": 3,
            "level 1": 2
            },
        }
    }

class Class:
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment):
        self.class_name = class_name
        self.hit_die = hit_die
        self.proficiencies = proficiencies
        self.prof_choice = prof_choice_list
        self.class_abilities = class_abilities
        self.starting_equipment = starting_equipment

class Barbarian(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, rage_charges):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.rage = rage_charges

def create_barbarian(data):
    return Barbarian(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment],
        data[rage_charges]
    )

class Bard(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, spells_known, bardic_die):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known
        self.bardic_die = bardic_die

def create_bard(data):
    return Bard(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots],
        data[spells_known],
        data[bardic_die]
    )

class Cleric(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, domain, channel_divinity_slots):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.domain = domain
        self.channel = channel_divinity_slots

def create_cleric(data):
    return Cleric(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots],
        data[domain],
        data[channel_divinity_charges]
    )

class Druid(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots

def create_druid(data):
    return Druid(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots]
    )

class Fighter(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, fighting_style):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.fighting_style = fighting_style

def create_fighter(data):
    return Fighter(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment],
        data[fighting_style]
    )

class Monk(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, ki_points):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.ki = ki_points

def create_monk(data):
    return Monk(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment],
        data[ki_points]
    )

class Paladin(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots,):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots

def create_paladin(data):
    return Paladin(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots]
    )

class Ranger(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)

def create_ranger(data):
    return Ranger(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment]
    )

class Rogue(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment,sneak_attack_die):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.sneak_attack_die = sneak_attack_die

def create_rogue(data):
    return Rogue(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment],
        data[sneak_attack]
    )

class Sorcerer(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, spells_known, origin):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known
        self.origin = origin

def create_sorcerer(data):
    return Sorcerer(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots],
        data[spells_known],
        data[origin]
    )

class Warlock(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, spells_known, patron):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known
        self.patron = patron

def create_warlock(data):
    return Warlock(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots],
        data[spells_known],
        data[patron]
    )

class Wizard(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots,):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots

def create_wizard(data):
    return Wizard(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_abilities],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots]
    )

class_create_map = {
    "barbarian": create_barbarian,
    "bard": create_bard,
    "cleric": create_cleric,
    "druid": create_druid,
    "fighter": create_fighter,
    "monk": create_monk,
    "paladin": create_paladin,
    "ranger": create_ranger,
    "rogue": create_rogue,
    "sorcerer": create_sorcerer,
    "warlock": create_warlock,
    "wizard": create_wizard
}

def create_class_object(class_name):
    data = class_data[class_name]
    function = class_create_map[class_name]
    return function(data)
