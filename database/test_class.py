import pytest
from c_class import *

def test_get_class_data():
    class_input = "barbarian"
    data = class_data[class_input]
    assert data[class_name] == "barbarian"
    assert data[hit_die] == 12
    assert data[proficiencies] == ["light armor", 
                                          "medium armor", 
                                          "heavy armor", 
                                          "shield", 
                                          "simple weapons", 
                                          "martial weapons", 
                                          "strength",
                                          "constitution"]
    assert data[prof_choices] == (["animal handling", 
                                         "athletics", 
                                         "intimidation", 
                                         "nature", 
                                         "perception", 
                                         "survival"],
                                        2)
    assert data[class_abilities] == ["rage", "unarmored defense"]
    assert data[equipment] == ["testing", "testing", "one two three"]
    assert data[rage_charges] == 2

def test_get_class_createor():
    class_input = "barbarian"
    func = class_create_map[class_input]
    assert func == create_barbarian

    class_input = "bard"
    func = class_create_map[class_input]
    assert func == create_bard

    class_input = "cleric"
    func = class_create_map[class_input]
    assert func == create_cleric

    class_input = "druid"
    func = class_create_map[class_input]
    assert func == create_druid

    class_input = "fighter"
    func = class_create_map[class_input]
    assert func == create_fighter

    class_input = "monk"
    func = class_create_map[class_input]
    assert func == create_monk

    class_input = "paladin"
    func = class_create_map[class_input]
    assert func == create_paladin

    class_input = "ranger"
    func = class_create_map[class_input]
    assert func == create_ranger

    class_input = "rogue"
    func = class_create_map[class_input]
    assert func == create_rogue

    class_input = "sorcerer"
    func = class_create_map[class_input]
    assert func == create_sorcerer

    class_input = "warlock"
    func = class_create_map[class_input]
    assert func == create_warlock

    class_input = "wizard"
    func = class_create_map[class_input]
    assert func == create_wizard

def test_create_class_handler():
    class_input = "barbarian"
    barb = create_class_object(class_input)
    assert barb.class_name == "barbarian"
    assert barb.hit_die == 12
    assert barb.proficiencies == ["light armor", 
                                          "medium armor", 
                                          "heavy armor", 
                                          "shield", 
                                          "simple weapons", 
                                          "martial weapons", 
                                          "strength",
                                          "constitution"]
    assert barb.prof_choice == (["animal handling", 
                                         "athletics", 
                                         "intimidation", 
                                         "nature", 
                                         "perception", 
                                         "survival"],
                                        2)
    assert barb.class_abilities == ["rage", "unarmored defense"]
    assert barb.starting_equipment == ["testing", "testing", "one two three"]
    assert barb.rage == 2

def test_create_barb():
    barb = create_barbarian(class_data["barbarian"])
    assert barb.class_name == "barbarian"
    assert barb.hit_die == 12
    assert barb.proficiencies == ["light armor", 
                                          "medium armor", 
                                          "heavy armor", 
                                          "shield", 
                                          "simple weapons", 
                                          "martial weapons", 
                                          "strength",
                                          "constitution"]
    assert barb.prof_choice == (["animal handling", 
                                         "athletics", 
                                         "intimidation", 
                                         "nature", 
                                         "perception", 
                                         "survival"],
                                        2)
    assert barb.class_abilities == ["rage", "unarmored defense"]
    assert barb.starting_equipment == ["testing", "testing", "one two three"]
    assert barb.rage == 2


