"""Stores API library methods"""

# Python Imports
import functools
import json

# TODO verify that request passes valid ip address
def get_ip(request):
    """Determines user IP address

    Args:
        request: resquest object

    Return:
        ip_address: requesting machine's ip address (PUBLIC)

    """
    ip_address = request.remote_addr
    return ip_address

def ip_exists(ip_address, client):
    """Determines whether an IP address already exists in database

    Args:
        ip_address
        client: pymongo client used to connect to mongodb database

    Return:
        exists: boolean indicating whether an IP address exists in database

    """
    user_collection = client.db.user
    exists = bool(user_collection.find_one({'ipAddress': ip_address}))
    return exists

def generate_report(user):
    """Generates required report for a given user

    Note:
        expenses < (leftover + savings) - You have a good handle of your budget
        expenses > (leftover + savings) - You need to cut back on your expenses
        expenses = (leftover + savings) - Your budget is very tight

    Args:
        user: dictionary containing user data

    Return:
        report: dictionary containing additional reported information

        report = {
            'firstName': 'Dominic',
            'lastName': 'Henry',
            ...
            totalExpenses: 50000
            totalSavings: 170000
            totalIncome: 300000
            leftover: 80000,
            statement: 'You have a good handle of your budget'
        }

    """
    def __(category):
        """Consolidates a given category"""
        return functools.reduce(lambda x, y: x + y, user[category].values())

    user['totalExpenses'] = __('expense')
    user['totalSavings'] = __('savings')
    user['totalIncome'] = __('income')
    user['leftover'] = user['totalIncome'] - (user['totalExpenses'] +
                                              user['totalSavings'])

    # Setting statements
    if user['leftover'] > 0:
        user['statement'] = 'You have a good handle of your budget'
    elif user['leftover'] < 0:
        user['statement'] = 'You need to cut back on your expenses'
    else:
        user['statement'] = 'Your budget is very tight'

    return user

def insert_user(user_data, ip_address, client):
    """Inserts new user data into database

    Required Submission data from user_data:
        - First name
        - Last Name
        - IP Address
        - At least one stream of income

    The process of insertion also fails if extra user unnecessary field data is
    sent to within the json object(user_data).

    Args:
        user_data: json object containing all user data
        ip_address: ip address of the user
        client: pymongo client used to connect to mongodb database

    Return:
        user: valid user dictionary or None
        message: Message indicating whether insertion was a success
        status_code: Relevant status code to indicate success or failure

    """
    user, message, status_code = None, 'Failed', 400

    # Checking that user_data has all required entries
    required = ['firstName', 'lastName', 'income']
    optional = ['expense', 'savings']

    # Counts that required entries are present in `user_data`
    # This will work because dictionaries cannot have duplicate keys
    # Thus required_count can only be capped at the lengths of required list
    required_count = 0
    valid_user = True

    # Converting user_data to dictionary
    user_data = json.loads(user_data)

    for entry in user_data.keys():
        if entry in required:
            required_count += 1
            continue
        elif entry in optional:
            continue
        else:
            break

    if (required_count == len(required)) and valid_user:
        user = generate_report(user_data)
        user['ipAddress'] = ip_address

        # Inserting new user
        _id = client.db.user.insert_one(user).inserted_id

        # Proper ObjectId would indicate a truthy value and a successfully
        # intserted user
        if bool(_id):
            message, status_code = 'Success', 200

    return user, message, status_code

def all_users(client):
    """Retrieves all user data

    Args:
        client: pymongo client used to connect to mongodb database

    Return:
        users: json object containing a all user data denoted by their
        associated id

    """
    users = []
    for user in client.db.user.find():
        users.append(user)
    return users
