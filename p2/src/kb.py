from copy import *
import sys
import os

DEBUG = False
class Kb():
    """Class that represents a KB, it may receive a conjunction of disjuntions,
    so it receives a list of sets, every element must be a disjunction"""
    def __init__(self, sentences_list=None):
        self.sentences = sentences_list
        self.simplifyKB()

    def pl_resolution(self):
    #this function assumes that the list is a list of tupples every tupple defines a disjuntion
        self.new = []
        while True:
            self.sentences.sort(key=lambda x: len(x))
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
            if len(self.sentences) == 0:
                return False
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
                for sentence in self.sentences:
                    if Kb.negate_literal(literal) in sentence:
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
            for literal in sentence:
                if Kb.negate_literal(literal) in sentence: # tautologie
                    break
            else:
                if sentence not in result:
                    sub = [x.issubset(sentence) or x.issuperset(sentence) for x in result]
                    flag = True
                    for j in [i for i, x in enumerate(sub) if x]:
                        if len(sentence) < len(result[j]): # subset of
                            result.remove(result[j])
                            result.append(sentence)
                        flag = False
                    if flag:
                        result.append(sentence)
        self.sentences = result
        self.simplification_one()
        self.new = deepcopy(self.sentences)

    def _pl_resolve(self,x,y):
        #this function receives two lists that represent a disjuntion and returns
        #the new clauses that can be deducted by resolution with that pair
        resolvent = None
        for a in x:
            if Kb.negate_literal(a) in y:
                aux_x = deepcopy(x)
                aux_y = deepcopy(y)
                aux_x.remove(a)
                aux_y.remove(Kb.negate_literal(a))
                aux_x = aux_x.union(aux_y)
                resolvent = aux_x
                break # we only need to resolve one time

        if resolvent is not None:
            if not resolvent: #empty clause
                return True
            else:
                if resolvent not in self.new:
                    self.new.append(resolvent)
        return False
