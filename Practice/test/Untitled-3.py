import unittest

class teststring(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper,'Foo')

