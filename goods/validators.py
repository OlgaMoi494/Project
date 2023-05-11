from errors import IncorrectUserInputError


def decor_validate(validator_function):
    def wrapper(*args, **kwargs):
        try:
            validator_function(*args, **kwargs)
            return True
        except IncorrectUserInputError as err:
            print(err)
    return wrapper


@decor_validate
def validate_user_choice(value):
    if not value.isdigit():
        raise IncorrectUserInputError("User choice should be number.")
    if value not in map(str, range(1, 8)):
        raise IncorrectUserInputError("User choice should from 1 to 7.")


@decor_validate
def validate_item_quantity(value):
    if not value.isdigit():
        raise IncorrectUserInputError("User choice should be number.")
