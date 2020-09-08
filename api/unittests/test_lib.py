# Python Imports
import unittest
import os
import sys
import json
import random

# Third-party modules
from mongomock import MongoClient
from bson.objectid import ObjectId

# Flask Imports
from flask import Flask

# PYTHONPATH
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# Application imports
from api.lib import (get_ip, ip_exists, insert_user, all_users,
                       __generate_report)

def create_user_dict(firstName, lastName):
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
            'grocery': random.randrange(20000, 25000),
            'utilities': random.randrange(5000, 10000),
            'transportation': random.randrange(5000, 10000)
        },
        'income': {
            'salary': random.randrange(200000, 6000000),
        },
        'savings': {
            'equities': random.randrange(10000, 30000),
            'pension': random.randrange(10000, 20000),
            'emergency': random.randrange(10000, 30000)
        }
    }

    return user_one


class TestLibraryModules(unittest.TestCase):
    """Tests Each method stored in the lib.py module"""

    @classmethod
    def setUpClass(self):
        """Test class setup"""

        # Need a new app to test various functionality surrounding processing
        # request objects
        self.app = Flask(__name__)
        self.client = self.app.test_client()
        self.client.testing = True

    def setUp(self):
        """Test setup upon each run"""

        # Creating user instance
        self.user = create_user_dict('Dominic', 'Henry')
        self.user['ipAddress'] = '192.0.1.20'

        # Instantiate MongoClient
        # Inserting new user instance into mock mongodb database
        self.mongo_client = MongoClient()
        self.user_collection = self.mongo_client.db.user

        # Insert new user
        self.user['_id'] = self.user_collection.insert_one(self.user).inserted_id

    def test_get_ip(self):
        """Tests get_ip"""

        # Creating mock test object because normal request object is immutable
        request = type('Request', (object,), {'remote_addr': '192.0.1.20'})()
        self.assertEqual(get_ip(request), request.remote_addr)

    def test_ip_exists(self):
        """Test ip_exists"""

        # Testing when ip address exists within mongodb database
        result = ip_exists(self.user['ipAddress'], self.mongo_client)
        self.assertTrue(result)

        # Testing when ip address does not exist within mongodb database
        result = ip_exists('127.0.10.10', self.mongo_client)
        self.assertFalse(result)

    def test___generate_report(self):
        "Test generate_report"

        # Case One: expenses < (income + savings)

        # Case Two: expenses > (income + savings)
        # Case Three: expenses = (income + savings)


    def test_insert_user(self):
        """Test insert_user"""

        # Tests that a valid user is entered correctly
        user_one = create_user_dict('Gabrielle', 'Clarke')
        user_id, message, status_code = insert_user(json.dumps(user_one),
                                                    '191.0.10.10',
                                                    self.mongo_client)

        self.assertEqual(ObjectId, type(user_id))
        self.assertEqual('Success', message)
        self.assertEqual(200, status_code)

        # Test that a invalid user is not entered
        user_two = {}
        user_id, message, status_code = insert_user(json.dumps(user_two),'193.0.10.10', self.mongo_client)

        self.assertIsNone(user_id)
        self.assertEqual('Failed', message)
        self.assertEqual('400', status_code)

    def test_all_users(self):
        """Test all_users"""

        # Inserting additional users for testing
        users = [create_user_dict('Alex', 'Lawson'), create_user_dict('Dineah',
                                                                      'Cohen')]
        user_ids = self.user_collection.insert_many(users).inserted_ids
        expected = [{**users[i], **dict(zip(['_id'], [user_ids[i]]))} for i in
                 range(len(users))]

        result = all_users(self.mongo_client)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
