import pytest
from c_class import *

def test_get_class_data():
    class_input = "Barbarian"
    data = class_data[class_input]
    assert data[class_name] == "Barbarian"
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
    assert data[class_info] == ["rage", "unarmored defense"]
    assert data[equipment] == ["testing", "testing", "one two three"]
    assert data[class_abilities] == {"rage": 2}

def test_get_class_createor():
    class_input = "Barbarian"
    func = class_create_map[class_input]
    assert func == create_barbarian

    class_input = "Bard"
    func = class_create_map[class_input]
    assert func == create_bard

    class_input = "Cleric"
    func = class_create_map[class_input]
    assert func == create_cleric

    class_input = "Druid"
    func = class_create_map[class_input]
    assert func == create_druid

    class_input = "Fighter"
    func = class_create_map[class_input]
    assert func == create_fighter

    class_input = "Monk"
    func = class_create_map[class_input]
    assert func == create_monk

    class_input = "Paladin"
    func = class_create_map[class_input]
    assert func == create_paladin

    class_input = "Ranger"
    func = class_create_map[class_input]
    assert func == create_ranger

    class_input = "Rogue"
    func = class_create_map[class_input]
    assert func == create_rogue

    class_input = "Sorcerer"
    func = class_create_map[class_input]
    assert func == create_sorcerer

    class_input = "Warlock"
    func = class_create_map[class_input]
    assert func == create_warlock

    class_input = "Wizard"
    func = class_create_map[class_input]
    assert func == create_wizard

def test_create_class_handler():
    class_input = "Barbarian"
    barb = create_class_object(class_input)
    assert barb.class_name == "Barbarian"
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
    assert barb.class_info == ["rage", "unarmored defense"]
    assert barb.starting_equipment == ["testing", "testing", "one two three"]
    assert barb.class_abilities == {"rage": 2}

def test_create_barb():
    barb = create_barbarian(class_data["Barbarian"])
    assert barb.class_name == "Barbarian"
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
    assert barb.class_info == ["rage", "unarmored defense"]
    assert barb.starting_equipment == ["testing", "testing", "one two three"]
    assert barb.class_abilities == {"rage": 2}


