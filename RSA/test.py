import unittest
from encrypt import is_prime


class RSATestCase(unittest.TestCase):

    """ Tests for `encrypt.py`. """

    # First we will test the prime no. module.
    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index))


if __name__ == '__main__':
    unittest.main()
