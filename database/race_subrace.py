dwarf = "dwarf"
elf = "elf"
halfling = "halfling"
human = "human"
dragonborn = "dragonborn"
gnome = "gnome"
half_elf = "half elf"
half_orc = "half orc"
tiefling = "tiefling"

races = {
    dwarf: 
            ["hill dwarf", "mountain dwarf"],
    elf: 
            ["high elf", "wood elf", "dark elf"], 
    halfling: 
            ["lightfoot halfling", "stout halfling"],
    human: 
            [],
    dragonborn:
            ["black", "blue", "brass", "bronze", "copper", "gold", "green", "red", "silver", "white"],
    gnome:
        ["forest gnome", "rock gnome"],
    half_elf:
        [],
    half_orc:
        [],
    tiefling:
        []
}
race = "race"
speed = "speed"
ability_bonus = "ability bonus"
proficiencies = "proficiencies"
resistances = "resistances"
prof_choices = "proficiency choices"
sub_races = "sub races"

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
    "hill dwarf": {
        sub_race: "hill dwarf",
        ability_bonus: [("wisdom", 1)],
        proficiencies: [],
        resistances: [],
        hp_bonus: "hp += 1 * self.level",
        speed_bonus: None
        },
    "mountain dwarf": {
        sub_race: "mountain dwarf",
        ability_bonus: [("strength", 2)],
        proficiencies: ['light armor', 'medium armor'],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        },
    "high elf": {
        sub_race: "high elf",
        ability_bonus: [("intelligence", 1)],
        proficiencies: ['long sword', "short sword", "long bow", "short bow"],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        },
    "wood elf": {
        sub_race: "wood elf",
        ability_bonus: [("wisdom", 1)],
        proficiencies: ['long sword', "short sword", "long bow", "short bow"],
        resistances: [],
        hp_bonus: None,
        speed_bonus: 5
        },
    "dark elf": {
        sub_race: "dark elf",
        ability_bonus: [("charisma", 1)],
        proficiencies: ['rapier', "short sword", "hand crossbow"],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        },
    "lightfoot halfling": {
        sub_race: "lightfoot halfling",
        ability_bonus: [("charisma", 1)],
        proficiencies: [],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        },
    "stout halfling": {
        sub_race: "stout halfling",
        ability_bonus: [("charisma", 1)],
        proficiencies: [],
        resistances: ["poison"],
        hp_bonus: None,
        speed_bonus: None
        },
    "forest gnome": {
        sub_race: "forest gnome",
        ability_bonus: [("dexterity", 1)],
        proficiencies: [],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        },
    "rock gnome": {
        sub_race: "rock gnome",
        ability_bonus: [("constitution", 1)],
        proficiencies: [],
        resistances: [],
        hp_bonus: None,
        speed_bonus: None
        }
}

dragon_color_stats = {
    "black": {
        sub_race: "black",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["acid"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "line",
        breath_size: (5, 30),
        breath_type: "acid"
        },
    "blue": {
        sub_race: "blue",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["lightning"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "line",
        breath_size: (5, 30),
        breath_type: "lightning"
        },
    "brass": {
        sub_race: "brass",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["fire"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "line",
        breath_size: (5, 30),
        breath_type: "fire"
        },
    "bronze": {
        sub_race: "bronze",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["lightning"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "line",
        breath_size: (5, 30),
        breath_type: "lightning"
        },
    "copper": {
        sub_race: "copper",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["acid"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "line",
        breath_size: (5, 30),
        breath_type: "acid"
        },
    "gold": {
        sub_race: "gold",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["fire"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "cone",
        breath_size: (15,),
        breath_type: "fire"
        },
    "green": {
        sub_race: "green",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["poison"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "cone",
        breath_size: (15,),
        breath_type: "poison"
        },
    "red": {
        sub_race: "red",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["fire"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "cone",
        breath_size: (15,),
        breath_type: "fire"
        },
    "silver": {
        sub_race: "silver",
        ability_bonus: [],
        proficiencies: [],
        resistances: ["cold"],
        hp_bonus: None,
        speed_bonus: None,
        breath_shape: "cone",
        breath_size: (15,),
        breath_type: "cold"
        },
    "white": {
        sub_race: "white",
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