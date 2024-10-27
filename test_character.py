import pytest
from character import Character
from database.race_subrace import *

def test_create_character():
    character = Character("test")
    assert character.name == "test"

def test_get_ability_mod():
    character = Character("test")
    character.strength = 15
    assert character.get_ability_mod("strength") == 2
    assert character.get_ability_mod("dexterity") == -1


def test_increase_core_stat():
    character = Character("test")
    assert character.strength == 8
    character.increase_core_stat("strength", 5)
    assert character.strength == 13

def test_decrease_core_stat():
    character = Character("test")
    assert character.strength == 8
    character.decrease_core_stat("strength", 5)
    assert character.strength == 3

def test_gain_proficiency():
    character = Character("test")
    assert character.proficiencies["strength"] == False
    character.gain_proficiency(["strength"])
    assert character.proficiencies["strength"] == True
    character.gain_proficiency(["simple weapons"])
    assert character.proficiencies["simple weapons"] == True
    assert character.proficiencies["club"] == True
    assert character.proficiencies["flail"] == False
    character.gain_proficiency(["wisdom", "perception"])
    assert character.proficiencies["perception"] == True
    assert character.proficiencies["wisdom"] == True

def test_apply_race_bonus():
    character = Character("test")
    assert character.strength == 8
    assert character.constitution == 8
    race_obj = create_race_object(half_orc)
    character.apply_race_bonus(race_obj)
    assert character.speed == 30
    assert character.strength == 10
    assert character.constitution == 9

    char2 = Character("testing")
    assert char2.constitution == 8
    assert char2.proficiencies["battle axe"] == False
    assert char2.proficiencies["handaxe"] == False
    assert char2.proficiencies["light hammer"] == False
    assert char2.proficiencies["warhammer"] == False
    dwarf_obj = create_race_object(dwarf)
    char2.apply_race_bonus(dwarf_obj)
    assert char2.speed == 25
    assert char2.constitution == 10
    assert char2.proficiencies["battle axe"] == True
    assert char2.proficiencies["handaxe"] == True
    assert char2.proficiencies["light hammer"] == True
    assert char2.proficiencies["warhammer"] == True
    assert char2.damage_resistance["poison"] == True

def test_apply_subrace():
    character = Character("testing")
    assert character.strength == 8
    assert character.constitution == 8
    assert character.proficiencies["battle axe"] == False
    assert character.proficiencies["handaxe"] == False
    assert character.proficiencies["light hammer"] == False
    assert character.proficiencies["warhammer"] == False
    dwarf_obj = create_race_object(dwarf)
    character.apply_race_bonus(dwarf_obj)
    assert character.speed == 25
    assert character.constitution == 10
    assert character.proficiencies["battle axe"] == True
    assert character.proficiencies["handaxe"] == True
    assert character.proficiencies["light hammer"] == True
    assert character.proficiencies["warhammer"] == True
    assert character.damage_resistance["poison"] == True
    subrace_obj = create_subrace_object("mountain dwarf")
    character.apply_subrace_bonus(subrace_obj)
    assert character.subrace == "mountain dwarf"
    assert character.strength == 10
    assert character.proficiencies["light armor"] == True
    assert character.proficiencies["medium armor"] == True

def test_apply_dragon_subrace():
    character = Character("testing")
    assert character.strength == 8
    assert character.charisma == 8
    dragon_obj = create_race_object(dragonborn)
    character.apply_race_bonus(dragon_obj)
    assert character.speed == 30
    assert character.strength == 10
    assert character.charisma == 9
    subrace_obj = create_dragoncolor_object("black")
    character.apply_subrace_bonus(subrace_obj)
    assert character.subrace == "black"
    assert character.damage_resistance["acid"] == True
    assert character.breath_shape == "line"
    assert character.breath_size == (5, 30)
    assert character.breath_type == "acid"

def test_gain_damage_resistance():
    character = Character("testing")
    assert character.damage_resistance["acid"] == False
    character.gain_damage_resistance("acid")
    assert character.damage_resistance["acid"] == True

def test_get_core_skill_ability():
    character = Character("testing")
    assert character.get_skill_core_ability("athletics") == "strength"
    assert character.get_skill_core_ability("perception") == "wisdom"
    assert character.get_skill_core_ability("stealth") == "dexterity"
    assert character.get_skill_core_ability("arcana") == "intelligence"
    assert character.get_skill_core_ability("intimidation") == "charisma"

def test_get_skill_bonus():
    pass

def test_get_spell_list():
    pass

def test_add_and_remove_from_inventory():
    pass

def test_equip_and_unequip_items():
    pass

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
