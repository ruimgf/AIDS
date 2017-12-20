from copy import *
import sys

DEBUG = False
class Kb():
    """Class that represents a KB, it may receive a conjunction of disjuntions,
    so it receives a list of sets, every element must be a disjunction"""
    def __init__(self, sentences_list=None):
        self.sentences = sentences_list
        print(self.sentences)
        self.simplifyKB()
        print(self.sentences)
        #print(self.sentences)
        #for e in self.sentences:
        #    print(list(e))

    def pl_resolution(self):
    #this function assumes that the list is a list of tupples every tupple defines a disjuntion
        self.new = []
        while True:
            for i in range(len(self.sentences)):
                for j in range(i+1,len(self.sentences)):
                    x = self.sentences[i]
                    y = self.sentences[j]
                    if self._pl_resolve(x,y):#apply resolution to the 2 clauses
                        return True
            for element in self.new:
                if element not in self.sentences:
                    break
            else:
                return False

            for element in self.new:
                if element not in self.sentences:
                    self.sentences.append(element)
            self.simplifyKB()

            if DEBUG:
                print("clauses:" + str(clauses))

    @staticmethod
    def negate_literal(literal):
        if type(literal) is str:
            return ('not',literal)
        else:
            return literal[1]

    def simplification_one(self):
        for i in range(len(self.sentences)):
            for literal in self.sentences[i]:
                #print(literal)
                for sentence in self.sentences:
                    if Kb.negate_literal(literal) in sentence:
                        #print('break')
                        break
                else:
                    for sentence in self.sentences:
                        if literal in sentence:
                            self.sentences.remove(sentence)

                    self.simplification_one()
                    return

    def simplifyKB(self):
        #simplification 1 remove a clause if contains a literal that is not comp-
        #lementary with any other in the remaining clauses

        #Simplification	2 and 3:
        result = []
        for sentence in self.sentences:
            if sentence is not None:
                for literal in sentence:
                    if Kb.negate_literal(literal) in sentence:
                        break
                else:
                    if sentence not in result:
                        sub = [x.issubset(sentence) or x.issuperset(sentence) for x in result]
                        flag = True
                        for j in range(len(sub)):
                            if sub[j] is True:
                                if len(sentence) < len(result[j]): # subset of
                                    result.remove(result[j])
                                    result.append(sentence)
                                flag = False
                        if flag:
                            result.append(sentence)
            self.sentences = result

        self.simplification_one()
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
                return True
            else:
                if z not in self.new:
                    self.new.append(z)
        return False
