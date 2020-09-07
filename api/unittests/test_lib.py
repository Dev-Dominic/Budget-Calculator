# Python Imports
import unittest
import os
import sys

# PYTHONPATH
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# Application imports
from api import app
from api.lib import (get_ip, ip_exists, insert_user, all_users,
                       generate_report)

class TestLibraryModules(unittest.TestCase):
    """Tests Each method stored in the lib.py module"""

    @classmethod
    def setUpClass(self):
        """Test class setup"""
        self.app = app.test_client()
        self.app.testing = True

    def test_get_ip(self):
        """Tests get_ip"""
        pass

if __name__ == "__main__":
    untitest.main()
