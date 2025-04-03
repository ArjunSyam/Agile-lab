import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    """Test cases for Flask application."""

    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()

    def test_home(self):
        """Test home route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"USN: 1RVU23CSE075")

    def test_add(self):
        """Test addition API."""
        response = self.app.get('/add?num1=5&num2=3')
        self.assertEqual(response.json["result"], 8)

if __name__ == '__main__':
    unittest.main()
