from node import Node
import copy
import itertools
import sys

class Operation:
    def __init__(self, pieces):
        self.pieces = pieces
        self.pay_load = sum([piece.weight for piece in self.pieces])

    def __repr__(self):
        return str(self.pieces)

    def get_pieces_ids(self):
        return [p.piece_id for p in self.pieces]


class Problem:
    def __init__(self, g):

        self.in_graph = g
        launches = g.info['launches']
        self.operations = []
        allIds = self.in_graph.nodes.keys()
        for i in range(1, len(self.in_graph) + 1):
            combinations = itertools.combinations(allIds, i)
            for combination in combinations:
                pieces = []
                for piece_id in list(combination):
                    pieces.append(self.in_graph.nodes[piece_id].info['piece'])
                self.operations.append(Operation(pieces))

        max_pay_load = max([launch.max_payload for launch in launches])

        self.operations = [x for x in self.operations if x.pay_load <= max_pay_load]

    def get_initial_state(self):
        return OurState(self, copy.deepcopy(self.in_graph.info['launches']))


    def get_valid_operations(self, pieces_on_air, max_payload):

        ops = [x for x in self.operations if x.pay_load <= max_payload]
        op_clean = []

        for op in ops:
            op_piecesId = [p.piece_id for p in op.pieces]
            x = [p for p in pieces_on_air if p in op_piecesId]
            if len(x)==0:
                if self.in_graph.connected_subset(op.get_pieces_ids() + pieces_on_air):
                    op_clean.append(op)

        return op_clean

    def __repr__(self):
        return str(self.operations)


class OurState:
    def __init__(self, problem, launches=None, launch_nr=0):
        self.problem = problem
        if launches is None:
            self.launches = list(self.g.info['launches'])  # list
        else:
            self.launches = launches
        self.launch_nr = launch_nr
        self.cost = sum([launch.compute_cost() for launch in self.launches])

    def __repr__(self):
        s = ""
        total_cost = 0
        for launch in self.launches:
            if len(launch.pieces) != 0:
                s += str(launch)
                s += "\n"
                total_cost += launch.compute_cost()
        s += str(total_cost)
        return s
        #return str(self.launches)

    def isa_goal_state(self):
        nr_pieces_on_air = len(self.pieces_on_air())

        if len(self.problem.in_graph) == nr_pieces_on_air:
            print(self)
            sys.exit(0)
            return True
        else:
            return False

    def left_weight(self):
        pieces_on_air = self.pieces_on_air()
        leftpieces = [self.problem.in_graph.nodes[piece_id].info['piece'] for piece_id in list(self.problem.in_graph.nodes.keys()) if piece_id not in pieces_on_air]
        return sum([p.weight for p in leftpieces])

    def __lt__(self, other):

        try:
            return self.cost < other.cost

        except AttributeError:
            return NotImplemented

    def pieces_on_air(self):
        pieces_on_air = []
        for launch in self.launches:
            pieces_on_air += [piece.piece_id for piece in launch.pieces]
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
            sendLauches = copy.deepcopy(self.launches)
            s = OurState(self.problem, sendLauches, self.launch_nr + 1)
            succ.append(s)

        for op in ops:
            sendLauches = copy.deepcopy(self.launches)

            for piece in op.pieces:
                sendLauches[self.launch_nr].insert_piece(piece)
            #if self.launch_nr + 1 < len(self.launches):
            s = OurState(self.problem, sendLauches, self.launch_nr + 1)
            succ.append(s)

        return succ


class Launch():
    def __init__(self, date, max_payload, fixed_cost, variable_cost):
        self.date = date
        self.max_payload = float(max_payload)
        self.fixed_cost = float(fixed_cost)
        self.variable_cost = float(variable_cost)
        self.pieces = []

    def __repr__(self):
        return "%s,%s,%s,%s" % (self.date, self.max_payload, self.fixed_cost, self.variable_cost)
        #return str(self.pieces)

    def __str__(self):
        s = ""
        s += str(self.date)
        for piece in self.pieces:
            s = s + " " + piece.piece_id
        return s + " " + str(self.compute_cost())
        #return str(self.pieces)

    def compute_cost(self):
        total_weight = sum([piece.weight for piece in self.pieces])
        if total_weight !=0:
            return self.fixed_cost + self.variable_cost * total_weight
        else:
            return 0

    def can_insert(self, weight):
        total_weight = self.total_weight()
        return (self.max_payload - total_weight) >= weight

    def total_weight(self):
        return sum([piece.weight for piece in self.pieces])

    def insert_piece(self, piece):  # return True if sucess
        total_weight = sum([p.weight for p in self.pieces])
        if total_weight + piece.weight <= self.max_payload:
            self.pieces.append(piece)
            return True
        else:
            print("error inserted")
            return False
