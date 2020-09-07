"""Stores API library methods"""

# Python Imports

# TODO verify that request passes valid ip address
def get_ip(request):
    """Determines user IP address

    Args:
        request: resquest object

    Return:
        ip_address: requesting machine's ip addresss (PUBLIC)

    """
    ip_address = request.remote_addr
    return ip_address

def ip_exists(ip_address):
    """Determines whether an IP address already exists in database

    Args:
        ip_address

    Return:
        exists: boolean indicating whether an IP address exists in database

    """
    pass

def insert_user(user_data, ip_address):
    """Inserts new user data into database

    Required Submission data from user_data:
        - Username
        - IP Address
        - At least one stream of income

    The process of insertion also fails if extra user unneccsary field data is
    sent to within the json object(user_data).

    Args:
        user_data: json object containing all user data
        ip_address: ip address of the user

    Return:
        user_id: valid user_id or None
        message: Message indicating whether inerstion was a success
        status_code: Relevant status code to indicate success or failure

    """
    pass

def all_users():
    """Retrieves all user data

    Args:
        None

    Return:
        users: json object containing a all user data denoted by their
        associated id

    """
    pass

def generate_report(user_id):
    """Generates required report for a given user

    Note:
        expenses < (income + savings) - You have a good handle of your budget
        expenses > (income + savings) - You need to cut back on your expenses
        expenses < (income + savings) - You budget is very tight

    Args:
        user_id

    Return:
        all_users: json object containing summary of user information

    """
    pass
