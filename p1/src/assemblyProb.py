from node import Node
import itertools
import sys


class Operation:
    def __init__(self, pieces,pay_load):
        self.pieces = pieces
        self.pay_load = pay_load

    def __repr__(self):
        return str(self.pieces)


class Problem:
    def __init__(self, g, heuristic=None):

        self.in_graph = g
        self.launches = g.info['launches']
        self.operations = []
        allIds = self.in_graph.nodes.keys()
        self.max_pay_load = max([launch.max_payload for launch in self.launches])
        self.heuristic = heuristic

        for i in range(1, len(self.in_graph) + 1):
            combinations = itertools.combinations(allIds, i)
            for combination in combinations:
                total_weight = sum([g.nodes[x].info['weight'] for x in list(combination)])
                if total_weight <= self.max_pay_load:
                    self.operations.append(Operation(list(combination), total_weight))

    def get_initial_state(self):
        return OurState(self, [[] for x in range(len(self.launches))])

    def get_valid_operations(self, pieces_on_air, max_payload):
        left_pieces = [x for x in self.in_graph.nodes.keys() if x not in pieces_on_air]
        ops = []
        for i in range(1, len(left_pieces) + 1):
            combinations = itertools.combinations(left_pieces, i)
            for combination in combinations:
                total_weight = sum([self.in_graph.nodes[x].info['weight'] for x in list(combination)])
                if total_weight <= max_payload and self.in_graph.connected_subset(list(combination) + pieces_on_air):
                    ops.append(Operation(list(combination), total_weight))

        return ops

    def __repr__(self):
        return str(self.operations)


def g(state):
    return sum(state.cost_launch)


def heur_cost_per_kg(state):
    total_cost = sum(state.cost_launch)
    total_weight = sum([state.problem.in_graph.nodes[key].info['weight'] for key in state.pieces_on_air()])
    total_weight = total_weight + 0.0000000001

    return total_cost/total_weight * state.left_weight()

def heur_left_weight(state):
    return state.left_weight()

class OurState:

    def __init__(self, problem,pieces_list,launch_nr=0,cost_launch=None):
        self.problem = problem
        self.launches = list(self.problem.in_graph.info['launches'])
        self.launch_nr = launch_nr
        self.pieces_list = pieces_list
        self.pieces_on_air = []
        for pieces in self.pieces_list:
            self.pieces_on_air += pieces

        if cost_launch is None:
            self.cost_launch = [0 for x in range(len(self.launches))]
        else:
            self.cost_launch = cost_launch

        if self.problem.heuristic is None:
            self.cost = g(self)
        else:
            self.cost = g(self) + self.problem.heuristic(self)

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
        nr_pieces_on_air = len(self.pieces_on_air)

        if len(self.problem.in_graph) == nr_pieces_on_air:
            return True
        else:
            return False

    def left_weight(self):
        pieces_on_air = self.pieces_on_air
        left_pieces = [piece_id for piece_id in list(self.problem.in_graph.nodes.keys()) if piece_id not in pieces_on_air]
        return sum([self.problem.in_graph.nodes[piece_id].info['weight'] for piece_id in left_pieces])

    def __lt__(self, other):

        try:
            return self.cost < other.cost

        except AttributeError:
            return NotImplemented

    def __eq__(self,other):
        if self.launch_nr != other.launch_nr:
            return False
        if len(self.pieces_on_air) != len(other.pieces_on_air):
            return False
        intersect = set(self.pieces_on_air).intersection(set(other.pieces_on_air))
        if len(intersect) == len(other.pieces_on_air):
            return True
        return False

    def total_left_capacity(self):
        return sum([l.max_payload for l in self.launches[self.launch_nr:]])

    def get_sucessors(self):

        if self.launch_nr >= len(self.launches):
            return []

        if self.total_left_capacity() < self.left_weight():
            return []

        ops = self.problem.get_valid_operations(self.pieces_on_air, self.launches[self.launch_nr].max_payload)

        succ = []
        if self.launch_nr + 1 < len(self.launches):
            costs = self.cost_launch.copy()
            costs[self.launch_nr] = 0
            s = OurState(self.problem, self.pieces_list, self.launch_nr + 1,costs)
            succ.append(s)

        for op in ops:
            lcopy = [[] for x in range(len(self.pieces_list))]

            for i in range(len(lcopy)):
                lcopy[i] += self.pieces_list[i].copy()

            lcopy[self.launch_nr] += op.pieces
            costs = self.cost_launch.copy()
            costs[self.launch_nr] = self.launches[self.launch_nr].compute_cost(op.pay_load)
            s = OurState(self.problem,lcopy, self.launch_nr + 1,costs)
            succ.append(s)

        return succ


class Launch:
    def __init__(self, date, max_payload, fixed_cost, variable_cost):
        self.date = date
        self.max_payload = float(max_payload)
        self.fixed_cost = float(fixed_cost)
        self.variable_cost = float(variable_cost)

    def __repr__(self):
        return "%s,%s,%s,%s" % (self.date, self.max_payload, self.fixed_cost, self.variable_cost)

    def get_str(self, pieces, cost):
        s = ""
        s += self.date.strftime('%d%M%Y') + "  "
        for piece in pieces:
            s = s + " " + piece
        return s + "  " + "%.6f" % cost

    def compute_cost(self,total_weight):
        if total_weight != 0:
            return self.fixed_cost + self.variable_cost * total_weight
        else:
            return 0

    def total_weight(self,pieces):
        return sum([piece.weight for piece in pieces])
