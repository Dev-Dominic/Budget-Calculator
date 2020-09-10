"""Stores utiliy methods for tests"""

def create_user_dict(firstName, lastName, values):
    """Creates a new user dictionary for testing

    Args:
        firstName
        lastName

    Return:
        user: dictionary containing random user data

    """
    user_one = {
        'firstName': firstName,
        'lastName': lastName,
        'expense': {
            'grocery': values['grocery'],
            'utilities': values['utilities'],
            'transportation': values['transportation']
        },
        'income': {
            'salary': values['salary']
        },
        'savings': {
            'equities': values['equities'],
            'pension': values['pension'],
            'emergency': values['emergency']
        }
    }

    return user_one
