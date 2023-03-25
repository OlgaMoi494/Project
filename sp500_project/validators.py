from errors import IncorrectUserInputError
import string


def decor_validate(validator_function):
    def wrap(check_input, *args, **kwargs):
        try:
            validator_function(check_input, *args, **kwargs)
            return True
        except IncorrectUserInputError as err:
            print(err)

    return wrap


@decor_validate
def validate_user_choice(check_input, *args, **kwargs):
    if not check_input.isdigit():
        raise IncorrectUserInputError('Choice must be digit.')
    if check_input not in map(str, range(1, 12)):
        raise IncorrectUserInputError('Choice must be from 1 to 11.')


@decor_validate
def validate_symbol_input(check_input, *args, **kwargs):
    if len(check_input) not in range(3, 7):
        raise IncorrectUserInputError(
            'Length of symbol should be from 3 to 6 letters.')
    for letter in check_input:
        if letter not in string.ascii_letters:
            raise IncorrectUserInputError('Symbol should latin letters.')


@decor_validate
def validate_name_input(check_input, *args, **kwargs):
    if len(check_input) not in range(3, 51):
        raise IncorrectUserInputError(
            'Length of company name should be from 3 to 50 letters.')


@decor_validate
def validate_price(check_input, *args, **kwargs):
    if check_input not in map(str, range(1001)):
        raise IncorrectUserInputError(
            "Price should be float positive number to max 1000.")


@decor_validate
def validate_number_of_entries(check_input, *args, **kwargs):
    if not check_input.isdigit:
        raise IncorrectUserInputError('Number must be digit.')

    elif check_input not in map(str, range(10001)):
        raise IncorrectUserInputError(
            "Number of entries should be integer positive number to max 10000."
        )
