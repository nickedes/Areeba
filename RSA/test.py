import unittest
from encrypt import is_prime


class RSATestCase(unittest.TestCase):

    """ Tests for `encrypt.py`. """

    # First we will test the prime no. module.
    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()
