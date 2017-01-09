from random import randint as rendom


def is_hit(hit_chance, evasion_chance):
    result = 0
    for var in range(11):
        if rendom(0, hit_chance) >= rendom(0, evasion_chance):
            result += 1
        else:
            result -= 1
    return result > 0


