# Python Imports
import unittest
import os
import sys

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

class TestLibraryModules(unittest.TestCase):
    """Tests Each method stored in the lib.py module"""

    @classmethod
    def setUpClass(self):
        """Test class setup"""
        self.app = Flask(__name__)
        self.client = self.app.test_client()
        self.client.testing = True

        user_test_collection = MongoClient.db.collection()



    def test_get_ip(self):
        """Tests get_ip"""

        # Creating mock test object because normal request object is immutable
        request = type('Request', (object,), {'remote_addr': '192.0.1.20'})()
        self.assertEqual(get_ip(request), request.remote_addr)

    def ip_exists(self):
        """Test ip_exists"""


if __name__ == "__main__":
    unittest.main()
