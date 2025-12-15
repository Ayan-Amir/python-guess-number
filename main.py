# guess the correct number

attempts = 0
number_guessed = False

try:
    guessing_number = int(input('Choose the number you want to guess from 1 to 100: '))
    if guessing_number > 100 or guessing_number < 1:
        print('Number should be in the range of 1 to 100')
        exit()
except ValueError:
    print('Kindly enter valid number')
    exit()

while not number_guessed:
    try:
        user_input = int(input('Guess the number from 1 to 100: '))
    except:
        print('Enter Valid number')
        continue

    if user_input > 100 or user_input < 1:
        print('error: the guessing number should be in the range of 1 to 100')
        played_again = input('Want to guess number again ? Yes / No: ').lower()

        if played_again == 'yes':
            continue
        else:
            print('Game over!')
            break

    attempts += 1

    if user_input == guessing_number:
       print(f'correct number, user take {attempts} attempt to solve this')
       number_guessed = True
    elif user_input > guessing_number:
        print('too large')
    else:
        print('too small')
