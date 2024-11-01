import pytest
from character import Character
from database.race_subrace import *
from database.equipment.weapon_and_armor_objects import *
from database.c_class import create_class_object

def test_create_character():
    c = Character("test")
    assert c.name == "test"
    assert c.race == None
    assert c.race_info == None
    assert c.subrace == None
    assert c.c_class == None
    assert c.subclass == None
    assert c.class_info == []
    assert c.class_abilities == {}
    assert c.background == None
    assert c.speed == 0
    assert c.hp == 0
    assert c.hit_die == 0
    assert c.proficiency_bonus == 2
    assert c.level == 1
    assert c.xp == 0
    assert c.strength == 8
    assert c.dexterity == 8
    assert c.constitution == 8
    assert c.intelligence == 8
    assert c.wisdom == 8
    assert c.charisma == 8
    assert c.ac == 10
    assert c.proficiencies == {
    'strength': False, 
    'dexterity': False, 
    'constitution': False, 
    'intelligence': False, 
    'wisdom': False, 
    'charisma': False,
    'athletics': False, 
    'acrobatics': False, 
    'sleight of hand': False, 
    'stealth': False, 
    'arcana': False, 
    'history': False, 
    'investigation': False, 
    'nature': False, 
    'religion': False, 
    'animal handling': False, 
    'insight': False, 
    'medicine': False, 
    'perception': False, 
    'survival': False, 
    'deception': False, 
    'intimidation': False, 
    'performance': False, 
    'persuasion': False, 
    'light armor': False, 
    'medium armor': False, 
    'heavy armor': False, 
    'shield': False,
    'simple weapons': False,
    "martial weapons": False, 
    'club': False, 
    'dagger': False, 
    'greatclub': False, 
    'handaxe': False, 
    'javelin': False, 
    'light hammer': False, 
    'mace': False, 
    'quarterstaff': False, 
    'sickle': False, 
    'spear': False, 
    'unarmed strike': False, 
    'light crossbow': False, 
    'dart': False, 
    'short bow': False, 
    'sling': False, 
    'battle axe': False, 
    'flail': False, 
    'glaive': False, 
    'great axe': False, 
    'great sword': False, 
    'halberd': False, 
    'lance': False, 
    'long sword': False, 
    'maul': False, 
    'morning star': False, 
    'pike': False, 
    'rapier': False, 
    'scimitar': False, 
    'short sword': False, 
    'trident': False, 
    'war pick': False, 
    'warhammer': False, 
    'whip': False, 
    'blow gun': False, 
    'hand crossbow': False, 
    'heavy crossbow': False, 
    'long bow': False, 
    'net': False
    }
    assert c.damage_resistance == {
    'acid': False, 
    'bludgeoning': False, 
    'cold': False, 
    'fire': False, 
    'force': False, 
    'lightning': False, 
    'necrotic': False, 
    'piercing': False, 
    'poison': False, 
    'psychic': False, 
    'radiant': False, 
    'slashing': False, 
    'thunder': False
    }
    assert c.inventory == []
    assert c.weapon == None
    assert c.armor == None
    assert c.shield == None
    assert c.equipped_items == []
    assert c.spell_casting_ability == None
    assert c.spell_slots == {
    "cantrips": 0,
    "level 1": 0,
    "level 2": 0,
    "level 3": 0,
    "level 4": 0,
    "level 5": 0,
    "level 6": 0,
    "level 7": 0,
    "level 8": 0,
    "level 9": 0,
}
    assert c.spell_list == []
    assert c.breath_weapon == None

def test_assign_stat():
    c = Character("testing")
    assert c.strength == 8
    assert c.dexterity == 8
    assert c.constitution == 8
    assert c.intelligence == 8
    assert c.wisdom == 8
    assert c.charisma == 8
    c.assign_stat("strength", 10)
    assert c.strength == 10
    c.assign_stat("dexterity", 12)
    assert c.dexterity == 12
    c.assign_stat("constitution", 14)
    assert c.constitution == 14
    c.assign_stat("intelligence", 16)
    assert c.intelligence == 16
    c.assign_stat("wisdom", 18)
    assert c.wisdom == 18
    c.assign_stat("charisma", 20)
    assert c.charisma == 20

