"""Stores API library methods"""

# Python Imports

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

def __generate_report(user):
    """Generates required report for a given user

    Note:
        expenses < (income + savings) - You have a good handle of your budget
        expenses > (income + savings) - You need to cut back on your expenses
        expenses = (income + savings) - You budget is very tight

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
    pass

def insert_user(user_data, ip_address, client):
    """Inserts new user data into database

    Required Submission data from user_data:
        - Username
        - IP Address
        - At least one stream of income

    The process of insertion also fails if extra user unnecessary field data is
    sent to within the json object(user_data).

    Args:
        user_data: json object containing all user data
        ip_address: ip address of the user
        client: pymongo client used to connect to mongodb database

    Return:
        user_id: valid user_id or None
        message: Message indicating whether insertion was a success
        status_code: Relevant status code to indicate success or failure

    """
    pass

def all_users(client):
    """Retrieves all user data

    Args:
        client: pymongo client used to connect to mongodb database

    Return:
        users: json object containing a all user data denoted by their
        associated id

    """
    pass
