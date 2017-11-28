from copy import *
class Kb():
    """Class that represents a KB, it may receive a conjunction of disjuntions,
    so it receives a list of lists, every element must be a disjunction"""
    def __init__(self, sentences_list=None):
        self.sentences = sentences_list
        

    def pl_resolution(self):
    #this function assumes that the list is a list of tupples every tupple defines a disjuntion
        clauses = deepcopy(self.sentences)
        new = []
        while True:
            for i in range(len(clauses)):
                for j in range(i+1,len(clauses)):
                    x = clauses[i]
                    y = clauses[j]
                    print('------------------------')
                    print(x)
                    print(y)
                    resolvents = pl_resolve(x,y)#apply resolution to the 2 clauses
                    print(resolvents)
                    print('------------------------')
                    for z in resolvents:
                        if not(z):
                            return True
                        else:
                            if z not in new:
                                new.append(z)
            flag = False
            for element in new:
                if element not in clauses:
                    flag = True
                    break
            if flag:
                for i in new:
                    if i not in clauses:
                        clauses.append(i)

            else: # is a sub set
                return False
            print("clauses:" + str(clauses))

def negate_literal(literal):
    if type(literal) is str:
        return ('not',literal)
    else:
        return literal[1]

def pl_resolve(x,y):
    #this function receives two lists that represent a disjuntion and returns
    #the new clauses that can be deducted by resolution with that pair
    resolvents = []
    for a in x:
        if negate_literal(a) in y:
            aux_x = deepcopy(x)
            aux_y = deepcopy(y)
            aux_x.remove(a)
            aux_y.remove(negate_literal(a))
            aux_x = aux_x.union(aux_y)
            resolvents.append(aux_x)
    return resolvents
