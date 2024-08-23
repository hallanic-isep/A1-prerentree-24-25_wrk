import unittest

import juste_prix

class Tests(unittest.TestCase):

    def test_verifie_OK(self):
        self.assertEqual(juste_prix.verifie(5,5), True)

    def test_verifie_PB(self):
        self.assertEqual(juste_prix.verifie(5,3), False)
