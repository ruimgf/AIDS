import unittest
from solver import main

class TestSolver(unittest.TestCase):

    def t(self,testname):
        output = str(main([1, "-u", "../testFiles/"+testname+".txt"]))
        cost = float(output.split("\n")[-1])
        with open("../testFiles/"+testname+".out", 'r')  as f:
            expected = f.readlines()
            expected_cost = float(expected[-1])
        self.assertEqual(cost, expected_cost)

    def test_uniformed_simple1(self):
        "simple1.txt [uniformedSearch]"
        self.t("simple1")

    def test_uniformed_trivial1(self):
        "trivial1.txt [uniformedSearch]"
        self.t("trivial1")

    def test_uniformed_trivial2(self):
        "trivial2.txt [uniformedSearch]"
        self.t("trivial2")

    #@unittest.skip("skipping mir")
    def test_uniformed_mir(self):
        "mir.txt [uniformedSearch]"
        self.t("mir")


if __name__ == '__main__':
    unittest.main(verbosity=3)