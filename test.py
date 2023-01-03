import unittest

from core import implies

data = {'a': {'c', 'd', 'f', 'b'},
        'b': {'e', 'g', 'r'}}

slightly_weird_data = {
        'a': ['c', 'd', 'f', 'b'],
        'b': ('e', 'g', 'r')}

# more testing data goes here if needed

class TestImplication(unittest.TestCase):

    def test_one(self):
        self.assertEqual(
                implies(data, ['a']),
                {'c', 'd', 'f', 'b'})

    def test_multiple(self):
        self.assertEqual(
                implies(data, ['a', 'b']),
                {'c', 'd', 'f', 'e', 'g', 'r'}) # no b in results since it was already 'known' from the input assertions

    def test_weird_data(self):
        self.assertEqual(
                implies(slightly_weird_data, ['a', 'b']),
                {'c', 'd', 'f', 'e', 'g', 'r'})

    # more tests go here ...
    # if you know how to use pytest instead of unittest, please go ahead -- it's nicer to read and write


if __name__ == '__main__':
    unittest.main()
