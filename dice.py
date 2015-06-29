import math
import random


def d(sides):
    '''
    :param sides: integer, sides on the die to be rolled
    :return: integer, random value in range of sides
    '''
    return int(math.ceil(random.random() * sides))


def d6(pool):
    '''
    :param pool: integer, die pool size
    :return: list, result of die pool
    '''
    result = []
    for die in range(pool):
        roll = d(6)
        result.append(roll)
    print(result)
    return result


def check(difficulty, result):
    '''
    :param difficulty: integer, difficulty roll must beat to be considered a success
    :return: integer, number of successes (wins)
    '''
    wins = 0
    for die in result:
        if die >= difficulty:
            wins += 1
    return "successes: " + str(wins)
