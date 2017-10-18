import sys
class GeneralSearch:
    """docstring forUniformedSearch."""

    def __init__(self,problem,queue):
        self.open_list = queue
        self.problem = problem
        self.open_list.put(problem.get_initial_state())

    def init_search(self):
        i=0
        while not self.open_list.empty():
            node = self.open_list.get()
            i += 1
            if node.isa_goal_state():
                return node
            else:
                l = node.get_sucessors()
                for element in l:
                    self.open_list.put(element)
            
        return "0"
