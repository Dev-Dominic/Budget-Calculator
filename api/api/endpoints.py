# API Imports
from api import app, client
from api.lib import get_ip, insert_user, all_users

# Flask Imports
from flask import jsonify, request

@app.route('/api/create', methods=['POST'])
def create():
    """Creates new user submission

    Args:
        request: Each endpoint receives a http request body

    Return:
        user:
            - Valid Submission: New user submission json with generate report
            - Invalid Submission: json with null
        message:
            - Valid: Success
            - Invalid: Failed
        status_code:
            - Valid: 200
            - Invalid: 400

        {
            message: 'Success',
            user: {
                'firstName': 'Dominic',
                'lastName': 'Henry',
                ...
            }
        }

    """
    ip_address = get_ip(request)
    user_data = request.get_json()
    user, message, status_code = insert_user(user_data, ip_address, client)

    # Converts ObjectId of user to string, because ObjectId instance isn't JSON
    # serializable
    if not user == {}:
        user['_id'] = str(user['_id'])

    return jsonify(message=message, user=user), status_code

@app.route('/api/all-users')
def get_users():
    """Retrieves all users submissions

    Args:
        request: each endpoint receives a http request body

    Return:
        users: returns list of user submissions, returns empty list otherwise
        status_code: 200

    """
    users = all_users(client)

    # Converting each user's '_id' ObjectId instance to a string, because it's
    # not JSON serializable
    for user in users:
        user['_id'] = str(user['_id'])

    status_code = 200
    return jsonify(users=users), status_code
