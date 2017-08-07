import unittest

from birdverse.birdverse import app

class BirdverseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to root and assert status is 200
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_home_default_response(self):
        # sends HTTP GET request to root and assert correct default response
        result = self.app.get('/') 

        # assert the data of the response
        self.assertEqual(result.data, 'Welcome to Birdverse')

    def test_home_get_a_bird(self):
        # sends HTTP GET request to root with a bird, get that bird back
        result = self.app.get('/tinamou') 

        # assert the data of the response
        self.assertEqual(result.data, 'getting a bird: tinamou')