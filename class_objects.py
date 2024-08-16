# begin defining the child object 'class'(Character)
class Class:
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities):
        self.name = name
        self.hit_die = hit_die
        self.proficiencies = proficiencies
        self.prof_choice = prof_choice_list
        self.class_abilities = class_abilities

# each of the class objects need specific init arguments for class specific abilities

class Barbarian(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list, class_abilities, rage_charges):
        super().__init__(name, hit_die, proficiencies, prof_choice_list, class_abilities)
        self.rage = rage_charges

# need to establish the unique arguments for each class and set up according inits

class Bard(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list):
        super().__init__(name, hit_die, proficiencies, prof_choice_list)

class Cleric(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list):
        super().__init__(name, hit_die, proficiencies, prof_choice_list)

class Druid(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list):
        super().__init__(name, hit_die, proficiencies, prof_choice_list)

class Fighter(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list):
        super().__init__(name, hit_die, proficiencies, prof_choice_list)

class Paladin(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list):
        super().__init__(name, hit_die, proficiencies, prof_choice_list)

class Ranger(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list):
        super().__init__(name, hit_die, proficiencies, prof_choice_list)

class Rogue(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list):
        super().__init__(name, hit_die, proficiencies, prof_choice_list)

class Sorcerer(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list):
        super().__init__(name, hit_die, proficiencies, prof_choice_list)

class Warlock(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list):
        super().__init__(name, hit_die, proficiencies, prof_choice_list)

class Wizard(Class):
    def __init__(self, name, hit_die, proficiencies, prof_choice_list):
        super().__init__(name, hit_die, proficiencies, prof_choice_list)
