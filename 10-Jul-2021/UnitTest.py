import unittest
from unittest.main import main

class Testing(unittest.TestCase):
    def test_string(self):
        string = 'hello'
        self.assertEqual(string,'hello')


    def test_upper(self):
        self.assertEqual("hai".upper(),"HAI")
        self.assertEqual("HAI".lower(),"hai")

    def test_strip(self):
        word = "abcdPythondcba"
        self.assertEqual(word.strip("abcd"),"Python")

    def test_average(self):
        ls = [1,2,3,4,5]
        total = sum(ls)
        avg = total/len(ls)
        self.assertEqual(total,15)
        self.assertEqual(avg,3.0)

if __name__=='__main__' :
    unittest.main()