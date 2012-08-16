import random
from unittest import TestCase

__author__ = 'bunnyman'


class LynxGen(object):
    def __init__(self):
        ## Keypass parameters
        self._keyStart = 'LYNX'
        self._keyLength = (20, 40)
        self._validChars = {'l': 1, 'y': 2, 'n': 3, 'x': 4,
                            'L': -4, 'Y': -3 , 'N': -2, 'X': -1}

    def check_pass(self, keyString):
        if len(keyString) < 20 or len(keyString) > 40:
            return False
        if not keyString.startswith('LYNX'):
            return False
        if sum([ self._validChars.get(x) for x in str(keyString) ]) != 0:
            return False
        return True

    def get_random_key(self):
        random.seed(self)
        key = "N"
        chars = self._validChars.keys()
        while not self.check_pass(key):
            key = self._keyStart
            length = random.randint(self._keyLength[0], self._keyLength[1])
            key += "".join([random.choice(chars) for x in xrange(len(key), length)])
        return key


class LynxGen_test(TestCase):
    def test_good_key(self):
        keygen = LynxGen()
        testKey = 'LYNXlynxLYNXlynxLYnx'
        self.assertTrue(keygen.check_pass(testKey))

    def test_bad_key(self):
        keygen = LynxGen()
        testKey = 'LYNXlynxLYNXlynxLYNXlynxlynx'
        self.assertFalse(keygen.check_pass(testKey))
        testKey = 'LYNXlynxLYNXlynxLYnxLYNXlynxLYNXlynxLYnxLYNXlynxLYNXlynxLYnx'
        self.assertFalse(keygen.check_pass(testKey))
        testKey = 'LYNXlynxLYnx'
        self.assertFalse(keygen.check_pass(testKey))
        testKey = 'lynxLYNXLYNXlynxLYnx'
        self.assertFalse(keygen.check_pass(testKey))

    def test_random_key(self):
        keygen = LynxGen()
        random_key = keygen.get_random_key()
        print "Valid Key: %s" % random_key
        self.assertTrue(keygen.check_pass(random_key))


if __name__ == '__main__':
    keygen = LynxGen()
    print "Tell nrr to %s" % keygen.get_random_key()