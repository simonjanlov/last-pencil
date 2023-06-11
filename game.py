import string
import random

ok_deductions = ['1', '2', '3']


def is_only_numeric(value):  # return True if the value is not None or empty, and only contains digits
    if value is None or value == "":
        print("The number of pencils should be numeric ")
        return False
    else:
        for letter in value:
            if letter not in string.digits:
                print("The number of pencils should be numeric ")
                return False
        return True


def is_positive_integer(value):  # return True if the value is greater than 0
    if value <= 0:
        print("The number of pencils should be positive")
        return False
    return True


def accepted_amount(value):
    if value not in ok_deductions:
        return False
    return True


def not_more_than_remaining(removed, remaining):
    try:
        removed_num = int(removed)
    except ValueError:
        return False
    else:
        if removed_num > remaining:
            return False
        else:
            return True


def execute_bots_play(remaining_pencils):
    if remaining_pencils == 1:
        deduct = 1
    elif (remaining_pencils + 4) % 4 == 0:
        deduct = 3
    elif (remaining_pencils + 4) % 4 == 3:
        deduct = 2
    elif (remaining_pencils + 4) % 4 == 2:
        deduct = 1
    else:
        deduct = random.randint(1, 3)
    return str(deduct)


number_of_pencils = ""
print("How many pencils would you like to use: ")

amount_ok = False
while not amount_ok:  # prompt user for a number until the input is acceptable
    number_of_pencils = input()
    amount_ok = is_only_numeric(number_of_pencils)
    if amount_ok:
        number_of_pencils = int(number_of_pencils)
        amount_ok = is_positive_integer(number_of_pencils)


players = ["Tony", "Silvio"]  # list of included players (player and bot)
print(f"Who will be the first ({players[0]}, {players[1]}): ")
player_1 = input()

while player_1 not in players:  # prompt user again, repeatedly, if the given name is not one of the included players
    print(f"Choose between '{players[0]}' and '{players[1]}'")
    player_1 = input()

if player_1 == players[0]:  # set the bot as player_2
    player_2 = players[1]
    bots_turn = False
else:
    player_2 = players[0]  # set the human player as player_2
    bots_turn = True
# print the initial amount of pencils
for pencil in range(number_of_pencils):
    print("|", end="")

print()
player_1s_turn = True  # boolean value decides if it's currently player 1's turn or not
while number_of_pencils > 0:
    amount_ok = False
    if player_1s_turn:
        print(f"{player_1}'s turn! ")
        if bots_turn:
            removed_pencils = execute_bots_play(number_of_pencils)
            print(removed_pencils)
            bots_turn = not bots_turn
        else:
            removed_pencils = input()
            amount_ok = accepted_amount(removed_pencils) and not_more_than_remaining(removed_pencils, number_of_pencils)
            while not amount_ok:
                if removed_pencils not in ok_deductions:
                    print(f"Possible values: '{ok_deductions[0]}', '{ok_deductions[1]}' or '{ok_deductions[2]}'")
                else:
                    print("Too many pencils were taken")
                removed_pencils = input()
                amount_ok = accepted_amount(removed_pencils) \
                    and not_more_than_remaining(removed_pencils, number_of_pencils)
            bots_turn = not bots_turn
        player_1s_turn = not player_1s_turn
    else:
        print(f"{player_2}'s turn! ")
        if bots_turn:
            removed_pencils = execute_bots_play(number_of_pencils)
            print(removed_pencils)
            bots_turn = not bots_turn
        else:
            removed_pencils = input()
            amount_ok = accepted_amount(removed_pencils) and not_more_than_remaining(removed_pencils, number_of_pencils)
            while not amount_ok:
                if removed_pencils not in ok_deductions:
                    print(f"Possible values: '{ok_deductions[0]}', '{ok_deductions[1]}' or '{ok_deductions[2]}'")
                else:
                    print("Too many pencils were taken")
                removed_pencils = input()
                amount_ok = accepted_amount(removed_pencils) \
                    and not_more_than_remaining(removed_pencils, number_of_pencils)
            bots_turn = not bots_turn
        player_1s_turn = not player_1s_turn

    removed_pencils = int(removed_pencils)

    number_of_pencils -= removed_pencils
    for pencil in range(number_of_pencils):
        print("|", end="")
    print()

if player_1s_turn:
    print(f"{player_1} won!")
else:
    print(f"{player_2} won!")
