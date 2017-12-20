import unittest
import convert
import prove
import os
class TestSolver(unittest.TestCase):

    def prove(self,testname,solution):
        testfile_path = "../testFiles/" + testname

        output = prove.main(convert.main(testfile_path).sentences)
        self.assertEqual(solution, output)

    def test_trival(self):
        self.prove("trivial.txt",True)

    def test_p1(self):
        self.prove("p1.txt",False)

    def test_p2(self):
        self.prove("p2.txt",False)

    def test_p3(self):
        self.prove("p3.txt",False)

    def test_p4(self):
        self.prove("p4.txt",True)

    def test_fp1(self):
        self.prove("fp1.txt",True)
    def test_fp2(self):
        self.prove("fp2.txt",True)
    def test_fp3(self):
        self.prove("fp3.txt",True)
    def test_fp5(self):
        self.prove("fp5.txt",True)
    def test_fp6(self):
        self.prove("fp6.txt",True)
    def test_fp7(self):
        self.prove("fp7.txt",True)
    def test_fp8(self):
        self.prove("fp8.txt",True)
    def test_fp18(self):
        self.prove("fp18.txt",True)


    '''
    def test_uuf(self):
        l = os.listdir("../testFiles/uuf")
        for e in l:
            testfile_path = "../testFiles/uuf/" + e
            with open(testfile_path) as f:
                print(testfile_path)
                lines = f.readlines()
                sentences = []
                for line in lines: # convert each line to a python object
                    line = line.rstrip()
                    a = eval(line)
                    if isinstance(a,list):
                        sentences.append(set(a))
                    else:
                        b = set([a])
                        sentences.append(b)
                #print(sentences)
                output = prove.main(sentences)
                if output != True:
                    print("diferent")
                #self.assertEqual(True, output)
    '''
    '''
    def test_uuf(self):
        l = os.listdir("../testFiles/uf")
        for e in l:
            testfile_path = "../testFiles/uf/" + e
            with open(testfile_path) as f:
                print(testfile_path)
                lines = f.readlines()
                sentences = []
                for line in lines: # convert each line to a python object
                    line = line.rstrip()
                    a = eval(line)
                    if isinstance(a,list):
                        sentences.append(set(a))
                    else:
                        b = set([a])
                        sentences.append(b)
                #print(sentences)
                output = prove.main(sentences)
                #self.assertEqual(True, output)
    '''
if __name__ == '__main__':
     unittest.main(verbosity=3)
