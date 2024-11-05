import random
def roll_d_4():
    return random.randint(1, 4)

def roll_d_6():
    return random.randint(1, 6)

def roll_d_8():
    return random.randint(1, 8)

def roll_d_10():
    return random.randint(1, 10)

def roll_d_12():
    return random.randint(1, 12)

def roll_d_20():
    return random.randint(1, 20)

def roll_stat():
    die_1 = roll_d_6()
    die_2 = roll_d_6()
    die_3 = roll_d_6()
    die_4 = roll_d_6()
    result = sorted([die_1, die_2, die_3, die_4])
    result = result[1:]
    return sum(result)

def get_random_stats():
    stats = [roll_stat() for _ in range(6)]
    return sorted(stats, reverse=True)

# numbers is a list of die numbers to handle cases where we roll more than one dice for a single result (i.e. multiple d6 for sneak attack damage)
def roll_dice(numbers):
    result = 0
    for number in numbers:
        if number == 4:
            roll = roll_d_4()
        elif number == 6:
            roll = roll_d_6()
        elif number == 8:
            roll = roll_d_8()
        elif number == 10:
            roll = roll_d_10()
        elif number == 12:
            roll = roll_d_12()
        elif number == 20:
            roll = roll_d_20()
        result += roll
    return result