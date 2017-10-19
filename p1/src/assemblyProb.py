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
    def __init__(self, g):

        self.in_graph = g
        self.launches = g.info['launches']
        self.operations = []
        allIds = self.in_graph.nodes.keys()

        for i in range(1, len(self.in_graph) + 1):
            combinations = itertools.combinations(allIds, i)
            for combination in combinations:
                total_weight = sum([g.nodes[x].info['weight'] for x in list(combination)])
                self.operations.append(Operation(list(combination), total_weight))

        max_pay_load = max([launch.max_payload for launch in self.launches])

        self.operations = [x for x in self.operations if x.pay_load <= max_pay_load]

    def get_initial_state(self):
        return OurState(self,[[] for x in range(len(self.launches))])

    def get_valid_operations(self, pieces_on_air, max_payload):
        ops = [x for x in self.operations if x.pay_load <= max_payload]
        op_clean = []

        for op in ops:
            op_pieces_id = op.pieces
            x = [p for p in pieces_on_air if p in op_pieces_id]
            if len(x) == 0:
                if self.in_graph.connected_subset(op.pieces + pieces_on_air):
                    op_clean.append(op)

        return op_clean

    def __repr__(self):
        return str(self.operations)


class OurState:

    def __init__(self, problem,pieces_list,launch_nr=0):
        self.problem = problem
        self.launches = list(self.problem.in_graph.info['launches'])
        self.launch_nr = launch_nr
        self.pieces_list = [[] for x in range(len(self.launches))]
        self.cost_launch = [0 for x in range(len(self.launches))]
        for i in range(len(pieces_list)):
            self.pieces_list[i] += pieces_list[i]
            self.cost_launch[i] = self.launches[i].compute_cost(sum(self.problem.in_graph.nodes[x].info['weight'] for x in self.pieces_list[i]))
        self.cost = sum(self.cost_launch)

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
        nr_pieces_on_air = len(self.pieces_on_air())

        if len(self.problem.in_graph) == nr_pieces_on_air:
            return True
        else:
            return False

    def left_weight(self):
        pieces_on_air = self.pieces_on_air()
        left_pieces = [piece_id for piece_id in list(self.problem.in_graph.nodes.keys()) if piece_id not in pieces_on_air]
        return sum([self.problem.in_graph.nodes[piece_id].info['weight'] for piece_id in left_pieces])

    def __lt__(self, other):

        try:
            return self.cost < other.cost

        except AttributeError:
            return NotImplemented

    def pieces_on_air(self):
        pieces_on_air = []
        for pieces in self.pieces_list:
            pieces_on_air += pieces
        return pieces_on_air

    def total_left_capacity(self):
        return sum([l.max_payload for l in self.launches[self.launch_nr:]])

    def get_sucessors(self):

        if self.launch_nr >= len(self.launches):
            return []

        if self.total_left_capacity() < self.left_weight():
            return []

        ops = self.problem.get_valid_operations(self.pieces_on_air(),self.launches[self.launch_nr].max_payload)

        succ = []
        if self.launch_nr + 1 < len(self.launches):
            s = OurState(self.problem, self.pieces_list, self.launch_nr + 1)
            succ.append(s)

        for op in ops:
            lcopy = [[] for x in range(len(self.pieces_list))]

            for i in range(len(lcopy)):
                lcopy[i] += self.pieces_list[i].copy()

            lcopy[self.launch_nr] += op.pieces
            s = OurState(self.problem,lcopy, self.launch_nr + 1)
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
        s += str(self.date) + "  "
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
