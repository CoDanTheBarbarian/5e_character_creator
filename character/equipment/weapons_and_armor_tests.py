import unittest
from weapon_and_armor_objects import MeleeWeapon, VersatileMeleeWeapon

class TestMeleeWeapon(unittest.TestCase):
    def test_init(self):
        weapon = MeleeWeapon("Longsword", "martial", (8,), "slashing", "strength", ["versatile"])
        self.assertEqual(weapon.name, "Longsword")
        self.assertEqual(weapon.weapon_type, "martial")
        self.assertEqual(weapon.damage_die, (8,))
        self.assertEqual(weapon.damage_type, "slashing")
        self.assertEqual(weapon.bonus_attribute, "strength")
        self.assertEqual(weapon.properties, ["versatile"])

    def test_get_weapon_damage_mod(self):
        weapon = MeleeWeapon("Longsword", "martial", (8,), "slashing", "strength", ["versatile"])
        self.assertEqual(weapon.get_weapon_damage_mod(), "strength")

    def test_repr(self):
        weapon = MeleeWeapon("Longsword", "martial", (8,), "slashing", "strength", ["versatile"])
        self.assertEqual(repr(weapon), "Longsword")

class TestVersatileMeleeWeapon(unittest.TestCase):
    def test_init(self):
        weapon = VersatileMeleeWeapon("Longsword", "martial", (8,), "slashing", "strength", ["versatile"], (10,))
        self.assertEqual(weapon.name, "Longsword")
        self.assertEqual(weapon.weapon_type, "martial")
        self.assertEqual(weapon.damage_die, (8,))
        self.assertEqual(weapon.damage_type, "slashing")
        self.assertEqual(weapon.bonus_attribute, "strength")
        self.assertEqual(weapon.properties, ["versatile"])
        self.assertEqual(weapon.two_handed_damage_die, (10,))

    def test_repr(self):
        weapon = VersatileMeleeWeapon("Longsword", "martial", (8,), "slashing", "strength", ["versatile"], (10,))
        self.assertEqual(repr(weapon), "Longsword")

if __name__ == "__main__":
    unittest.main()