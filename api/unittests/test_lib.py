# Python Imports
import unittest
import os
import sys
import random

# Third-party modules
from mongomock import MongoClient

# Flask Imports
from flask import Flask

# PYTHONPATH
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# Application imports
from api.lib import (get_ip, ip_exists, insert_user, all_users,
                       generate_report)

# Unittest utilities
from unittests.utils import create_user_dict

class TestLibraryModules(unittest.TestCase):
    """Tests Each method stored in the lib.py module"""

    def setUp(self):
        """Test setup upon each run"""

        # Creating user instance
        values = {'grocery': 10000, 'utilities': 20000, 'transportation': 5000,
                  'salary': 200000, 'equities': 20000, 'pension':
                  20000,'emergency': 20000}
        self.user = create_user_dict('Dominic', 'Henry', values)
        self.user['ipAddress'] = '192.0.1.20'

        # Adding expected generated report entries
        self.user.update({
            'totalExpenses': 35000,
            'totalSavings': 60000,
            'totalIncome': 200000,
            'leftover': 105000,
            'statement': 'You have a good handle of your budget'
        })

        # Instantiate MongoClient
        # Inserting new user instance into mock mongodb database
        self.mongo_client = MongoClient()
        self.user_collection = self.mongo_client.bdCalculator.user

        self.user_collection.insert_one(self.user)

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

    def test_generate_report(self):
        "Test generate_report"

        ########################################################################
        # Case One: expenses < (income + savings)
        ########################################################################

        values = {'grocery': 10000, 'utilities': 20000, 'transportation': 5000,
                  'salary': 200000, 'equities': 20000, 'pension':
                  20000,'emergency': 20000}
        user_one = create_user_dict('Tajhyei', 'Thompson', values)
        updated_user_one = generate_report(user_one)

        # Checking if these fields were added to existing dictionary
        self.assertEqual(updated_user_one['totalExpenses'], 35000)
        self.assertEqual(updated_user_one['totalSavings'], 60000)
        self.assertEqual(updated_user_one['totalIncome'], 200000)
        self.assertEqual(updated_user_one['leftover'], 105000)
        self.assertEqual(updated_user_one['statement'], 'You have a good handle of your budget')

        # Checking that previous fields remained intact
        # Checking that both key and value match-up
        for key in user_one.keys():
            self.assertIn(key, updated_user_one)
            self.assertEqual(user_one[key], updated_user_one[key])

        ########################################################################
        # Case Two: expenses > (income + savings)
        ########################################################################

        values = {'grocery': 10000, 'utilities': 100000, 'transportation':
                  100000, 'salary': 200000, 'equities': 0, 'pension':
                  0,'emergency': 0}
        user_one = create_user_dict('Dineah', 'Cohen', values)
        updated_user_one = generate_report(user_one)

        # Checking if these fields were added to existing dictionary
        self.assertEqual(updated_user_one['totalExpenses'], 210000)
        self.assertEqual(updated_user_one['totalSavings'], 0)
        self.assertEqual(updated_user_one['totalIncome'], 200000)
        self.assertEqual(updated_user_one['leftover'], -10000)
        self.assertEqual(updated_user_one['statement'], 'You need to cut back on your expenses')

        # Checking that preivous fields reamined intact
        # Checking that both key and value match-up
        for key in user_one.keys():
            self.assertIn(key, updated_user_one)
            self.assertEqual(user_one[key], updated_user_one[key])

        ########################################################################
        # Case Three: expenses = (income + savings)
        ########################################################################

        values = {'grocery': 10000, 'utilities': 80000, 'transportation':
                  100000, 'salary': 200000, 'equities': 5000, 'pension':
                  5000,'emergency': 0}
        user_one = create_user_dict('Ladonna', 'Larmine', values)
        updated_user_one = generate_report(user_one)

        # Checking if these fields were added to existing dictionary
        self.assertEqual(updated_user_one['totalExpenses'], 190000)
        self.assertEqual(updated_user_one['totalSavings'], 10000)
        self.assertEqual(updated_user_one['totalIncome'], 200000)
        self.assertEqual(updated_user_one['leftover'], 0)
        self.assertEqual(updated_user_one['statement'], 'Your budget is very tight')

        # Checking that preivous fields reamined intact
        # Checking that both key and value match-up
        for key in user_one.keys():
            self.assertIn(key, updated_user_one)
            self.assertEqual(user_one[key], updated_user_one[key])


    def test_insert_user(self):
        """Test insert_user"""

        # Tests that a valid user is entered correctly
        values = {'grocery': 10000, 'utilities': 100000, 'transportation':
                  100000, 'salary': 200000, 'equities': 0, 'pension':
                  0,'emergency': 0}
        ip_address = '191.0.10.10'
        user_one = create_user_dict('Gabrielle', 'Clarke', values)
        updated_user_one, message, status_code = insert_user(user_one, ip_address,
                                                    self.mongo_client)

        # Checking if these fields were added to existing dictionary
        self.assertEqual(updated_user_one['totalExpenses'], 210000)
        self.assertEqual(updated_user_one['totalSavings'], 0)
        self.assertEqual(updated_user_one['totalIncome'], 200000)
        self.assertEqual(updated_user_one['leftover'], -10000)
        self.assertEqual(updated_user_one['statement'], 'You need to cut back on your expenses')
        self.assertEqual(ip_address, updated_user_one['ipAddress'])

        # Checking that preivous fields reamined intact
        # Checking that both key and value match-up
        for key in user_one.keys():
            self.assertIn(key, updated_user_one)
            self.assertEqual(user_one[key], updated_user_one[key])

        # Checking status_code and success message
        self.assertEqual('Success', message)
        self.assertEqual(200, status_code)

        # Test that a invalid user is not entered
        user_two = {}
        updated_user_two, message, status_code = insert_user(user_two,'193.0.10.10', self.mongo_client)

        self.assertEqual({}, updated_user_two)
        self.assertEqual('Failed', message)
        self.assertEqual(400, status_code)

    def test_all_users(self):
        """Test all_users"""

        # Inserting additional users for testing
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
            'ipAddress': '190.1.0.20'
        })

        users[1].update({
            'totalExpenses': 190000,
            'totalSavings': 10000,
            'totalIncome': 200000,
            'leftover': 0,
            'statement': 'Your budget is very tight',
            'ipAddress': '190.1.0.21'
        })

        self.mongo_client.bdCalculator.user.insert_many(users)

        expected = users + [self.user]
        result = all_users(self.mongo_client)

        # Checking that all expected entries are present
        for entry in expected:
            self.assertIn(entry, result)

    def test_create_mongo_client(self):
        """Test create_mongo_client"""
        pass


if __name__ == "__main__":
    unittest.main()
