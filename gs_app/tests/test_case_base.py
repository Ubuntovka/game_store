"""
Test case base used for set up and tear down each test.
Classes:
- `TestCaseBase`, base test case
"""
import unittest
from mongoengine.connection import connect, disconnect
from gs_app import app, db


class TestCaseBase(unittest.TestCase):

    def setUp(self) -> None:
        disconnect()
        connect('test_game_store', alias='default')
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        self.client = app.test_client()
        self.db = db.get_db()

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
