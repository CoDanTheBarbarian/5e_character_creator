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
favored_terrain = "Favored Terrain"
favored_enemy = "Favored Enemy"
sneak_attack = "Sneak Attack Die"
origin = "Sorcerous Origin"
patron = "Patron"
arcane_recovery = "Arcane Recovery"

class_abil_desc = {
    "Barbarian": {
        "Unarmored Defense": "While you are not wearing any armor, your AC equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.",
        "Rage": "During your turn in combat, you can rage as a bonus action. While raging you gain the following benefits:\n - You have advantage of Stregth checks and saving throws\n - When you make a strength based weapon attack add 2 to your attack roll\n - You have resistance to bludgeoning, piercing, and slashing damage\nYou can't cast spells while raging. Your rage lasts for 1 minute and ends if you are knocked unconscious or you haven't attacked a hostile creature since your last turn."
    },
    "Bard": {
        "Spellcasting": "You've learned to cast spells using your music.",
        "Bardic Inspiration": "You can use a bonus action to give one creature other than yourself a Bardic Inspiration die to add to their next ability check, attack roll or saving throw in the next 10 minutes. The target can wait until after they roll to use the Bardic die, but must decide before the DM declares success or failure. You regain any expended uses on a long rest."
    },
    "Cleric": {
        "Spellcasting": "You can cast spells granted to you by your Divine Domain. Your domain spells are always prepared and don't count against the number of spells you can have prepared."
    },
    "Druid": {
        "Spellcasting": "You can cast spells drawn from the divine essence of nature itself."
    },
    "Fighter": {
        "Second Wind": "On your turn you can use a bonus action to regain hit points eqaul to 1d10 + your fighter level. Once you use this feature you can't use it again until you finish a short or long rest."
    },
    "Monk": {
        "Martial Arts": "You gain benefits while you aren't wearing armor or using and a shield and while you are unarmed or using only monk weapons. Monk weapons are unarmed strikes and simple melee weapons that do don't have the 'two handed' or 'heavy' property."
    },
    "Paladin": {
        "Divine Sense": "On your turn as an action you invoke your divine sense. Until the end of your next turn, you know the location of any celestial, fiend or undead within 60 feet of you that is not behind total cover. You know the type of creature sensed, but not it's identity. Regain all uses on a long rest.",
        "Lay on Hands": "As an action, you can can touch a creature and restore their hit points up to the amount in your pool, or expend 5 hit points from your pool to heal that creature of a disease or poison. Your pool is 5 times your paladin level and replenishes on a long rest."
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
        class_abilities: {rage_charges: 2},
        spell_casting_ability: None,
        spell_slots: None,
        spells_known: None
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
        class_abilities: {bardic_die: "d6"},
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
        spells_known: None,
        class_abilities: {channel_divinity_charges: 0},
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
        spells_known: None,
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
                          'martial weapons', 
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
            fighting_style: None
            },
        spell_casting_ability: None,
        spell_slots: None,
        spells_known: None
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
        class_abilities: {ki_points: 0},
        spell_casting_ability: None,
        spell_slots: None,
        spells_known: None
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
            "martial weapons", 
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
        spell_slots: None,
        spells_known: None,
        class_abilities: {lay_on_hands: 5},
        },
    "Ranger": {
        class_name: "Ranger",
        hit_die: 10,
        proficiencies: [
            "light armor", 
            "medium armor", 
            "heavy armor", 
            "shield", 
            'simple weapons', 
            'martial weapons', 
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
        class_abilities: {
            favored_terrain: None,
            favored_enemy: None
        },
        spell_casting_ability: None,
        spell_slots: None,
        spells_known: None
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
            "simple weapons", 
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
            "weapons": ["short sword", "short bow", "dagger", "dagger"],
            "armor": ["leather"],
        },
        spell_casting_ability: "charisma",
        spell_slots: {
            "cantrips": 4,
            "level 1": 2
            },
        spells_known: None,
        class_abilities: {sneak_attack: 6},
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
        class_abilities: {origin: None},
        },
    "Warlock": {
        class_name: "Warlock",
        hit_die: 8,
        proficiencies: [
            'light armor', 
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
        class_abilities: {patron: None},
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
        spells_known: None,
        class_abilities: {arcane_recovery: None},
        }
    }

