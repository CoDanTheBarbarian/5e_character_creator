class Class:
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment):
        self.name = name
        self.hit_die = hit_die
        self.proficiencies = proficiencies
        self.prof_choice = prof_choice_list
        self.class_abilities = class_abilities
        self.starting_equipment = starting_equipment

class Barbarian(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, rage_charges):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.rage = rage_charges

class Bard(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, spells_known, bardic_die):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known
        self.bardic_die = bardic_die

class Cleric(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, domain, channel_divinity_slots):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.domain = domain
        self.channel = channel_divinity_slots

class Druid(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots

class Fighter(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, fighting_style):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.fighting_style = fighting_style

class Monk(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, ki_points):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.ki = ki_points

class Paladin(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, lay_on_hands_charges):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.lay_on_hands = lay_on_hands_charges

class Ranger(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)

class Rogue(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, sneak_attack_die):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.sneak_attack_die = sneak_attack_die

class Sorcerer(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, spells_known, origin):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known
        self.origin = origin

class Warlock(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, spells_known, patron):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known
        self.patron = patron

class Wizard(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment, spell_casting_ability, spell_slots, spells_known):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities, starting_equipment)
        self.spell_casting_ability = spell_casting_ability
        self.spell_slots = spell_slots
        self.spells_known = spells_known
