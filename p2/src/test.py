import unittest
import convert
import prove

class TestSolver(unittest.TestCase):

    def test_prove(self,testname,solution):
        testfile_path = "../testFiles/" + testname + ".txt"
        output = prove.main((convert.main(testfile_path)).sentences)
        self.assertEqual(solution, output)

    def test_1_prove(self):
        "test1"
        self.test_prove("test1",True)



if __name__ == '__main__':
     unittest.main(verbosity=3)
