import unittest, random
from k_sum_in_list.k_sum_in_list import k_sum_in_list

class Params:
    def __init__(self, k, l, res):
        self.k = k
        self.l = l
        self.res = res


class TestKSumInList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        random.seed(49)
        return super().setUpClass()


    def setUp(self):
        self.testCases = {
            'Definition Sample' : Params(17, [10, 15, 3, 7], True),
            'Simple not exists' : Params(17, [10, 15, 3, 8], False),
            'Empty list' : Params(17, [], False),
            'Zero' : Params(0, [10, 25, 4, 12], False),
            'Large Number Exists' : Params(9999999999, [10, 9876543210, 3, 123456789], True),
            'Large list' : Params(17, [9] + [random.randint(0,8)]*100000 + [8], True),
            'Worst Case' : Params(9999999999, [10, 9876543210] + [random.randint(0,1000000)]*100000 + [123456789], True),
        }


    def test_multiple(self):
        for desc, params in self.testCases.items():
            with self.subTest(desc=desc):
                self.assertEqual(k_sum_in_list(params.k, params.l), params.res) 

if __name__ == '__main__':
    unittest.main()