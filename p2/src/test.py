import unittest
import convert
import prove

class TestSolver(unittest.TestCase):

    def prove(self,testname,solution):
        testfile_path = "../testFiles/" + testname + ".txt"

        output = prove.main(convert.main(testfile_path).sentences)
        self.assertEqual(solution, output)

    def test_trival(self):
        self.prove("trivial",True)

    def test_p1(self):
        self.prove("p1",False)

    def test_p2(self):
        self.prove("p2",False)

    def test_p3(self):
        self.prove("p3",False)

    def test_p4(self):
        self.prove("p4",True)

if __name__ == '__main__':
     unittest.main(verbosity=3)
