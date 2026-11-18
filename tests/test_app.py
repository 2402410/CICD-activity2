
import unittest
from src.app import greet


class TestGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(
            greet(),
            "Hello, Daryl! Welcome to our Updated Software Engineering Activity."
        )


if __name__ == "__main__":
    unittest.main()
