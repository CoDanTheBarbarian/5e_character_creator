strength = "strength"
dexterity = "dexterity"
constitution = "constitution"
intelligence = "intelligence"
wisdom = "wisdom"
charisma = "charisma"

core_abilities = [strength, dexterity, constitution, intelligence, wisdom, charisma]

athletics = "athletics"
acrobatics = "acrobatics"
sleight_of_hand = "sleight of hand"
stealth = "stealth"
arcana = "arcana"
history = "history"
investigation = "investigation"
nature = "nature"
religion = "religion"
animal_handling = "animal handling"
insight = "insight"
medicine = "medicine"
perception = "percption"
survival = "survival"
deception = "deception"
intimidation = "intimidation"
performance = "performance"
persuasion = "persuasion"

skill_list = [
    athletics, 
    acrobatics, 
    sleight_of_hand, 
    stealth, 
    arcana, 
    history, 
    investigation, 
    nature, 
    religion, 
    animal_handling, 
    insight, 
    medicine, 
    perception, 
    survival, 
    deception, 
    intimidation, 
    performance, 
    persuasion]

skill_core_stat = {athletics: strength, 
    acrobatics: dexterity, 
    sleight_of_hand: dexterity, 
    stealth: dexterity, 
    arcana: intelligence, 
    history: intelligence, 
    investigation: intelligence, 
    nature: intelligence, 
    religion: intelligence, 
    animal_handling: wisdom, 
    insight: wisdom, 
    medicine: wisdom, 
    perception: wisdom, 
    survival: wisdom, 
    deception: charisma, 
    intimidation: charisma, 
    performance: charisma, 
    persuasion: charisma}

light_armor = "light armor"
medium_armor = "medium armor"
heavy_armor = "heavy armor"
shield = "shields"

club = "club"
dagger = "dagger"
greatclub = "greatclub"
handaxe = "handaxe"
javelin = "javelin"
light_hammer = "light hammer"
mace = "mace"
quarterstaff = "quarterstaff"
sickle = "sickle"
spear = "spear"
unarmed_strike = "unarmed strike"
crossbow_light = "light crossbow"
dart = "dart"
shortbow = "short bow"
sling = "sling"
simple_weapon = "simple weapon"
martial_weapon = "martial weapon"
simple_weapons = [club,
    dagger,
    greatclub,
    handaxe,
    javelin,
    light_hammer,
    mace,
    quarterstaff,
    sickle,
    spear,
    unarmed_strike,
    crossbow_light,
    dart,
    shortbow,
    sling]
battleaxe = "battle axe"
flail = "flail"
glaive = "glaive"
greataxe = "great axe"
greatsword = "great sword"
halberd = "halberd"
lance = "lance"
longsword = "long sword"
maul = "maul"
morningstar = "morning star"
pike = "pike"
rapier = "rapier"
scimitar = "scimitar"
shortsword = "short sword"
trident = "trident"
war_pick = "war pick"
warhammer = "warhammer"
whip = "whip"
blowgun = "blow gun"
crossbow_hand = "hand crossbow"
crossbow_heavy = "heavy crossbow"
longbow = "long bow"
net = "net"
martial_weapons = [
    battleaxe,
    flail,
    glaive,
    greataxe,
    greatsword,
    halberd,
    lance,
    longsword,
    maul,
    morningstar,
    pike,
    rapier,
    scimitar,
    shortsword,
    trident,
    war_pick,
    warhammer,
    whip,
    blowgun,
    crossbow_hand,
    crossbow_heavy,
    longbow,
    net,]

proficiencies = [light_armor, medium_armor, heavy_armor, shield] + simple_weapons + martial_weapons


damage_type_acid = "acid damage"
damage_type_bludgeon = "bludgeoning damage"
damage_type_cold = "cold damage"
damage_type_fire = "fire damage"
damage_type_force = "force damage"
damage_type_lightning = "lightning damage"
damage_type_necrotic = "necrotic damage"
damage_type_piercing = "piercing damage"
damage_type_poison = "poison damage"
damage_type_psychic = "psychic damage"
damage_type_radiant = "radiant damage"
damage_type_slashing = "slashing damage"
damage_type_thunder = "thunder damage"
damage_types = [
    damage_type_acid,
    damage_type_bludgeon, 
    damage_type_cold, 
    damage_type_fire, 
    damage_type_force, 
    damage_type_lightning, 
    damage_type_necrotic, 
    damage_type_piercing,
    damage_type_poison,
    damage_type_psychic,
    damage_type_radiant,
    damage_type_slashing,
    damage_type_thunder
    ]

saving_throw_proficiencies = {ability: False for ability in core_abilities}
proficiency_dict = {item: False for item in skill_list + proficiencies}
damage_resistances = {damage_type: False for damage_type in damage_types}

