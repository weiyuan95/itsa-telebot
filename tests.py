import unittest
from tasker.helpers.register_helper import all_lowercase

class Tests(unittest.TestCase):
    def test_lowercase_success(self):
        string = 'abc'
        self.assertEqual(all_lowercase(string), True)
        string = 'a12.c'
        self.assertEqual(all_lowercase(string), True)

    def test_lowercase_failure(self):
        string = 'aBc'
        self.assertEqual(all_lowercase(string), False)
        string = 'a12.B'
        self.assertEqual(all_lowercase(string), False)


if __name__ == '__main__':
    unittest.main()