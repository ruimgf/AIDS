
class GeralSearch:
    """docstring forUniformedSearch."""
    def __init__(self,problem,strategy):
        self.open_list = strategy.open_list
        self.problem = problem
        self.open_list.put(problem.initialState())
    def init_search(self):
        while not self.open_list.empty():
            node = self.open_list.get()
            if node.isa_goal_state():
                return node
            else:
                l = node.get_sucessors()
                self.open_list.put(l)
        return None