def test_get_saving_throw():
    c = Character("test")
    assert c.get_saving_throw("charisma") == -1
    assert c.get_saving_throw("dexterity") == -1
    assert c.get_saving_throw("constitution") == -1
    assert c.get_saving_throw("intelligence") == -1
    assert c.get_saving_throw("strength") == -1
    assert c.get_saving_throw("wisdom") == -1
    c.assign_stat("strength", 10)
    assert c.strength == 10
    assert c.get_saving_throw("strength") == 0
    c.gain_proficiency(["strength"])
    assert c.get_saving_throw("strength") == 2

def test_get_ability_mod():
    c = Character("test")
    c.strength = 15
    assert c.get_ability_mod("strength") == 2
    assert c.get_ability_mod("dexterity") == -1


def test_increase_core_stat():
    c = Character("test")
    assert c.strength == 8
    c.increase_core_stat("strength", 5)
    assert c.strength == 13

def test_decrease_core_stat():
    c = Character("test")
    assert c.strength == 8
    c.decrease_core_stat("strength", 5)
    assert c.strength == 3

def test_get_core_skill_ability():
    c = Character("testing")
    assert c.get_skill_core_ability("athletics") == "strength"
    assert c.get_skill_core_ability("perception") == "wisdom"
    assert c.get_skill_core_ability("stealth") == "dexterity"
    assert c.get_skill_core_ability("arcana") == "intelligence"
    assert c.get_skill_core_ability("intimidation") == "charisma"

def test_get_skill_bonus():
    c = Character("testing")
    assert c.get_skill_bonus("athletics") == -1
    assert c.get_skill_bonus("intimidation") == -1
    c.assign_stat("strength", 20)
    assert c.strength == 20
    assert c.get_skill_bonus("athletics") == 5
    c.assign_stat("charisma", 4)
    assert c.charisma == 4
    assert c.get_skill_bonus("intimidation") == -3

def test_get_weapon_profs():
    c = Character("testing")
    assert c.proficiencies["simple weapons"] == False
    assert c.proficiencies["martial weapons"] == False
    c.gain_proficiency(["simple weapons", "light armor"])
    assert c.get_weapon_proficiencies() == ['Simple weapons', 
                  'Club', 
                  'Dagger', 
                  'Greatclub', 
                  'Handaxe', 
                  'Javelin', 
                  'Light hammer', 
                  'Mace', 
                  'Quarterstaff', 
                  'Sickle', 
                  'Spear', 
                  'Unarmed strike', 
                  'Light crossbow', 
                  'Dart', 
                  'Short bow', 
                  'Sling',]

def test_apply_background():
    c = Character("testing")
    assert c.background == None
    c.apply_background("Noble")
    assert c.background == "Noble"
    assert c.proficiencies["history"] == True
    assert c.proficiencies["persuasion"] == True

    c2 = Character("testing")
    assert c2.background == None
    c2.apply_background("Acolyte")
    assert c2.background == "Acolyte"
    assert c2.proficiencies["insight"] == True
    assert c2.proficiencies["religion"] == True
    

def test_gain_damage_resistance():
    c = Character("testing")
    assert c.damage_resistance["acid"] == False
    c.gain_damage_resistance("acid")
    assert c.damage_resistance["acid"] == True

def test_gain_proficiency():
    c = Character("test")
    assert c.proficiencies["strength"] == False
    c.gain_proficiency(["strength"])
    assert c.proficiencies["strength"] == True
    c.gain_proficiency(["simple weapons"])
    assert c.proficiencies["simple weapons"] == True
    assert c.proficiencies["club"] == True
    assert c.proficiencies["flail"] == False
    c.gain_proficiency(["wisdom", "perception"])
    assert c.proficiencies["perception"] == True
    assert c.proficiencies["wisdom"] == True

def test_add_remove_from_inventory():
    c = Character("test")
    assert c.inventory == []
    c.add_to_inventory("test")
    assert c.inventory == ["test"]
    c.remove_from_inventory("test")
    assert c.inventory == []
    w = create_weapon("club")
    c.add_to_inventory(w)
    assert c.inventory == [w]
    w2 = create_weapon("light crossbow")
    c.add_to_inventory(w2)
    assert c.inventory == [w, w2]
    c.remove_from_inventory(w2)
    assert c.inventory == [w]
    c.remove_from_inventory(w)
    assert c.inventory == []

