from constants import YES, USER_MESSAGES, ERROR_MESSAGE

# guess the correct number

attempts = 0
number_guessed = False

try:
    guessing_number = int(input(USER_MESSAGES['CHOOSE_GUESS_NUMBER']))
    if guessing_number > 100 or guessing_number < 1:
        print(USER_MESSAGES['NUMBER_RANGE'])
        exit()
except ValueError:
    print(USER_MESSAGES['ENTER_VALID_NUMBER'])
    exit()

while not number_guessed:
    try:
        user_input = int(input(USER_MESSAGES['GUESS_NUMBER']))
    except:
        print(USER_MESSAGES['ENTER_VALID_NUMBER'])
        continue

    if user_input > 100 or user_input < 1:
        print(ERROR_MESSAGE['NUMBER_RANGE'])
        played_again = input(USER_MESSAGES['NUMBER_RE_GUESS']).lower()

        if played_again == YES:
            continue
        else:
            print(USER_MESSAGES['GAME_OVER'])
            break

    attempts += 1

    if user_input == guessing_number:
       print(USER_MESSAGES['CORRECT_NUMBER'](attempts))
       number_guessed = True
    elif user_input > guessing_number:
        print(USER_MESSAGES['TOO_LARGE'])
    else:
        print(USER_MESSAGES['TOO_SMALL'])
