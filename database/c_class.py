class_name = "class name"  # <-- string
hit_die = "hit_die"  # <-- integer
proficiencies = "proficiencies "  # <-- list of strings
prof_choices = "proficiency choice "  # <-- tuple containing a list of choices and an integer (the number of choices)
class_abilities = "class abilities "  # <-- dictionaries of ability name -> relevant info
class_info = "class info"  # <-- list of class info keywords mapped to an as of yet unmade database
equipment = "starting equipment"  # <-- dictionary of item_type -> strings pointing to weapons and armor database.
spell_casting_ability = "spell casting ability"  # <-- string (one of the six core stats)
spell_slots = "spell slots"  # <-- dictionary with updated values for the character self.spell_slots dictionary
spells_known = "spells known"  # <-- integer, the number of spells to choose from the spell list
rage_charges = "Rage Charges"
bardic_die = "Bardic Die"
domain = "Divine Domain"
channel_divinity_charges = "Channel Divinity Charges"
fighting_style = "Fighting Style"
ki_points = "Ki Points"
lay_on_hands = "Lay on Hands"
sneak_attack = "Sneak Attack Die"
origin = "Sorcerous Origin"
patron = "Patron"

class_abil_desc = {
    "Barbarian": {
        "Unarmored Defense": "While you are not wearing any armor, your AC equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.",
        "Rage": "During your turn in combat, you can rage as a bonus action. While raging you gain the following benefits:\n - You have advantage of Stregth checks and saving throws\n - When you make a strength based weapon attack add 2 to your attack roll\n - You have resistance to bludgeoning, piercing, and slashing damage\nYou can't cast spells while raging. Your rage lasts for 1 minute and ends if you are knocked unconscious or you haven't attacked a hostile creature since your last turn."
    },
    "Bard": {
        "Spellcasting": "You've learned to cast spells using your music.",
        "Bardic Inspiration": "You can use a bonus action to give one creature other than yourself a Bardic Inspiration die to add to their next ability check, attack roll or saving throw in the next 10 minutes. The target can wait until after they roll to use the Bardic die, but must decide before the DM declares success or failure."
    },
    "Cleric": {
        "Spellcasting": "You can cast spells granted to you by your Divine Domain."
    },
    "Druid": {
        "Spellcasting": "You can cast spells drawn from the divine essence of nature itself."
    },
    "Fighter": {
        "Fighting Style": "You have a preferred fighting style.",
        "Second Wind": "On your turn you can use a bonus action to regain hit points eqaul to 1d10 + your fighter level. Once you use this feature you can't use it again until you finish a short or long rest."
    },
    "Monk": {
        "Martial Arts": "You gain benefits while you aren't wearing armor or using and a shield and while you are unarmed or using only monk weapons. Monk weapons are unarmed strikes and simple melee weapons that do don't have the 'two handed' or 'heavy' property."
    },
    "Paladin": {
        "Divine Sense": "On your turn as an action you invoke your divine sense. Until the end of your next turn, you know the location of any celestial, fiend or undead within 60 feet of you that is not behind total cover. You know the type of creature sensed, but not it's identity. Regain all uses on a long rest.",
    },
    "Ranger": {
        "Favored Enemy": "You have advantage on Survival checks to track your favored enemy and on Intelligence checks to recall information about them.",
        "Natural Explorer": "While in your favored terrain, when you make Intelligence and Wisdom checks related to that terrain, your proficiency bonus is doubled if applicable.\nWhile traveling for an hour or more in your favored terrain you gain the following benefits:\n - Unaffected by difficult terrain\n - Can't get lost except by magical means\n - Move stealthily at a normal pace"
    },
    "Rogue": {
        "Expertise": "Choose two proficiencies or one and thieves tools. Your proficiency bonus is doubled when using those proficiencies.",
        "Sneak Attack": "Once per turn you can deal an extra 1d6 damage when you hit and have advantage on the attack roll or if the target has an enemy within 5 feet of it. The attack must use a finesse or a ranged weapon."
    },
    "Sorcerer": {
        "Spellcasting": "You can cast spells from your sorcerous bloodline.",
    },
    "Warlock": {
        "Pact Magic": "You can cast spells granted to you by your Patron."
    },
    "Wizard": {
        "Spellcasting": "You can cast spells from your research into the arcane.",
        "Arcane Recovery": "Once per day when you finish a short rest you can choose expended spell slots to recover. The spell slots can have a combined total of no more than half your wizard level (rounded up)."
    }
}

