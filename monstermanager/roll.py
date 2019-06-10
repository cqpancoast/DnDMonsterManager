import random


# Takes in a string representing a roll and returns the computed value
def roll(roll_string):

    if roll_string == "":
        d20_result = random.randint(1, 20)
        if d20_result == 20:
            print("CRITICAL HIT!!!")
        elif d20_result == 1:
            print("CRITICAL MISS!!!")
        return d20_result

    roll_values = roll_string.lower()\
        .replace(" ", "")\
        .replace("d", " ")\
        .replace("+", " ")\
        .split(" ")

    roll_values_all_ints = True
    for value in roll_values:
        if not represents_int(value):
            roll_values_all_ints = False

    if not roll_values_all_ints:
        print("Sorry; I don't understand. I'll just roll 1d20.")
        return random.randint(1, 20)
    elif len(roll_values) == 3:
        value_so_far = int(roll_values[2])
    elif len(roll_values) == 2:
        value_so_far = 0
    else:
        print("Sorry; I don't understand. I'll just roll 1d20.")
        return random.randint(1, 20)

    for i in range(int(roll_values[0])):
        value_so_far += random.randint(1, int(roll_values[1]))

    return value_so_far


# Tests if string represents int — Sourced from:
# https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
