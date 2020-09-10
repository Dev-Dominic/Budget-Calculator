# Python Imports
import unittest
import os
import sys
import json
import random

# Flask Imports
from flask import Flask

# PYTHONPATH
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# API endpoint methods
from api import app


class TestEndpoints(unittest.TestCase):
    """Tests all api endpoints"""

    @classmethod
    def setUpClass(self):
        """Setups mock flask application"""

        self.app = app.test_client()

    def test_create(self):
        """Test create endpoints"""

        response = self.app.get('/create')

    def test_all_users(self):
        """Test all_users endpoints"""

        response = self.app.get('/all-users')


if __name__ == "__main__":
    unittest.main()
