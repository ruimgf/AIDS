import unittest
from solver import main

class TestSolver(unittest.TestCase):

    def t(self,testname,type):
        output = str(main([1, type, "../testFiles/"+testname+".txt"]))
        cost = float(output.split("\n")[-1])
        with open("../testFiles/"+testname+".out", 'r')  as f:
            expected = f.readlines()
            expected_cost = float(expected[-1])
        self.assertEqual(cost, expected_cost)

    def test_uniformed_simple1(self):
        "simple1.txt [uniformedSearch]"
        self.t("simple1","-u")

    def test_uniformed_trivial1(self):
        "trivial1.txt [uniformedSearch]"
        self.t("trivial1","-u")

    def test_uniformed_trivial2(self):
        "trivial2.txt [uniformedSearch]"
        self.t("trivial2","-u")

    #@unittest.skip("skipping mir")
    def test_uniformed_mir(self):
        "mir.txt [uniformedSearch]"
        self.t("mir","-u")

    def test_informed_simple1(self):
        "simple1.txt [informedSearch]"
        self.t("simple1","-i")

    def test_informed_trivial1(self):
        "trivial1.txt [informedSearch]"
        self.t("trivial1","-i")

    def test_informed_trivial2(self):
        "trivial2.txt [informedSearch]"
        self.t("trivial2","-i")

    #@unittest.skip("skipping mir")
    def test_informed_mir(self):
        "mir.txt [informedSearch]"
        self.t("mir","-i")

    def test_uniformed_t0(self):
        "t0.txt [uniformedSearch]"
        self.t("t0","-u")

    def test_uniformed_t1(self):
        "t1.txt [uniformedSearch]"
        self.t("t1","-u")

    def test_uniformed_t2(self):
        "t2.txt [uniformedSearch]"
        self.t("t2","-u")

    def test_uniformed_t3(self):
        "t3.txt [uniformedSearch]"
        self.t("t3","-u")

    def test_uniformed_t4(self):
        "t4.txt [uniformedSearch]"
        self.t("t4","-u")

    def test_uniformed_t5(self):
        "t5.txt [uniformedSearch]"
        self.t("t5","-u")


if __name__ == '__main__':

     unittest.main(verbosity=3)