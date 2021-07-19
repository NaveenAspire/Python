import unittest
#from ..methods_unittest import mulIns

class Test_Mul(unittest.TestCase):

    def mulInstance(self,a,b):
        ans = int(a*b)
        return ans

    @staticmethod
    def mulStatic(a,b):
        ans = int(a*b)
        return ans

    def test_methods(self):
        mulIns  = self.mulInstance(10,2)
        mulSta = self.mulStatic(10,2)
        self.assertEqual(mulIns,20)
        self.assertEqual(mulSta,20)


if __name__ == "__main__":
    unittest.main()