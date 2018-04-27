"""Unit Test for Cloud Realty"""
import unittest
from flask import Flask
from flask_fast_cache import FastCache


class BaseTest(unittest.TestCase):
    """Base Testing Class for setting up Flask App"""
    app = None
    cache = None

    def setUp(self):
        self.app = Flask(__name__)
        self.cache = FastCache.setup()
        self.app.config['SERVER_NAME'] = 'localhost'
        self.client = self.app.test_client()
        with self.app.app_context():
            pass

    def tearDown(self):
        with self.app.app_context():
            pass


if __name__ == '__main__':
    unittest.main()