dwarf = "dwarf"
elf = "elf"
halfling = "halfling"
human = "human"
dragonborn = "dragonborn"
gnome = "gnome"
half_elf = "half elf"
half_orc = "half orc"
tiefling = "tiefling"
list_of_races = [
    dwarf,
    elf,
    halfling,
    human,
    dragonborn,
    gnome,
    half_elf,
    half_orc,
    tiefling
]
hill_dwarf = "hill dwarf"
mountain_dwarf = "mountain dwarf"
high_elf = "high elf"
wood_elf = "wood elf"
drow_elf= "drow elf"
lightfoot_halfling = "lightfoot halfling"
stout_halfling = "stout halfling"
forest_gnome = "forest gnome"
rock_gnome = "rock nome"
list_of_subraces = [
    hill_dwarf,
    mountain_dwarf,
    high_elf,
    wood_elf,
    drow_elf,
    lightfoot_halfling,
    stout_halfling,
    forest_gnome,
    rock_gnome
]

print(saving_throw_proficiencies)

damage_die = "d"
damage_type = "damage"
bonus_attribute = "+"
melee_weapon_stats = {
    club: {damage_die: 4,
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength},
    
    dagger: {damage_die: 4,
    damage_type: damage_type_piercing,
    bonus_attribute: (strength, dexterity)},
    
    greatclub: {damage_die: 8,
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength},
    
    handaxe: {damage_die: 6,
    damage_type: damage_type_slashing,
    bonus_attribute: strength},
    
    javelin: {damage_die: 6,
    damage_type: damage_type_piercing,
    bonus_attribute: strength},
    
    light_hammer: {damage_die: 4,
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength},
    
    mace: {damage_die: 6,
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength},
    
    quarterstaff: {damage_die: 6,
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength},
    
    sickle: {damage_die: 4,
    damage_type: damage_type_slashing,
    bonus_attribute: strength},
    
    spear: {damage_die: 6,
    damage_type: damage_type_piercing,
    bonus_attribute: strength},
    
    battleaxe: {damage_die: 8,
    damage_type: damage_type_slashing,
    bonus_attribute: strength},
    
    flail: {damage_die: 8,
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength},
    
    glaive: {damage_die: 10,
    damage_type: damage_type_slashing,
    bonus_attribute: strength},
    
    greataxe: {damage_die: 12,
    damage_type: damage_type_slashing,
    bonus_attribute: strength},
    
    greatsword: {damage_die: (6, 6),
    damage_type: damage_type_slashing,
    bonus_attribute: strength},
    
    halberd: {damage_die: 10,
    damage_type: damage_type_slashing,
    bonus_attribute: strength},
    
    lance: {damage_die: 12,
    damage_type: damage_type_piercing,
    bonus_attribute: strength},
    
    longsword: {damage_die: 8,
    damage_type: damage_type_slashing,
    bonus_attribute: strength},
    
    maul: {damage_die: (6, 6),
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength},
    
    morningstar: {damage_die: 8,
    damage_type: damage_type_piercing,
    bonus_attribute: strength},
    
    pike: {damage_die: 10,
    damage_type: damage_type_piercing,
    bonus_attribute: strength},

    rapier: {damage_die: 8,
    damage_type: damage_type_piercing,
    bonus_attribute: (strength, dexterity)},

    scimitar: {damage_die: 6,
    damage_type: damage_type_slashing,
    bonus_attribute: (strength, dexterity)},

    shortsword: {damage_die: 6,
    damage_type: damage_type_piercing,
    bonus_attribute: (strength, dexterity)},

    trident: {damage_die: 6,
    damage_type: damage_type_piercing,
    bonus_attribute: strength},

    war_pick: {damage_die: 8,
    damage_type: damage_type_piercing,
    bonus_attribute: strength},

    warhammer: {damage_die: 8,
    damage_type: damage_type_bludgeon,
    bonus_attribute: strength},

    whip: {damage_die: 4,
    damage_type: damage_type_slashing,
    bonus_attribute: (strength, dexterity)},
}
range = "range"
ranged_weapon_stats = {
    crossbow_light: {damage_die: 8,
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    range: (80, 320)},

    dart: {damage_die: 4,
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    range: (20, 60)},

    shortbow: {damage_die: 6,
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    range: (80, 320)},

    sling: {damage_die: 4,
    damage_type: damage_type_bludgeon,
    bonus_attribute: dexterity,
    range: (80, 320)},

    blowgun: {damage_die: 1,
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    range: (25, 100)},

    crossbow_hand: {damage_die: 6,
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    range: (30, 120)},

    crossbow_heavy: {damage_die: 10,
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    range: (100, 400)},

    longbow: {damage_die: 8,
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    range: (150, 600)},

    net: {damage_die: 8,
    damage_type: damage_type_piercing,
    bonus_attribute: dexterity,
    range: (5, 15)},
}