def test_equip_armor():
    c = Character("test")
    assert c.ac == 10
    assert c.armor == None
    assert c.inventory == []
    assert c.equipped_items == []
    a = create_armor("leather")
    c.add_to_inventory(a)
    assert c.inventory == [a]
    c.equip_armor(a)
    assert c.armor == a
    assert c.equipped_items == [a]
    assert c.ac == 11

def test_equip_armor_error():
    c = Character("test")
    assert c.armor == None
    a = create_armor("splint")
    c.add_to_inventory(a)
    with pytest.raises(Exception):
        c.equip_armor(a)

def test_equip_shield():
    c = Character("test")
    assert c.shield == None
    assert c.ac == 10
    assert c.inventory == []
    assert c.equipped_items == []
    s = create_armor("shield")
    c.add_to_inventory(s)
    assert c.inventory == [s]
    c.equip_shield(s)
    assert c.equipped_items == [s]
    assert c.shield == s
    assert c.ac == 12

def test_shield_error():
    c = Character("test")
    assert c.shield == None
    s = create_armor("shield")
    w = create_weapon("glaive")
    c.weapon = w
    with pytest.raises(Exception):
        c.equip_shield(s)

def test_equip_weapons():
    c = Character("test")
    assert c.weapon == None
    assert c.inventory == []
    assert c.equipped_items == []
    w = create_weapon("club")
    c.add_to_inventory(w)
    assert c.inventory == [w]
    assert c.equipped_items == []
    c.equip_weapon(w)
    assert c.weapon == w
    assert c.equipped_items == [w]
    assert c.inventory == [w]
    w2 = create_weapon("light crossbow")
    c.add_to_inventory(w2)
    assert c.inventory == [w, w2]
    c.equip_weapon(w2)
    assert c.weapon == w2
    assert c.inventory == [w, w2]
    assert c.equipped_items == [w2]

def test_apply_race_bonus():
    c = Character("test")
    assert c.strength == 8
    assert c.constitution == 8
    race_obj = create_race_object(half_orc)
    c.apply_race_bonus(race_obj)
    assert c.speed == 30
    assert c.strength == 10
    assert c.constitution == 9

    c2 = Character("testing")
    assert c2.constitution == 8
    assert c2.proficiencies["battle axe"] == False
    assert c2.proficiencies["handaxe"] == False
    assert c2.proficiencies["light hammer"] == False
    assert c2.proficiencies["warhammer"] == False
    assert c2.damage_resistance["poison"] == False
    assert c2.race_info == None
    dwarf_obj = create_race_object(dwarf)
    c2.apply_race_bonus(dwarf_obj)
    assert c2.speed == 25
    assert c2.constitution == 10
    assert c2.proficiencies["battle axe"] == True
    assert c2.proficiencies["handaxe"] == True
    assert c2.proficiencies["light hammer"] == True
    assert c2.proficiencies["warhammer"] == True
    assert c2.damage_resistance["poison"] == True
    assert c2.race_info == {
        "Darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "Dwarven Resilience": "You have advantage on saving throws against poison, and resistance against poison damage.",
        "Stonecunning": "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check.",
    }

def test_apply_subrace():
    c = Character("testing")
    assert c.strength == 8
    assert c.constitution == 8
    assert c.proficiencies["battle axe"] == False
    assert c.proficiencies["handaxe"] == False
    assert c.proficiencies["light hammer"] == False
    assert c.proficiencies["warhammer"] == False
    assert c.damage_resistance["poison"] == False
    assert c.race_info == None
    assert c.subrace == None
    dwarf_obj = create_race_object(dwarf)
    c.apply_race_bonus(dwarf_obj)
    assert c.speed == 25
    assert c.constitution == 10
    assert c.proficiencies["battle axe"] == True
    assert c.proficiencies["handaxe"] == True
    assert c.proficiencies["light hammer"] == True
    assert c.proficiencies["warhammer"] == True
    assert c.damage_resistance["poison"] == True
    assert c.race_info == {
        "Darkvision": "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
        "Dwarven Resilience": "You have advantage on saving throws against poison, and resistance against poison damage.",
        "Stonecunning": "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check.",
    }
    assert c.proficiencies["light armor"] == False
    assert c.proficiencies["medium armor"] == False
    subrace_obj = create_subrace_object("Mountain Dwarf")
    c.apply_subrace_bonus(subrace_obj)
    assert c.subrace == "Mountain Dwarf"
    assert c.strength == 10
    assert c.proficiencies["light armor"] == True
    assert c.proficiencies["medium armor"] == True
