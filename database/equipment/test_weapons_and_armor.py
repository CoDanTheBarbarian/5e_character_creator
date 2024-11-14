import pytest
from .weapon_and_armor_objects import *

def test_init_melee_weapons():
    w = MeleeWeapon("club", "simple", (4,), 'bludgeoning', ("strength",), ["light"])
    assert w.name == "club"
    assert w.weapon_type == "simple"
    assert w.damage_die == (4,)
    assert w.damage_type == "bludgeoning"
    assert w.bonus_attribute == ("strength",)
    assert w.properties == ["light"]
    assert w.get_damage_mod() == ("strength",)

def test_create_melee_weapons():
    w = create_melee_weapon("club")
    assert w.name == "club"
    assert w.weapon_type == "simple"
    assert w.damage_die == (4,)
    assert w.damage_type == "bludgeoning"
    assert w.bonus_attribute == ("strength",)
    assert w.properties == ["light"]
    assert w.get_damage_mod() == ("strength",)

def test_init_versatile_melee_weapons():
    w = VersatileMeleeWeapon("quarterstaff", "simple", (6,), 'bludgeoning', ("strength",), ["versatile"], (8,))
    assert w.name == "quarterstaff"
    assert w.weapon_type == "simple"
    assert w.damage_die == (6,)
    assert w.damage_type == "bludgeoning"
    assert w.bonus_attribute == ("strength",)
    assert w.properties == ["versatile"]
    assert w.versatile_die == (8,)
    assert w.get_damage_mod() == ("strength",)

def test_create_versatile_melee_weapons():
    w = create_versatile_melee_weapon("quarterstaff")
    assert w.name == "quarterstaff"
    assert w.weapon_type == "simple"
    assert w.damage_die == (6,)
    assert w.damage_type == "bludgeoning"
    assert w.bonus_attribute == ("strength",)
    assert w.properties == ["versatile"]
    assert w.versatile_die == (8,)
    assert w.get_damage_mod() == ("strength",)

def test_init_ranged_weapon():
    w = RangedWeapon('light crossbow', 'simple', (8,), 'piercing', ("dexterity",), ["ammunition", "ranged", "loading", "two handed"], (80, 320))
    assert w.name == "light crossbow"
    assert w.weapon_type == "simple"
    assert w.damage_die == (8,)
    assert w.damage_type == "piercing"
    assert w.bonus_attribute == ("dexterity",)
    assert w.properties == ["ammunition", "ranged", "loading", "two handed"]
    assert w.weapon_range == (80, 320)
    assert w.get_damage_mod() == ("dexterity",)

def test_create_ranged_weapon():
    w = create_ranged_weapon('light crossbow')
    assert w.name == "light crossbow"
    assert w.weapon_type == "simple"
    assert w.damage_die == (8,)
    assert w.damage_type == "piercing"
    assert w.bonus_attribute == ("dexterity",)
    assert w.properties == ["ammunition", "ranged", "loading", "two handed"]
    assert w.weapon_range == (80, 320)
    assert w.get_damage_mod() == ("dexterity",)

def test_versatile_ranged_weapon_init():
    w = VersatileRangedWeapon("trident", "martial", (6,), "piercing", ("strength",), ["thrown", "versatile"], (20, 60), (8,))
    assert w.name == "trident"
    assert w.weapon_type == "martial"
    assert w.damage_die == (6,)
    assert w.damage_type == "piercing"
    assert w.bonus_attribute == ("strength",)
    assert w.properties == ["thrown", "versatile"]
    assert w.versatile_die == (8,)
    assert w.weapon_range == (20, 60)
    assert w.get_damage_mod() == ("strength",)

def test_create_versatile_ranged_weapon():
    w = create_versatile_ranged_weapon("trident")
    assert w.name == "trident"
    assert w.weapon_type == "martial"
    assert w.damage_die == (6,)
    assert w.damage_type == "piercing"
    assert w.bonus_attribute == ("strength",)
    assert w.properties == ["thrown", "versatile"]
    assert w.versatile_die == (8,)
    assert w.weapon_range == (20, 60)
    assert w.get_damage_mod() == ("strength",)

def test_create_weapon():
    w = create_weapon("club")
    assert w.name == "club"
    assert w.weapon_type == "simple"
    assert w.damage_die == (4,)
    assert w.damage_type == "bludgeoning"
    assert w.bonus_attribute == ("strength",)
    assert w.properties == ["light"]
    assert w.get_damage_mod() == ("strength",)

    w2 = create_weapon("quarterstaff")
    assert w2.name == "quarterstaff"
    assert w2.weapon_type == "simple"
    assert w2.damage_die == (6,)
    assert w2.damage_type == "bludgeoning"
    assert w2.bonus_attribute == ("strength",)
    assert w2.properties == ["versatile"]
    assert w2.versatile_die == (8,)
    assert w2.get_damage_mod() == ("strength",)

    w3 = create_weapon("light crossbow")
    assert w3.name == "light crossbow"
    assert w3.weapon_type == "simple"
    assert w3.damage_die == (8,)
    assert w3.damage_type == "piercing"
    assert w3.bonus_attribute == ("dexterity",)
    assert w3.properties == ["ammunition", "ranged", "loading", "two handed"]
    assert w3.weapon_range == (80, 320)
    assert w3.get_damage_mod() == ("dexterity",)

    w4 = create_weapon("trident")
    assert w4.name == "trident"
    assert w4.weapon_type == "martial"
    assert w4.damage_die == (6,)
    assert w4.damage_type == "piercing"
    assert w4.bonus_attribute == ("strength",)
    assert w4.properties == ["thrown", "versatile"]
    assert w4.versatile_die == (8,)
    assert w4.weapon_range == (20, 60)
    assert w4.get_damage_mod() == ("strength",)

def test_armor_init():
    a = Armor("padded", "light", 11, True, None, True, None)
    assert a.name == "padded"
    assert a.armor_type == "light"
    assert a.ac == 11
    assert a.dex_mod == True
    assert a.dex_max == None
    assert a.stealth_penalty == True
    assert a.strength_min == None

    s = Armor("shield", "shield", 2, False, None, False, None)
    assert s.name == "shield"
    assert s.armor_type == "shield"
    assert s.ac == 2
    assert s.dex_mod == False
    assert s.dex_max == None
    assert s.stealth_penalty == False
    assert s.strength_min == None

def test_create_armor():
    a = create_armor("padded")
    assert a.name == "padded"
    assert a.armor_type == "light"
    assert a.ac == 11
    assert a.dex_mod == True
    assert a.dex_max == None
    assert a.stealth_penalty == True
    assert a.strength_min == None

    a2 = create_armor("leather")
    assert a2.name == "leather"
    assert a2.armor_type == "light"
    assert a2.ac == 11
    assert a2.dex_mod == True
    assert a2.dex_max == None
    assert a2.stealth_penalty == False
    assert a2.strength_min == None

    s = create_armor("shield")
    assert s.name == "shield"
    assert s.armor_type == "shield"
    assert s.ac == 2
    assert s.dex_mod == False
    assert s.dex_max == None
    assert s.stealth_penalty == False
    assert s.strength_min == None