from queue import *
from copy import *

class TreeNode():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        pass

class Tree():
    def __init__(self,root=None):
        self.root = root
        self.spaces = [60,40,40,30,20,20,20,25,10,10,10,10,10,10,10,10]
    def represent(self):
        l = Queue()
        l.put(self.root)
        i = 1
        n = 0
        p = 0
        while not l.empty():
            e = l.get()
            #print("i=" + str(i))
            #print("2^n = " + str(2**n))
            if(i == 2**(n+1)):
               #print(n*" " + "╚╗")
               n += 1
               p = 5
               print(1 * "\n")
               if n == 4:
                   break

            if e is not None:
                print(self.spaces[i-1]*" ",end='')
                print(str(e.value),end='')
                l.put(e.left)
                l.put(e.right)
            else:
                print(self.spaces[i-1]*" ",end='')
                print("-1",end='')
            i += 1

        print("")
    def convertCNF(self):
        """
            convertCNF Runs a BFS that ensures that the result tree is a representation of a CNF
        """

        l = Queue()
        l.put(self.root)
        restart = False

        while not l.empty():
            e = l.get()
            if e.value == "or": # if we find an and before a or it isn't a CNF
                if e.left is not None and e.left.value == "and":
                    self.applyDist(e,e.left)
                    restart = True
                elif e.right is not None and e.right.value == "and":
                    self.applyDist(e,e.right)
                    restart = True
            if e.left is not None:
                l.put(e.left)
            if e.right is not None:
                l.put(e.right)

        if restart:
            self.convertCNF()

    def applyDist(self,ndOr,ndAnd):

        ndOr.value = "and" # or passa a and

        ndOrLeft = ndOr.left
        ndOrRight = ndOr.right

        if ndAnd is ndOr.left:
            ndOr.left = TreeNode("or",ndAnd.left,deepcopy(ndOrRight))
            ndOr.right = TreeNode("or",ndAnd.right,ndOrRight)
        else:
            ndOr.left = TreeNode("or",ndAnd.left,ndOrLeft)
            ndOr.right = TreeNode("or",ndAnd.right,ndOrLeft)
