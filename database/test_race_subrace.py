import pytest
from race_database import *

def test_get_race_stats():
    stats = race_stats[half_orc]
    assert stats[race] == half_orc
    assert stats[speed] == 30
    assert stats[ability_bonus] == [("strength", 2), ("constitution", 1)]
    assert stats[proficiencies] == []
    assert stats[resistances] == []
    assert stats[prof_choices] == []
    assert stats[sub_races] == []

def test_create_race_object():
    race_obj = create_race_object(half_orc)
    assert race_obj.race == half_orc
    assert race_obj.speed == 30
    assert race_obj.stat_bonus == [("strength", 2), ("constitution", 1)]
    assert race_obj.proficiencies == []
    assert race_obj.resistances == []
    assert race_obj.prof_choices == []
    assert race_obj.subraces == []

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