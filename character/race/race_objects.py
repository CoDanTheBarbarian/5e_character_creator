class Race:
    def __init__(self, race, speed, stat_bonus, proficiencies, resistances, prof_choices, subraces):
        self.race = race
        self.speed = speed
        self.stat_bonus = stat_bonus
        self.proficiencies = proficiencies
        self.resistance = resistances
        self.prof_choices = prof_choices
        self.subraces = subraces
        # if subraces is not an empty list, continue to choose subrace and input that into subrace class

class SubRace:
    def __init__(self, subrace, stat_bonus, proficiencies, resistances, hp_bonus, speed_bonus):
        self.subrace = subrace
        self.stat_bonus = stat_bonus
        self.proficiencies = proficiencies
        self.resistances = resistances
        self.hp_bonus = hp_bonus
        self.speed_bonus = speed_bonus

class DragonColor(SubRace):
    def __init__(self, subrace, stat_bonus, proficiencies, resistances, hp_bonus, speed_bonus, breath_shape, breath_size, breath_type):
        super().__init__(subrace, stat_bonus, proficiencies, resistances, hp_bonus, speed_bonus)
        self.breath_shape = breath_shape
        self.breath_size = breath_size
        self.breath_type = breath_type
