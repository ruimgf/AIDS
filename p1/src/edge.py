class Edge():
    def __init__(self,nodeA,nodeB,**kwargs):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.info = {}
        for name, value in kwargs.items():
            self.info[name] = value

    def __str__(self):
        pass
    def __eq__(self, other):
        pass
