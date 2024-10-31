dwarf = "Dwarf"
elf = "Elf"
halfling = "Halfling"
human = "Human"
dragonborn = "Dragonborn"
gnome = "Gnome"
half_elf = "Half Elf"
half_orc = "Half Orc"
tiefling = "Tiefling"

races = {
    dwarf: 
            ["Hill Dwarf", "Mountain Dwarf"],
    elf: 
            ["High Elf", "Wood Elf", "Dark Elf"], 
    halfling: 
            ["Lightfoot Halfling", "Stout Halfling"],
    human: 
            [],
    dragonborn:
            ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White"],
    gnome:
        ["Forest Gnome", "Rock Gnome"],
    half_elf:
        [],
    half_orc:
        [],
    tiefling:
        []
}
race_info = {
    dwarf: {
        "Darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "Dwarven Resilience": "You have advantage on saving throws against poison, and resistance against poison damage.",
        "Stonecunning": "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check.",
    },
    elf: {
        "Darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "Fey Ancestry": "You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
        "Trance": "You don't need to sleep. Instead you meditate deeply for 4 hours each day."
    },
    halfling: {
        "Lucky:": "When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll.",
        "Brave:": "You have advantage on saving throws against being frightened.",
        "Halfling Nimbleness": "You can move through the space of any creature that is of a size larger than yours."
    },
    human: {},
    dragonborn: {
        "Draconic Ancestry": "You have draconic ancestry. Your ancestry determines your breath weapon and damage resistance.",
        "Breath Weapon": "You can use your action to exhale destructive energy. Your draconic ancestry determines the size, shape and damade type of exhalation. Each creature in it's path makes saving throw, the type of which is determined by your draconic ancestry.",
        "Damage Resistance": "You have resistance to the damage type associated with your draconic ancestry."
    },
    gnome: {
        "Darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "Gnome Cunning": "You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
    },
    half_elf: {
        "Darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "Fey Ancestry": "You have advantage on saving throws against being charmed, and magic can't put you to sleep." 
    },
    half_orc: {
        "Darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "Relentless Endurance": "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest.",
        "Savage Attacks": "When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critiical hit."
    },
    tiefling: {
        "Darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "Hellish Resistance": "You have resistance to fire damage.",
        "Infernal Legacy": "You know the thaumaturgy cantrip."
    }
}
race = "race"
speed = "speed"
ability_bonus = "ability bonus"
proficiencies = "proficiencies"
resistances = "resistances"
prof_choices = "proficiency choices"
sub_races = "sub races"
race_traits = "race traits"

race_stats = {
    dwarf: {
        race: dwarf,
        speed: 25, 
        ability_bonus: [("constitution", 2)],
        proficiencies: ['battle axe', 'handaxe', "light hammer", "warhammer"],
        resistances: ["poison"],
        prof_choices: [],
        sub_races: races[dwarf]
        },
    elf: {
        race: elf,
        speed: 30, 
        ability_bonus: [("dexterity", 2)],
        proficiencies: ["perception"],
        resistances: [],
        prof_choices: [],
        sub_races: races[elf]
        }, 
    halfling: {
        race: halfling,
        speed: 25, 
        ability_bonus: [("dexterity", 2)],
        proficiencies: [],
        resistances: [],
        prof_choices: [],
        sub_races: races[halfling]
        },
    human: {
        race: human,
        speed: 30, 
        ability_bonus: [("strength", 1), 
                          ("dexterity", 1), 
                          ("constitution", 1), 
                          ("intelligence", 1), 
                          ("wisdom", 1), 
                          ("charisma", 1)],
        proficiencies: [],
        resistances: [],
        prof_choices: [],
        sub_races: races[human]
        },
    dragonborn: {
        race: dragonborn,
        speed: 30, 
        ability_bonus: [("strength", 2), ("charisma", 1)],
        proficiencies: [],
        resistances: [],
        prof_choices: [],
        sub_races: races[dragonborn]},
    gnome: {
        race: gnome,
        speed: 25, 
        ability_bonus: [("dexterity", 2)],
        proficiencies: [],
        resistances: [],
        prof_choices: [],
        sub_races: races[halfling]
        },
    half_elf: {
        race: half_elf,
        speed: 30, 
        ability_bonus: [("charisma", 2)],
        proficiencies: [],
        resistances: [],
        prof_choices:
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
            'persausion'], 2),
        sub_races: races[half_elf]
        },
    half_orc: {
        race: half_orc,
        speed: 30, 
        ability_bonus: [("strength", 2), ("constitution", 1)],
        proficiencies: [],
        resistances: [],
        prof_choices: [],
        sub_races: races[half_orc]
        },
    tiefling: {
        race: tiefling,
        speed: 30, 
        ability_bonus: [("intelligence", 1), ("charisma", 2)],
        proficiencies: [],
        resistances: ["fire"],
        prof_choices: [],
        sub_races: races[tiefling]
        }
}

hp_bonus = "hp bonus"
speed_bonus = "speed bonus"
breath_shape = "breath shape"
breath_size = "breath size"
breath_type = "damage type"
sub_race = "sub race"

