import unittest
from pks_app.reverse_hash import reverse_hash


class TestReversHash(unittest.TestCase):
    def test_reverse_hash(self):
        res = reverse_hash(680131659347)
        self.assertEqual(res, 'leepadg')

    def test_reverse_hash_error(self):
        with self.assertRaises(TypeError) as context:
            reverse_hash('test_string')
        self.assertTrue('Argument should be of Integer type')


if __name__ == '__main__':
    unittest.main()