class GeneralSearch:
    """docstring forUniformedSearch."""

    def __init__(self,problem,queue):
        self.open_list = queue
        self.problem = problem
        self.open_list.put(problem.get_initial_state())
        self.closed_list = []
    def init_search(self):
        self.i = 0
        self.generatedNodes = 1
        while not self.open_list.empty():
            self.i += 1
            node = self.open_list.get()
            
            if node.isa_goal_state():
                print("we have " + str(self.i) +  " iterations")
                print("we have " + "a total of " + str(self.generatedNodes) + " generated nodes")
                return node
            else:
                l = node.get_sucessors()
                self.generatedNodes += len(l)
                for element in l:
                    try:
                        i = self.closed_list.index(element)
                        if self.closed_list[i].cost <= element.cost: #an equal node with the same cost was yet expanded
                            continue
                    except ValueError:
                        pass
                    try:
                        i = self.open_list.pq.index(element)
                        state = self.open_list.pq[i]
                        if state.cost > element.cost:
                            self.open_list.remove(state)
                            self.open_list.put(element)
                    except ValueError:
                        self.open_list.put(element)
        print("we have " + str(self.i) + " iterations")
        return "0"
