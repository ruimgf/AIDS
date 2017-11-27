class Kb():
    """Class that represents a KB, it may receive a conjunction of disjuntions,
    so it receives a list of lists, every element must be a disjunction"""

    ""
    def __init__(self, sentences_list=none):
        self.sentences = set(sentences_list)

    #apply resolution in the KB, returns TRUE if it is OK, FALSE otherwise
    def pl_resolution(self):

        clauses = list(self.sentences);
        while True:
            new = []
            for x in clauses:
                for y in clauses:
                    if(x != y):
                        resolvents = pl_resolve(x,y)#apply resolution to the 2 clauses
                        for z in resolvents:
                            if z == None:#if we get an empty clause, ten i is true
                                return True
                        new.append(resolvents)
            if(set(new).issubset(set(clauses))):#check if the new clauses obtained by resolution
                return False
            clauses.append(new)
