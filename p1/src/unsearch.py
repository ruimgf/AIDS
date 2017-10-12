from ourgraph import OurGraph
from node import Node

class SearchState:

    def __init__(self):
        self.launch = None
        self.pieces = []
        pass

    def isa_goal_state(self):
        pass

    def applicable_actions(self,node):
        pass

    def apply_action(self,action):
        pass

    def __cmp__(self, other):
        #if hasattr(other, 'number'):
        pass

class GeralSearch:
    """docstring for UniformedSearch."""
    def __init__(self,structure_graph,fringe):
        self.fringe = fringe
        self.structure_graph = structure_graph

    def init_search(self):
        pass
