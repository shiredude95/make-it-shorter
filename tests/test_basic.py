import unittest
from context import helper
import application
from flask import Flask

class TestApplication(unittest.TestCase):


    def test_shorter_bad_route(self):
        app = Flask(__name__)
        with app.test_client() as c:
            response = c.get('/shortest')
            self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()