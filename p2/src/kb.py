from copy import *
import sys

DEBUG = False
class Kb():
    """Class that represents a KB, it may receive a conjunction of disjuntions,
    so it receives a list of lists, every element must be a disjunction"""
    def __init__(self, sentences_list=None):
        self.sentences = sentences_list


    def pl_resolution(self):
    #this function assumes that the list is a list of tupples every tupple defines a disjuntion
        clauses = deepcopy(self.sentences)
        self.new = []
        while True:
            for i in range(len(clauses)):
                for j in range(i+1,len(clauses)):
                    x = clauses[i]
                    y = clauses[j]
                    self._pl_resolve(x,y)#apply resolution to the 2 clauses

            for element in self.new:
                if element not in clauses:
                    break
            else:
                print('False')
                exit()

            for i in self.new:
                if i not in clauses:
                    sub = [x.issubset(i) or x.issuperset(i) for x in clauses]
                    flag = True
                    for j in range(len(sub)):
                        if sub[j]:
                            if len(i) < len(clauses[j]): # subset of
                                clauses.remove(clauses[j])
                                clauses.append(i)
                                flag = False
                    if flag:
                        clauses.append(i)


            if DEBUG:
                print("clauses:" + str(clauses))

    @staticmethod
    def negate_literal(literal):
        if type(literal) is str:
            return ('not',literal)
        else:
            return literal[1]

    def simplifyKB(self):
        pass


    def _pl_resolve(self,x,y):
        #this function receives two lists that represent a disjuntion and returns
        #the new clauses that can be deducted by resolution with that pair
        resolvents = []
        for a in x:
            if Kb.negate_literal(a) in y:
                aux_x = deepcopy(x)
                aux_y = deepcopy(y)
                aux_x.remove(a)
                aux_y.remove(Kb.negate_literal(a))
                aux_x = aux_x.union(aux_y)

                for element in aux_x:
                    if Kb.negate_literal(element) in aux_x:
                        break
                else:
                    resolvents.append(aux_x)

        for z in resolvents:

            if not z:
                print('True')
                sys.exit()
            else:
                if z not in self.new:
                    self.new.append(z)