class_option_data = {
    "Barbarian": {},
    "Bard": {},
    "Cleric": {
        domain: {
            "Knowledge Domain": {
                "Knowledge Domain Spells": "Your domain spells are command and identify.",
                "Blessings of Knowledge": "Your proficiency bonus of your chosen skills are doubled.",
                prof_choices: (["arcana", "history", "nature", "religion"], 2),
            },
            "Life Domain": {
                "Life Domain Spells": "Your domain spells are bless and cure wounds.",
                "Disciple of Life": "Whenever you use a spell slot of 1st level or higher to restore hit points to a creature, the creature gains an additional hit points equal to 2 + the spell's level.",
                proficiencies: ["heavy armor"]
            },
            "Light Domain": {
                "Light Domain Spells": "Your domain spells are burning hands and faerie fire.",
                "Bonus Cantrip": "You gain the light cantrip if you don't already know it.",
                "Warding Flare": "When you are attacked by a creature you can see within 30 feet of you, you can use your reaction to impose disadvantage on the attack roll. An attacker that can't be blinded is immune to this feature. You can use this feature a number opf times equal to Wisdom modifier (minimum of 1) and regain uses on a long rest."
            },
            "Nature Domain": {
                "Nature Domain Spells": "Your domain spells are animal freindship and speak with animals.",
                proficiencies: ["heavy armor"],
                prof_choices: (["animal handling", "nature", "survival"], 1),
            },
            "Tempest Domain": {
                "Tempest Domain Spells": "Your domain spells are fog cloud and thunderwave.",
                "Wrath of the Storm": "When a creature you can see within 5 feet of you hits you with an attack, you can use your reaction to cause the creature to make a Dexterity saving throw. The creature takes 2d8 thunder damage on a failed save, and half that on a successful save. You can use this feature a number of times equal to your Wisdom modifier (minimum of 1) and regain uses on a long rest.",
                proficiencies: ["heavy armor", "martial weapons"]
            },
            "Trickery Domain": {
                "Trickery Domain Spells": "Your domain spells are disguise self and charm person.",
                "Blessing of the Trickster": "You can use your action to touch a willing creature other than yourself to give it advantage on Stealth checks. This blessing lasts for 1 hour or until you use this feature again."
            },
            "War Domain": {
                "War Domain Spells": "Your domain spells are divine favor and shield of faith.",
                "War Priest": "When you use the Attack action, you can make one weapon attack as a bonus action. You can use this feature a number of times equal to your Wisdom modifier (minimum of 1) and regain uses on a long rest.",
                proficiencies: ["heavy armor", "martial weapons"]
            }
        }
    },
    "Druid": {},
    "Fighter": {
        fighting_style: {
            "Archery": "You gain a +2 bonus to attack rolls you make with ranged weapons.",
            "Defense": "While you are wearing armor, you gain a +1 bonus to AC.",
            "Dueling": "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",
            "Great Weapon Fighting": "When you roll a 1 or 2 on a damage die for an attack with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must be two-handed or versatile.",
            "Protection": "When a creature you can see attacks a target other that you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.",
            "Two-Weapon Fighting": "When you engage in two weapon fighting, you can add your ability modifier to the damage of the second attack."
        }
    },
    "Monk": {},
    "Paladin": {},
    "Ranger": {
        favored_enemy: ["Aberrations", "Beasts", "Celestials", "Constructs", "Dragons", "Elementals", "Fey", "Fiends", "Giants", "Monstrosities", "Oozes", "Plants", "Undead"],
        favored_terrain: ["Arctic", "Coast", "Desert", "Forest", "Grassland", "Mountain", "Swamp", "Underdark",],
    },
    "Rogue": {},
    "Sorcerer": {
        origin: {
            "Draconic Bloodline": {
                "Black": "Acid",
                "Blue": "Lightning",
                "Brass": "Fire",
                "Bronze": "Lightning",
                "Copper": "Acid",
                "Gold": "Fire",
                "Green": "Poison",
                "Red": "Fire",
                "Silver": "Cold",
                "White": "Cold"
            },
            "Wild Magic": {
                "Wild Magic Surge": "When you cast a level 1 or higher spell the DM may have you roll a d20. If you roll a 1, roll on the Wild Magic Surge Table.",
                "Tides of Chaos": "Once per long rest, you may gain advantage on an attack roll, ability check or saving throw. The DM may have you roll on the Wild Magic Surge table to restore this ability (normal timing rules still apply)."
            }
        }
    },
    "Warlock": {
        patron: {
            "The Archfey": {
                "Extended Spell List": "When choosing spells to learn you have access to an expanded spell list. Level 1 spells now include faerie fire and sleep.",
                "Fey Presence": "As an action, you can cause each creature in a 10-foot cube originating from you to make a Wisdom saving throw against your warlock spell save DC. The creatures that fail are all charmed or frightened by you (your choice) until the end of your next turn. This feature replenishes on a short/long rest."
            },
            "The Fiend": {
                "Expanded Spell List": "When choosing spells to learn you have access to an expanded spell list. Level 1 spells now include burning hands and command.",
                "Dark One's Blessing": "When you reduce a creature to 0 hit points, you gain temporary hit points equal to your Charisma modifier + your warlock level (minimimum of 1)."
            },
            "The Great Old One": {
                "Extended Spell List": "When choosing spells to learn you have access to an expanded spell list. Level 1 spells now include dissonant whispers and Tashsa's hideous laughter.",
                "Awakened Mind": "You can telepathically speak to any creature you can see within 30 feet of you. You don't need to share a language for that creature to understand you, but the creature must be able to understand at least one language."
            },
        }
    },
    "Wizard": {}
}

class Class:
    def __init__(self, class_name, hit_die, proficiencies, prof_choice_list, class_info, starting_equipment, class_abilities, spell_casting_ability=None, spell_slots=None, spells_known=None):
        self.class_name = class_name
        self.hit_die = hit_die
        self.proficiencies = proficiencies
        self.prof_choice = prof_choice_list
        self.class_info = class_info
        self.starting_equipment = starting_equipment
        self.class_abilities = class_abilities
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known
        self.subclass = None

def create_class_object(name):
    data = class_data[name]
    return Class(
        data[class_name],
        data[hit_die],
        data[proficiencies],
        data[prof_choices],
        data[class_info],
        data[equipment],
        data[class_abilities],
        data[spell_casting_ability],
        data[spell_slots],
        data[spells_known]
        )
