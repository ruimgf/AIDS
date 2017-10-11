class Node():
    def __init__(self, id_, **kwargs):
        self.id_ = id_
        self.neigh = []
        self.info = {}
        for name, value in kwargs.items():
            self.info[name] = value
    def __str__(self):
        pass
    def __eq__(self, other):
        pass
