# Python Imports
import unittest
import os
import sys
import socket
import json
import random

# Flask Imports
from flask import Flask

# PYTHONPATH
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# API Imports
from api import app, client

# Unittest utilities
from unittests.utils import create_user_dict

class TestEndpoints(unittest.TestCase):
    """Tests all api endpoints"""

    @classmethod
    def setUpClass(self):
        """Setups mock flask application"""

        self.app = app.test_client()

        # Used to set test ipAddress for app context's request body
        self.headers = {'Content-Type': 'application/json'}
        self.environ_base = {'REMOTE_ADDR': socket.gethostbyname(socket.gethostname())}

        self.ipAddress = socket.gethostbyname(socket.gethostname())

    def tearDown(self):
        """Teardowns mongodb user database each test"""

        client.db.user.drop()

    def test_create(self):
        """Test create endpoints"""

        ########################################################################
        # Inserting valid user
        ########################################################################

        values = {'grocery': 10000, 'utilities': 100000, 'transportation':
                  100000, 'salary': 200000, 'equities': 0, 'pension':
                  0,'emergency': 0}
        user_data = create_user_dict('Tajhyei', 'Thompson', values)
        expected_user = user_data
        valid_payload = json.dumps(user_data)

        # Making request to 'create' endpoint
        response = None
        response = self.app.post('/create', environ_base=self.environ_base,
                                 headers=self.headers, data=valid_payload)

        expected_user.update({
            'totalExpenses': 210000,
            'totalSavings': 0,
            'totalIncome': 200000,
            'leftover': -10000,
            'statement': 'You need to cut back on your expenses',
            'ipAddress': self.ipAddress
        })

        expected_message = 'Success'
        response_user = response.get_json()['user']
        response_message = response.get_json()['message']

        # Ommitts '_id' from user response to test every other field
        _id = response_user['_id']
        del response_user['_id']

        self.assertEqual(expected_user, response_user)
        self.assertGreater(len(_id), 1)
        self.assertEqual(expected_message, response_message)
        self.assertEqual(200, response.status_code)

        ########################################################################
        # Inserting invalid user
        ########################################################################

        invalid_payload = json.dumps({})
        response = self.app.post('/create', environ_base=self.environ_base,
                                 headers=self.headers, data=invalid_payload)

        expected_message = 'Failed'
        response_user = response.get_json()['user']
        response_message = response.get_json()['message']

        self.assertEqual({}, response_user)
        self.assertEqual(expected_message, response_message)
        self.assertEqual(400, response.status_code)

    def test_all_users(self):
        """Test all_users endpoints"""

        # Inserting users for testing
        values_one = {'grocery': 10000, 'utilities': 100000, 'transportation':
                  100000, 'salary': 200000, 'equities': 0, 'pension':
                  0,'emergency': 0}
        values_two = {'grocery': 10000, 'utilities': 80000, 'transportation':
                  100000, 'salary': 200000, 'equities': 5000, 'pension':
                  5000,'emergency': 0}

        # Creating base users
        users = [
            create_user_dict('Alex', 'Lawson', values_one),
            create_user_dict('Dineah', 'Cohen', values_two),
        ]

        users[0].update({
            'totalExpenses': 210000,
            'totalSavings': 0,
            'totalIncome': 200000,
            'leftover': -10000,
            'statement': 'You need to cut back on your expenses',
            'ipAddress': ipAddress
        })

        users[1].update({
            'totalExpenses': 190000,
            'totalSavings': 10000,
            'totalIncome': 200000,
            'leftover': 0,
            'statement': 'Your budget is very tight',
            'ipAddress': ipAddress
        })

        client.db.user.insert_many(users)
        response = self.app.get('/all-users', environ_base=self.environ_base,
                                headers=self.headers)

        # Changing ObjectId for expected users to a string
        for user in users:
            user['_id'] = str(user['_id'])

        response_users = response.get_json()['users']

        self.assertEqual(users, response_users)
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()
