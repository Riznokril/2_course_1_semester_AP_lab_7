import unittest
from kmp import KMP

class TestKMP(unittest.TestCase):

    def test_kmp_1(self):
        test_kmp = KMP("assabdasasdjk_*asn2324dwbeudhsmnxz@sndw 1213asasd", "asas")
        self.assertEqual(test_kmp.kmp(), [6, 44])

    def test_kmp_2(self):
        test_kmp = KMP("kjaecsn;iadsck;kaes", "sdfsdfe")
        self.assertEqual(test_kmp.kmp(), [])

    def test_kmp_3(self):
        test_kmp = KMP("nkldtrhdsfbjnsgtldsgf3#@%$^24rew4@!#kn", "^24")
        self.assertEqual(test_kmp.kmp(), [26])

    def test_find_sufix_massive_1(self):
        test_kmp = KMP("test", "teta")
        self.assertEqual(test_kmp.find_sufix_massive(), [0, 0, 1, 0])

    def test_find_sufix_massive_2(self):
        test_kmp = KMP("test", "terteter")
        self.assertEqual(test_kmp.find_sufix_massive(), [0, 0, 0, 1, 2, 1, 2, 3])

    def test_find_sufix_massive_3(self):
        test_kmp = KMP("test", "t")
        self.assertEqual(test_kmp.find_sufix_massive(), [0])

if __name__ == '__main__':
    unittest.main()