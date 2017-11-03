
import itertools
from heapq import heappop, heappush,heapify
#import pulp

###############################################################################
class ourPriorityQueue():
    def __init__(self):
        self.queue = []  # list of entries arranged in a heap
    def put(self,task, priority=0):
        'Add a new task or update the priority of an existing task'
        entry = task
        heappush(self.queue, entry)

    def remove(self,task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        self.queue.remove(task)
        heapify(self.queue)

    def get(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.queue:
            task = heappop(self.queue)
            return task
        raise KeyError('pop from an empty priority queue')

    def empty(self):
        return len(self.queue) == 0

################################################################################
class Operation:
    def __init__(self, pieces,pay_load):
        """
        @param pieces: pieces of operator
        @param pay_load: weight of operator
        """
        self.pieces = pieces
        self.pay_load = pay_load

    def __repr__(self):
        return str(self.pieces)

################################################################################
class Problem:
    def __init__(self, g, heuristic=None):
        """
        This class represents the assembly problem
        @param g: graph of problem
        @param heuristic: heuristic to use
        """
        self.in_graph = g
        self.launches = g.info['launches']
        self.operations = []

        allIds = self.in_graph.nodes.keys()
        self.max_pay_load = max(self.launches,key = lambda x: x.max_payload).max_payload
        self.heuristic = heuristic

        for i in range(1, len(self.in_graph) + 1):
            combinations = itertools.combinations(allIds, i)
            for combination in combinations:
                total_weight = sum([g.nodes[x].info['weight'] for x in combination])
                if total_weight <= self.max_pay_load:
                    self.operations.append(Operation(combination, total_weight))

    def get_initial_state(self):
        """
        @return: initial state
        """
        return OurState(self, [ () for x in range(len(self.launches))])

    def get_valid_operations(self, pieces_on_air, max_payload):

        left_pieces = set(self.in_graph.nodes.keys()) - pieces_on_air
        ops = []
        for i in range(1, len(left_pieces) + 1):
            combinations = itertools.combinations(left_pieces, i)
            for combination in combinations:
                total_weight = sum([self.in_graph.nodes[x].info['weight'] for x in combination])
                if total_weight <= max_payload and self.in_graph.connected_subset(list(combination) + list(pieces_on_air)):
                    ops.append(Operation(combination, total_weight))
        return ops

    def g(self, state):
        """
        @param state: state
        @return: path cost
        """
        return sum(state.cost_launch)

    def __repr__(self):
        return str(self.operations)

def heur_best_from_now(state):
    """
    This heuristics computes the cost based in put all weight in the launch with the lowest variable cost.
    @param state: state to compute the cost.
    @return: cost
    """
    try:
        return min([launch.compute_variable_cost(state.left_weight()) for launch in state.launches[state.launch_nr:]])
    except ValueError:
        return 0
"""
def heur_optimal(state):
    
    #This heuristic solves a linear problem to estimate the left cost.
    #@param state:
    #@return:
    
    lauches = state.launches[state.launch_nr:]
    P = state.left_weight()
    max = [l.max_payload for l in lauches]
    cf = [l.fixed_cost for l in lauches]
    cv = [l.variable_cost for l in lauches]

    p = []
    y = []
    prob = pulp.LpProblem("", pulp.LpMinimize)
    for i in range(len(cf)):
        k = pulp.LpVariable('p' + str(i), lowBound=0, cat='Continuous')
        p.append(k)

    for i in range(len(cf)):
        k = pulp.LpVariable('y' + str(i), cat='Binary')
        y.append(k)

    l = 0
    for i in range(len(cf)):
        l += y[i] * cf[i] + cv[i] * p[i]

    prob += l

    f = 0

    for i in range(len(cf)):
        f += p[i]
    prob += f == P

    for i in range(len(cf)):
        prob += p[i] <= max[i] * y[i]
    prob.solve()
    value = pulp.value(prob.objective)
    prob = None
    if value is not None:
        return value
    else:
        return 0

"""


class OurState:

    def __init__(self, problem,pieces_list,launch_nr=0,cost_launch=None):
        """
        This class represents one state of our problem
        @param problem: Problem to solve
        @param pieces_list: List of pieces on air
        @param launch_nr: actual launch number
        @param cost_launch: actual costs per launch
        """
        self.problem = problem
        self.launches = list(self.problem.in_graph.info['launches'])
        self.launch_nr = launch_nr
        self.pieces_list = pieces_list

        self.pieces_on_air = []
        for pieces in self.pieces_list:
            self.pieces_on_air += pieces

        self.pieces_on_air = set(self.pieces_on_air)

        if cost_launch is None:
            self.cost_launch = [0 for x in range(len(self.launches))]
        else:
            self.cost_launch = cost_launch

        if self.problem.heuristic is None:
            self.cost = self.problem.g(self)
        else:
            self.cost = self.problem.g(self) + self.problem.heuristic(self)

    def __repr__(self):
        s = ""
        total_cost = 0
        i=0
        for launch in self.launches:
            if len(self.pieces_list[i]) != 0:
                s += launch.get_str(self.pieces_list[i],self.cost_launch[i])
                s += "\n"
                total_cost += self.cost_launch[i]
            i += 1
        s += "%.6f" % total_cost
        return s


    def isa_goal_state(self):
        """
        @return: True if it is a goal state, false otherwise.
        """
        nr_pieces_on_air = len(self.pieces_on_air)

        if len(self.problem.in_graph) == nr_pieces_on_air:
            return True
        else:
            return False

    def left_weight(self):
        """
        @return: sum of weight of pieces that not sent
        """
        left_pieces = set(self.problem.in_graph.nodes.keys()) - set(self.pieces_on_air)
        return sum([self.problem.in_graph.nodes[piece_id].info['weight'] for piece_id in left_pieces])

    def __lt__(self, other):
        try:
            return self.cost < other.cost

        except AttributeError:
            return NotImplemented

    def __eq__(self, other):
        if self.launch_nr != other.launch_nr:
            return False
        if len(self.pieces_on_air) != len(other.pieces_on_air):
            return False

        if self.pieces_on_air == other.pieces_on_air:
            return True
        return False

    def total_left_capacity(self):
        """
        @return: Total capacity of left lauches.
        """
        return sum([l.max_payload for l in self.launches[self.launch_nr:]])

    def get_sucessors(self):
        """
        @return: Valid sucessores of one node.
        """
        if self.launch_nr >= len(self.launches): # no more launches
            return []

        if self.total_left_capacity() < self.left_weight(): # no capacity for all left weight
            return []

        ops = self.problem.get_valid_operations(self.pieces_on_air, self.launches[self.launch_nr].max_payload)

        succ = []
        # send any piece operation
        if self.launch_nr + 1 < len(self.launches):
            costs = self.cost_launch.copy()
            costs[self.launch_nr] = 0
            lcopy = self.pieces_list.copy()
            s = OurState(self.problem, lcopy, self.launch_nr + 1, costs)
            succ.append(s)

        # get valid pieces combinations
        for op in ops:
            lcopy= self.pieces_list.copy()
            lcopy[self.launch_nr] = op.pieces
            costs = self.cost_launch.copy()
            costs[self.launch_nr] = self.launches[self.launch_nr].compute_cost(op.pay_load)
            s = OurState(self.problem,lcopy, self.launch_nr + 1,costs)
            succ.append(s)

        return succ


class Launch:
    def __init__(self, date, max_payload, fixed_cost, variable_cost):
        """
        Class that represents a Launch
        @param date: date of launch
        @param max_payload: max_payload
        @param fixed_cost: fixed_cost of launch
        @param variable_cost: variable cost of launch
        """
        self.date = date #date of the launch
        self.max_payload = float(max_payload)
        self.fixed_cost = float(fixed_cost)
        self.variable_cost = float(variable_cost)

    def __repr__(self):
        return "%s,%s,%s,%s" % (self.date, self.max_payload, self.fixed_cost, self.variable_cost)

    def get_str(self, pieces, cost):
        s = ""
        s += self.date.strftime('%d%m%Y') + "  "
        for piece in pieces:
            s = s + " " + piece
        return s + "  " + "%.6f" % cost

    def compute_variable_cost(self,total_weight):
        """
         @param total_weight: weight in the launch
         @return: variable cost
        """
        if total_weight != 0:
            return self.variable_cost * total_weight
        else:
            return 0

    def compute_cost(self,total_weight):
        """
        @param total_weight: weight in the launch
        @return: total cost
        """
        if total_weight != 0:
            return self.fixed_cost + self.variable_cost * total_weight
        else:
            return 0
