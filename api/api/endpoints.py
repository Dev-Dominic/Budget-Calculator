from api import app

@app.route('/create')
def create():
    """Creates new user submission

    Args:
        request: Each endpoint receies a http request body

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

    """
    return 'create'

@app.route('/all-users')
def all_users():
    """Retrieves all users submissions

    Args:
        request: each endpoint receives a http request body

    Return:
        users: returns list of user submissions
        status_code: 200

    """
    return 'all-users'
