# Python Imports
import unittest
import os
import sys
import socket
import json
import random

# Flask Imports
from flask import Flask

# Unittest utilities
from utils import create_user_dict

# PYTHONPATH
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# API Imports
from api import app, client


class TestEndpoints(unittest.TestCase):
    """Tests all api endpoints"""

    @classmethod
    def setUpClass(self):
        """Setups mock flask application"""

        self.app = app.test_client()

    def test_create(self):
        """Test create endpoints"""

        headers = {'Content-Type': 'application/json'}

        ########################################################################
        # Inserting valid user
        ########################################################################

        values = {'grocery': 10000, 'utilities': 100000, 'transportation':
                  1000000, 'salary': 200000, 'equities': 0, 'pension':
                  0,'emergency': 0}
        user_data = create_user_dict('Tajhyei', 'Thompson', values)
        expected = user_data
        valid_payload = json.dumps(user_data)

        # Making request to 'create' endpoint
        response = self.app.post('/create', headers=headers, data=valid_payload)

        expected.update({
            'totalExpenses': 210000,
            'totalSavings': 0,
            'totalIncome': 200000,
            'leftover': -10000,
            'statement': 'You need to cut back on your expenses',
            'ipAddress': socket.gethostbyname(socket.gethostname())
        })

        self.assertEqual(expected, response.get_json())
        self.asssertEqual(200, response.status_code)

        ########################################################################
        # Inserting invalid user
        ########################################################################

        invalid_payload = json.dumps({})
        response = self.app.post('/create', headers=headers, data=invalid_payload)

        self.assertIsNone(response.get_json())
        self.assertEqual(400, response.status_code)

    def test_all_users(self):
        """Test all_users endpoints"""

        # Inserting users for testing
        values_one = {'grocery': 10000, 'utilities': 100000, 'transportation':
                  1000000, 'salary': 200000, 'equities': 0, 'pension':
                  0,'emergency': 0}
        values_two = {'grocery': 10000, 'utilities': 80000, 'transportation':
                  1000000, 'salary': 200000, 'equities': 5000, 'pension':
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
            'ipAddress': socket.gethostbyname(socket.gethostname())
        })

        users[1].update({
            'totalExpenses': 190000,
            'totalSavings': 10000,
            'totalIncome': 200000,
            'leftover': 0,
            'statement': 'Your budget is very tight',
            'ipAddress': socket.gethostbyname(socket.gethostname())
        })

        client.db.user.insert_many(users).inserted_ids
        response = self.app.get('/all-users')

        self.assertEqual(users, json.loads(response.get_json()))
        self.asssertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()
