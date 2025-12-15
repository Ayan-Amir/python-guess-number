YES = 'yes'

USER_MESSAGES = {
    'CHOOSE_GUESS_NUMBER': 'Choose the number you want to guess from 1 to 100: ',
    'ENTER_VALID_NUMBER': 'Kindly enter valid number',
    'GUESS_NUMBER': 'Guess the number from 1 to 100: ',
    'NUMBER_RANGE' : 'Number should be in the range of 1 to 100',
    'NUMBER_RE_GUESS': 'Want to guess number again ? Yes / No: ',
    'CORRECT_NUMBER': lambda attempts: f'Correct number, user took {attempts} attempt(s) to solve this',
    'GAME_OVER': 'Game over!',
    'TOO_LARGE': 'Too large',
    'TOO_SMALL': 'Too small'
}

ERROR_MESSAGE = {
    'NUMBER_RANGE': 'error: the guessing number should be in the range of 1 to 100'
}