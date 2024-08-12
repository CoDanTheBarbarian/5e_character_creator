class MeleeWeapon:
    def __init__(self, damage_die, damage_type, bonus_attribute):
        self.damage_die = damage_die
        self.damage_type = damage_type
        self.bonus_attribute = bonus_attribute

class RangedWeapon(MeleeWeapon):
    def __init__(self, damage_die, damage_type, bonus_attribute, range):
        super().__init__(damage_die, damage_type, bonus_attribute)
        self.range = range