sub_race_stats = {
    "Hill Dwarf": {
        sub_race: "Hill Dwarf",
        ability_bonus: [("wisdom", 1)],
        proficiencies: [],
        resistances: [],
        hp_bonus: "hp += 1 * self.level",
        speed_bonus: None
        },
    "Mountain Dwarf": {
        sub_race: "Mountain Dwarf",
        ability_bonus: [("strength", 2)],
        proficiencies: ['light armor', 'medium armor'],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        },
    "High Elf": {
        sub_race: "High Elf",
        ability_bonus: [("intelligence", 1)],
        proficiencies: ['long sword', "short sword", "long bow", "short bow"],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        },
    "Wood Elf": {
        sub_race: "Wood Elf",
        ability_bonus: [("wisdom", 1)],
        proficiencies: ['long sword', "short sword", "long bow", "short bow"],
        resistances: [],
        hp_bonus: None,
        speed_bonus: 5
        },
    "Dark Elf": {
        sub_race: "Dark Elf",
        ability_bonus: [("charisma", 1)],
        proficiencies: ['rapier', "short sword", "hand crossbow"],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        },
    "Lightfoot Halfling": {
        sub_race: "Lightfoot Halfling",
        ability_bonus: [("charisma", 1)],
        proficiencies: [],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        },
    "Stout Halfling": {
        sub_race: "Stout Halfling",
        ability_bonus: [("charisma", 1)],
        proficiencies: [],
        resistances: ["poison"],
        hp_bonus: None,
        speed_bonus: None
        },
    "Forest Gnome": {
        sub_race: "Forest Gnome",
        ability_bonus: [("dexterity", 1)],
        proficiencies: [],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        },
    "Rock Gnome": {
        sub_race: "Rock Gnome",
        ability_bonus: [("constitution", 1)],
        proficiencies: [],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        }
}

dragon_color_stats = {
    "Black": {
        sub_race: "Black",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["acid"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "line",
        breath_size: (5, 30),
        breath_type: "acid"
        },
    "Blue": {
        sub_race: "Blue",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["lightning"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "line",
        breath_size: (5, 30),
        breath_type: "lightning"
        },
    "Brass": {
        sub_race: "Brass",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["fire"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "line",
        breath_size: (5, 30),
        breath_type: "fire"
        },
    "Bronze": {
        sub_race: "Bronze",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["lightning"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "line",
        breath_size: (5, 30),
        breath_type: "lightning"
        },
    "Copper": {
        sub_race: "Copper",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["acid"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "line",
        breath_size: (5, 30),
        breath_type: "acid"
        },
    "Gold": {
        sub_race: "Gold",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["fire"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "cone",
        breath_size: (15,),
        breath_type: "fire"
        },
    "Green": {
        sub_race: "Green",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["poison"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "cone",
        breath_size: (15,),
        breath_type: "poison"
        },
    "Red": {
        sub_race: "Red",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["fire"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "cone",
        breath_size: (15,),
        breath_type: "fire"
        },
    "Silver": {
        sub_race: "Silver",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["cold"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "cone",
        breath_size: (15,),
        breath_type: "cold"
        },
    "White": {
        sub_race: "White",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["cold"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "cone",
        breath_size: (15,),
        breath_type: "cold"
        },
}
class Race:
    def __init__(self, race, speed, stat_bonus, proficiencies, resistances, prof_choices, subraces):
        self.race = race
        self.speed = speed
        self.stat_bonus = stat_bonus
        self.proficiencies = proficiencies
        self.resistances = resistances
        self.prof_choices = prof_choices
        self.subraces = subraces

class SubRace:
    def __init__(self, subrace, stat_bonus, proficiencies, resistances, hp_bonus, speed_bonus):
        self.subrace = subrace
        self.stat_bonus = stat_bonus
        self.proficiencies = proficiencies
        self.resistances = resistances
        self.hp_bonus = hp_bonus
        self.speed_bonus = speed_bonus

class DragonColor(SubRace):
    def __init__(self, subrace, stat_bonus, proficiencies, resistances, hp_bonus, speed_bonus, breath_shape, breath_size, breath_type):
        super().__init__(subrace, stat_bonus, proficiencies, resistances, hp_bonus, speed_bonus)
        self.breath_shape = breath_shape
        self.breath_size = breath_size
        self.breath_type = breath_type

def create_race_object(input):
    stats = race_stats[input]
    return Race(
        stats[race], 
        stats[speed], 
        stats[ability_bonus], 
        stats[proficiencies], 
        stats[resistances], 
        stats[prof_choices], 
        stats[sub_races])



def create_subrace_object(input):
    stats = sub_race_stats[input]
    return SubRace(
        stats[sub_race],
        stats[ability_bonus],
        stats[proficiencies], 
        stats[resistances],  
        stats[hp_bonus], 
        stats[speed_bonus])

def create_dragoncolor_object(input):
    stats = dragon_color_stats[input]
    return DragonColor(
        stats[sub_race],
        stats[ability_bonus],
        stats[proficiencies], 
        stats[resistances],  
        stats[hp_bonus], 
        stats[speed_bonus],
        stats[breath_shape],
        stats[breath_size],
        stats[breath_type])