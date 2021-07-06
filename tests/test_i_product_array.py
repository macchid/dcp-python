import unittest, random
from pkg.i_product_array import prod_array

class Params:
    def __init__(self, input, output):
        self.input = input
        self.output = output


class TestProductArray(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        random.seed(49)
        return super().setUpClass()


    def setUp(self):
        self.testCases = {
            'Definition Sample' : Params([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
            'Empty list' : Params([], []),
            'Other Example' : Params([3,2,1], [2,3,6]),
        }


    def test_multiple(self):
        for desc, params in self.testCases.items():
            with self.subTest(desc=desc):
                self.assertEqual(prod_array(params.input), params.output) 

if __name__ == '__main__':
    unittest.main()