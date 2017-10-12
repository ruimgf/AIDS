from ourgraph import OurGraph
from node import Node

class OurState:

    def __init__(self,g,launches=None,launch_nr=0):
        self.g = g
        if launches is None:
            self.launches = list(self.g.info['launches']) #list
        else:
            self.launches = launches
        self.launch_nr = launch_nr
        self.launches[0].insert_piece(Piece("VCM",10))
        self.launches[0].insert_piece(Piece("VK", 10))

    def isa_goal_state(self):
        nr_pieces_on_air = sum([len(launch.pieces) for launch in self.launches])
        if len(self.g) == nr_pieces_on_air:
            return True
        else:
            return False

    def get_sucessors(self):
        pieces_on_air = []
        print(self.launches[0].pieces)
        for launch in self.launches:
            pieces_on_air += [piece.piece_id for piece in launch.pieces]

        leftpieces = [piece for piece in list(self.g.nodes.keys()) if piece not in pieces_on_air]
        if len(pieces_on_air)==0:
            print("no pieces on air")
            print(leftpieces)
        else:
            air_neigh = []
            for piece in pieces_on_air:
                air_neigh += [p.id_ for p in self.g.nodes[piece].neigh]
            valid_pieces = [p for p in leftpieces if p in list(air_neigh)]
            print(valid_pieces)

    def __cmp__(self, other):
        #if hasattr(other, 'number'):
        pass


class Piece():

    def __init__(self, piece_id,weight):
        self.weight = weight
        self.piece_id = piece_id

    def __eq__(self, other):

        if hasattr(other, 'piece_id'):
            if self.piece_id == other.piece_id:
                return True
        return False
class Launch():

    def __init__(self,date,max_payload,fixed_cost,variable_cost):
        self.date = date
        self.max_payload = float(max_payload)
        self.fixed_cost = float(fixed_cost)
        self.variable_cost = float(variable_cost)
        self.pieces = []

    def __repr__(self):
        return ("%s,%s,%s,%s"%(self.date,self.max_payload,self.fixed_cost,self.variable_cost))

    def compute_cost(self,pieces):
        total_weight = sum([piece.weight for piece in self.pieces])
        return (self.fixed_cost + self.variable_cost * total_weight)

    def insert_piece(self,piece): # return True if sucess
        total_weight = sum([p.weight for p in self.pieces])
        if total_weight + piece.weight < self.max_payload:
            self.pieces.append(piece)
           return True
        else:
            return False
