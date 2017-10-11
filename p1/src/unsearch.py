from ourgraph import OurGraph
from node import Node

class SearchState():
    self.launch = None
    self.pieces = []

    def __init__(self):
        pass
    
    def isa_goal_state(self):
        pass

    def applicable_actions(self,node):
        pass

    def apply_action(self,action):
        pass

class UniformedSearch():
    """docstring for UniformedSearch."""
    def __init__(self,structure_graph):
        #self.search_tree = OurGraph()
        self.fringe = [Node(1,actionsPreformed=[])]
        self.structure_graph = structure_graph

    def init_search(self):
        pass
