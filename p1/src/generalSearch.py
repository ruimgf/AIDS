
class GeneralSearch:
    """docstring forUniformedSearch."""
    def __init__(self,Queue):
        self.open_list = Queue
        #self.problem = problem
        #self.open_list.put(problem.initialState())

    def init_search(self):
        i = 0
        while not self.open_list.empty():
            i +=1
            node = self.open_list.get()
            if node.isa_goal_state():
                return node
            else:
                l = node.get_sucessors()

                for element in l:
                    self.open_list.put(element)
        return None
