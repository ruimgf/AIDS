from node import Node
import copy
import itertools

class Operation:
    def __init__(self,pieces):
        self.pieces = pieces
        self.pay_load = sum([piece.weight for piece in self.pieces])

    def __repr__(self):
        return str(self.pieces)

class Problem:

    def __init__(self,g):

       self.in_graph = g
       launches = g.info['launches']
       self.operations = []
       allIds = self.in_graph.nodes.keys()
       for i in range(1,len(self.in_graph)+1):
           combinations = list(itertools.combinations(allIds,i))
           for combination in combinations:
               pieces = []
               for piece_id in list(combination):
                   pieces.append(self.in_graph.nodes[piece_id].info['piece'])
               self.operations.append(Operation(pieces))

               
       max_pay_load = max([launch.max_payload for launch in launches])
       #filtered operations
       self.operations = [x for x in self.operations if x.pay_load <= max_pay_load]
       print("len = =",len(self.operations))
    def __repr__(self):
        return str(self.operations)

class OurState:
    def __init__(self, g, launches=None, launch_nr=0):
        self.g = g
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
            if len(launch.pieces) != 0 :
                s += str(launch)
                s += "\n"
                total_cost += launch.compute_cost()
        s += str(total_cost)
        return s

    def isa_goal_state(self):
        nr_pieces_on_air = sum([len(launch.pieces) for launch in self.launches])
        if len(self.g) == nr_pieces_on_air:
            print(self)
            exit(0)
            return True
        else:
            return False

    def __lt__(self, other):

        try:
            return self.cost < other.cost

        except AttributeError:
            return NotImplemented

    def get_sucessors(self):
        pieces_on_air = []
        #substituir por grafo de peças no ar
        for launch in self.launches:
            pieces_on_air += [piece.piece_id for piece in launch.pieces]

        leftpieces = [piece for piece in list(self.g.nodes.keys()) if piece not in pieces_on_air]

        #ir buscar as operações válidas

        #esta vai ser sempre possivel
        succ = []
        if self.launch_nr + 1 < len(self.launches):
            sendLauches = copy.deepcopy(self.launches)
            s = OurState(self.g, sendLauches, self.launch_nr + 1)
            succ.append(s)

        #gerar os nós com base nas operações válidas


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

    def __str__(self):
        s = ""
        s += str(self.date)
        for piece in self.pieces:
            s = s + " " + piece.piece_id
        return s + " " + str(self.compute_cost())

    def compute_cost(self):
        total_weight = sum([piece.weight for piece in self.pieces])
        return self.fixed_cost + self.variable_cost * total_weight

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
            return False
