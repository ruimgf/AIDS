
class GeneralSearch:
    """docstring forUniformedSearch."""
    def __init__(self,problem,queue):
        self.open_list = queue
        self.problem = problem
        self.open_list.put(problem.get_initial_state())

    def init_search(self):

        while not self.open_list.empty():
            node = self.open_list.get()
            #print("pop element:",node)
            if node.isa_goal_state():
                return node
            else:
                l = node.get_sucessors()
                for element in l:
                    self.open_list.put(element)

                #print("queue: ",self.open_list.queue)
        return None
