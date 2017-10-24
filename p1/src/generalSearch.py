class GeneralSearch:
    """docstring forUniformedSearch."""

    def __init__(self,problem,queue):
        self.open_list = queue
        self.problem = problem
        self.open_list.put(problem.get_initial_state())

    def init_search(self):

        while not self.open_list.empty():
            node = self.open_list.get()

            if node.isa_goal_state():
                return node
            else:
                l = node.get_sucessors()
                for element in l:
                    if element not in self.open_list.pq:
                        self.open_list.put(element,element.cost)
                    else:
                        for state in self.open_list.pq:
                            if state == element:
                                if state.cost > element.cost:
                                    self.open_list.remove(state)
                                    self.open_list.put(element,element.cost)
                                    break

        return "0"