class_data = {
    "Barbarian": {
        class_name: "Barbarian",
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
        class_info: class_abil_desc["Barbarian"],
        equipment: {
            "weapons": ["great axe", "halberd", "javelin"],
            "armor": [],
        },
        class_abilities: {"rage": 2},
        },
    "Bard": {
        class_name: "Bard",
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
        class_info: class_abil_desc["Bard"],
        equipment: {
            "weapons": ["rapier", "dagger"],
            "armor": ["leather"],
        },
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 4,
            "level 1": 2
            },
        spells_known: 4,
        class_abilities: {"bardic die": 6},
        },
    "Cleric": {
        class_name: "Cleric",
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
        class_info: class_abil_desc["Cleric"],
        equipment: {
            "weapons": ["mace", "light crossbow"],
            "armor": ["scale mail", "shield"],
        },
        spell_casting_ability: "wisdom",
        spell_slots: {
            "cantrips": 3,
            "level 1": 2
            },
        domain: ["list of domains"],
        class_abilities: {"channel divinity": 0},
        },
    "Druid": {
        class_name: "Druid",
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
        class_info: class_abil_desc["Druid"],
        equipment: {
            "weapons": ["scimitar"],
            "armor": ["leather", "shield"],
        },
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 2,
            "level 1": 2
            },
        class_abilities: None,
        },
    "Fighter": {
        class_name: "Fighter",
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
        class_info: class_abil_desc["Fighter"],
        equipment: {
            "weapons": ["great axe", "long bow", "light crossbow", "long sword"],
            "armor": ["leather", "shield",],
        },
        class_abilities: {
            "second wind": 0,
            "fighting style": None
            },
        },
    "Monk": {
        class_name: "Monk",
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
        class_info: class_abil_desc["Monk"],
        equipment: {
            "weapons": ["short sword", "dart"],
            "armor": [],
        },
        class_abilities: {"ki points": 0},
        },
    "Paladin": {
        class_name: "Paladin",
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
        class_info: class_abil_desc["Paladin"],
        equipment: {
            "weapons": ["long sword", "short bow"],
            "armor": ["ring mail", "shield"],
        },
        spell_casting_ability: "charisma",
        spell_slots: {},
        class_abilities: {"lay on hands": "level x 5"},
        },
    "Ranger": {
        class_name: "Ranger",
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
        class_info: class_abil_desc["Ranger"],
        equipment: {
            "weapons": ["short sword", "short sword", "long bow"],
            "armor": ["ring mail"],
        },
        class_abilities: None,
        },
    "Rogue": {
        class_name: "Rogue",
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
        class_info: class_abil_desc["Rogue"],
        equipment: {
            "weapons": ["short sword", "shortbow", "dagger", "dagger"],
            "armor": ["leather"],
        },
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 4,
            "level 1": 2
            },
        class_abilities: {"sneak attack die": 6},
        },
    "Sorcerer": {
        class_name: "Sorcerer",
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
        class_info: class_abil_desc["Sorcerer"],
        equipment: {
            "weapons": ["quarterstaff", "light crossbow", "dagger", "dagger"],
            "armor": [],
        },
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 4,
            "level 1": 2
            },
        spells_known: 2,
        class_abilities: {"sorcerous origin": None},
        },
    "Warlock": {
        class_name: "Warlock",
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
        class_info: class_abil_desc["Warlock"],
        equipment: {
            "weapons": ["light crossbow", "handaxe", "dagger", "dagger"],
            "armor": ["leather"],
        },
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 2,
            "level 1": 2
            },
        spells_known: 2,
        class_abilities: {"pact magic": None},
        },
    "Wizard": {
        class_name: "Wizard",
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
        class_info: class_abil_desc["Wizard"],
        equipment: {
            "weapons": ["quarterstaff"],
            "armor": [],
        },
        spell_casting_ability: "intelligence",
        spell_slots: {
            "cantrips": 3,
            "level 1": 2
            },
        class_abilities: {"arcane recovery": None},
        }
    }

subclass_data = {
    "Barbarian": {},
    "Bard": {},
    "Cleric": {},
    "Druid": {},
    "Fighter": {},
    "Monk": {},
    "Paladin": {},
    "Ranger": {},
    "Rogue": {},
    "Sorcerer": {},
    "Warlock": {},
    "Wizard": {}
}

class Class:
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities):
        self.class_name = class_name
        self.hit_die = hit_die
        self.proficiencies = proficiencies
        self.prof_choice = prof_choice_list
        self.class_info = class_info
        self.starting_equipment = starting_equipment
        self.class_abilities = class_abilities
        self.spell_casting_ability = None
        self.spell_slots = None
        self.spells_known = None

class Barbarian(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)

def create_barbarian(data):
    return Barbarian(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[class_abilities]
    )

class Bard(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, spell_casting_ability, spell_slots, spells_known, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known

def create_bard(data):
    return Bard(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots],
        data[spells_known],
        data[class_abilities]
    )

class Cleric(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, spell_casting_ability, spell_slots, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots

def create_cleric(data):
    return Cleric(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots],
        data[class_abilities]
    )

class Druid(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, spell_casting_ability, spell_slots, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots

def create_druid(data):
    return Druid(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots],
        data[class_abilities]
    )

class Fighter(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)

def create_fighter(data):
    return Fighter(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[class_abilities]
    )

class Monk(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)

def create_monk(data):
    return Monk(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[class_abilities]
    )

class Paladin(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, spell_casting_ability, spell_slots, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots

def create_paladin(data):
    return Paladin(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots],
        data[class_abilities]
    )

class Ranger(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)

def create_ranger(data):
    return Ranger(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[class_abilities]
    )

class Rogue(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)

def create_rogue(data):
    return Rogue(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[class_abilities]
    )

class Sorcerer(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, spell_casting_ability, spell_slots, spells_known, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known

def create_sorcerer(data):
    return Sorcerer(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots],
        data[spells_known],
        data[class_abilities]
    )

class Warlock(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, spell_casting_ability, spell_slots, spells_known, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known

def create_warlock(data):
    return Warlock(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots],
        data[spells_known],
        data[class_abilities]
    )

class Wizard(Class):
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, spell_casting_ability, spell_slots, class_abilities):
        super().__init__(class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots

def create_wizard(data):
    return Wizard(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[spell_casting_ability],
        data[spell_slots],
        data[class_abilities]
    )

class_create_map = {
    "Barbarian": create_barbarian,
    "Bard": create_bard,
    "Cleric": create_cleric,
    "Druid": create_druid,
    "Fighter": create_fighter,
    "Monk": create_monk,
    "Paladin": create_paladin,
    "Ranger": create_ranger,
    "Rogue": create_rogue,
    "Sorcerer": create_sorcerer,
    "Warlock": create_warlock,
    "Wizard": create_wizard
}

def create_class_object(class_name):
    data = class_data[class_name]
    function = class_create_map[class_name]
    return function(data)
