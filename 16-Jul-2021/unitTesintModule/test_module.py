import unittest
from methods import mulInstance,mulStatic


class Test_Mul(unittest.TestCase):

    
    def test_methods(self):
        mulIns  =mulInstance(10,2)
        
        self.assertEqual(mulIns,20)
        mulStatic(10,2)assertEqual(mulStatic(10,2),20)


if __name__ == "__main__":
    unittest.main()