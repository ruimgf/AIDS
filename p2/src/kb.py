class Kb():
    """Class that represents a KB, it may receive a conjunction of disjuntions,
    so it receives a list of lists, every element must be a disjunction"""
    ""
    def __init__(self, sentences_list=None):
        self.sentences = set(sentences_list)


    def pl_resolution(self):
    """
    this function assumes that the list is a list of tupples every tupple defines a disjuntion
    """
        clauses = list(self.sentences);
        while True:
            new = []
            for x in clauses:
                for y in clauses:
                    if(x != y):
                        resolvents = pl_resolve(x,y)#apply resolution to the 2 clauses
                        for z in resolvents:
                            if not(z):#if we get an empty clause, this means that the tupple is empty
                                return True
                            else:
                                new.append(z)
            if(set(new).issubset(set(clauses))):#check if the new clauses obtained by resolution
                return False
            clauses.append(new)

    def pl_resolve(x,y):
        """
         this function receives two tupples that represent a disjuntion and returns
         the new clauses that can be deducted by resolution with that pair
         """
         resolvents = []
         for a in x:
            if(isinstance(a,tupple)):#if it is a tupple is of type ('not',A) so check if A is in y
                if(a[1] in y):#this means that A is in Y so we can have a
                    aux_x = list(x)
                    aux_y = list(y)
                    aux_x.remove(a)
                    aux_y.remove(a[1])
                    aux_x = aux_x + aux_y
                    resolvents.append(tupple(aux_x))
            else:
                if(('not',a) in y):
                    aux_x = list(x)
                    aux_y = list(y)
                    aux_x.remove(a)
                    aux_y.remove(('not',a))
                    aux_x = aux_x + aux_y
                    resolvents.append(tupple(aux_x))
        return resolvents
