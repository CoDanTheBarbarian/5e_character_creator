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
    stat_1 = roll_stat()
    stat_2 = roll_stat()
    stat_3 = roll_stat()
    stat_4 = roll_stat()
    stat_5 = roll_stat()
    stat_6 = roll_stat()
    return [stat_1, stat_2, stat_3, stat_4, stat_5, stat_6]