import pytest
from race_subrace import *

def test_get_race_stats():
    stats = race_stats[half_orc]
    assert stats[race] == half_orc
    assert stats[speed] == 30
    assert stats[ability_bonus] == [("strength", 2), ("constitution", 1)]
    assert stats[proficiencies] == []
    assert stats[resistances] == []
    assert stats[prof_choices] == []
    assert stats[sub_races] == []

    stats = race_stats[human]
    assert stats[race] == human
    assert stats[speed] == 30
    assert stats[ability_bonus] == [("strength", 1), 
                          ("dexterity", 1), 
                          ("constitution", 1), 
                          ("intelligence", 1), 
                          ("wisdom", 1), 
                          ("charisma", 1)]
    assert stats[proficiencies] == []
    assert stats[resistances] == []
    assert stats[prof_choices] == []
    assert stats[sub_races] == []

    stats = race_stats[dwarf]
    assert stats[race] == dwarf
    assert stats[speed] == 25
    assert stats[ability_bonus] == [("constitution", 2)]
    assert stats[proficiencies] == ['battle axe', 'handaxe', "light hammer", "warhammer"]
    assert stats[resistances] == ["poison"]
    assert stats[prof_choices] == []
    assert stats[sub_races] == ["hill dwarf", "mountain dwarf"]

def test_create_race_object():
    race_obj = create_race_object(half_orc)
    assert race_obj.race == half_orc
    assert race_obj.speed == 30
    assert race_obj.stat_bonus == [("strength", 2), ("constitution", 1)]
    assert race_obj.proficiencies == []
    assert race_obj.resistances == []
    assert race_obj.prof_choices == []
    assert race_obj.subraces == []

    race_obj = create_race_object(human)
    assert race_obj.race == human
    assert race_obj.speed == 30
    assert race_obj.stat_bonus == [("strength", 1), 
                          ("dexterity", 1), 
                          ("constitution", 1), 
                          ("intelligence", 1), 
                          ("wisdom", 1), 
                          ("charisma", 1)]
    assert race_obj.proficiencies == []
    assert race_obj.resistances == []
    assert race_obj.prof_choices == []
    assert race_obj.subraces == []

    race_obj = create_race_object(dwarf)
    assert race_obj.race == dwarf
    assert race_obj.speed == 25
    assert race_obj.stat_bonus == [("constitution", 2)]
    assert race_obj.proficiencies == ['battle axe', 'handaxe', "light hammer", "warhammer"]
    assert race_obj.resistances == ["poison"]
    assert race_obj.prof_choices == []
    assert race_obj.subraces == ["hill dwarf", "mountain dwarf"]

def test_other_races():
    assert dwarf in race_stats.keys()
    assert elf in race_stats.keys()
    assert halfling in race_stats.keys()
    assert human in race_stats.keys()
    assert dragonborn in race_stats.keys()
    assert gnome in race_stats.keys()
    assert half_elf in race_stats.keys()
    assert half_orc in race_stats.keys()
    assert tiefling in race_stats.keys()

def test_get_subrace_stats():
    subrace = "lightfoot halfling"
    stats = sub_race_stats[subrace]
    assert stats[sub_race] == subrace
    assert stats[ability_bonus] == [("charisma", 1)]
    assert stats[proficiencies] == []
    assert stats[resistances] == []
    assert stats[hp_bonus] == None
    assert stats[speed_bonus] == None

def test_create_subrace_object():
    subrace = "lightfoot halfling"
    subrace_obj = create_subrace_object(subrace)
    assert subrace_obj.subrace == subrace
    assert subrace_obj.stat_bonus == [("charisma", 1)]
    assert subrace_obj.proficiencies == []
    assert subrace_obj.resistances == []
    assert subrace_obj.hp_bonus == None
    assert subrace_obj.speed_bonus == None

def get_dragon_color_stats():
    color = "black"
    stats = dragon_color_stats[color]
    assert stats[sub_race] == color
    assert stats[ability_bonus] == []
    assert stats[proficiencies] == []
    assert stats[resistances] == ["acid"]
    assert stats[hp_bonus] == None
    assert stats[speed_bonus] == None
    assert stats[breath_shape] == "line"
    assert stats[breath_size] == (5, 30)
    assert stats[breath_type] == "acid"

def test_create_dragoncolor_object():
    color = "black"
    color_obj = create_dragoncolor_object(color)
    assert color_obj.subrace == color
    assert color_obj.stat_bonus == []
    assert color_obj.proficiencies == []
    assert color_obj.resistances == ["acid"]
    assert color_obj.hp_bonus == None
    assert color_obj.speed_bonus == None
    assert color_obj.breath_shape == "line"
    assert color_obj.breath_size == (5, 30)
    assert color_obj.breath_type == "acid"