def test_apply_dragon_subrace():
    c = Character("testing")
    assert c.strength == 8
    assert c.charisma == 8
    assert c.race == None
    assert c.subrace == None
    dragon_obj = create_race_object(dragonborn)
    c.apply_race_bonus(dragon_obj)
    assert c.race == "Dragonborn"
    assert c.speed == 30
    assert c.strength == 10
    assert c.charisma == 9
    subrace_obj = create_dragoncolor_object("Black")
    c.apply_subrace_bonus(subrace_obj)
    assert c.subrace == "Black"
    assert c.breath_weapon == {
            breath_shape: "Line",
            breath_size: (5, 30),
            breath_type: "Acid"
            }

def test_apply_class():
    c = Character("testing")
    assert c.c_class == None
    assert c.hit_die == 0
    assert c.proficiencies["light armor"] == False
    assert c.class_info == []
    assert c.class_abilities == {}
    barb = create_class_object("Barbarian")
    c.apply_class(barb)
    assert c.c_class == "Barbarian"
    assert c.hit_die == 12
    assert c.proficiencies["light armor"] == True
    assert c.class_info == ["rage", "unarmored defense"]
    assert c.class_abilities == {"rage": 2}

# I haven't written a database for spell lists yet.
def test_populate_spell_list():
    pass

def test_race_info_initialized():
    c = Character("testing")
    assert c.race_info == None

def test_get_equipped_weapon_mod():
    c = Character("testing")
    assert c.weapon == None
    assert c.strength == 8
    assert c.dexterity == 8
    c.assign_stat("strength", 14)
    c.assign_stat("dexterity", 12)
    assert c.strength == 14
    assert c.dexterity == 12
    w = create_weapon("short sword")
    c.add_to_inventory(w)
    c.equip_weapon(w)
    assert c.weapon == w
    mod = c.get_equipped_weapon_damage_mod()
    assert mod == 2
    c.assign_stat("dexterity", 20)
    assert c.dexterity == 20
    mod = c.get_equipped_weapon_damage_mod()
    assert mod == 5

def test_print_inventory():
    c = Character("testing")
    assert c.inventory == []
    w = create_weapon("short sword")
    c.add_to_inventory(w)
    assert len(c.inventory) == 1
    assert c.print_inventory() == "Short sword\n"
    w2 = create_weapon("long sword")
    c.add_to_inventory(w2)
    assert len(c.inventory) == 2
    assert c.print_inventory() == "Short sword\nLong sword\n"
    a = create_armor("chain mail")
    c.add_to_inventory(a)
    assert len(c.inventory) == 3
    assert c.print_inventory() == "Short sword\nLong sword\nChain mail\n"

def test_get_prof_mod():
    c = Character("testing")
    assert c.proficiencies["club"] == False
    assert c.get_prof_mod("club") == 0
    assert c.proficiency_bonus == 2
    c.gain_proficiency(["club"])
    assert c.get_prof_mod("club") == 2

def test_get_equipped_weapon_prof_mod():
    c = Character("testing")
    assert c.weapon == None
    assert c.get_equipped_weapon_prof_mod() == 0
    assert c.proficiency_bonus == 2
    assert c.proficiencies["club"] == False
    w = create_weapon("club")
    c.add_to_inventory(w)
    c.equip_weapon(w)
    c.gain_proficiency(["club"])
    assert c.get_prof_mod("club") == 2
    assert c.get_equipped_weapon_prof_mod() == 2

def test_get_starting_hp():
    c = Character("testing")
    assert c.hp == 0
    assert c.constitution == 8
    assert c.hit_die == 0
    assert c.get_starting_hp() == 0
    c.hit_die = 6
    assert c.hit_die == 6
    assert c.get_starting_hp() == 6
    c.assign_stat("constitution", 14)
    assert c.constitution == 14
    assert c.get_starting_hp() == 8
    c.assign_stat("constitution", 20)
    assert c.constitution == 20
    assert c.get_starting_hp() == 11
    c.hit_die = 12
    assert c.get_starting_hp() == 17
