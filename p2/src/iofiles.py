import sys
from tree import *

class SentencesReader():
    """
        Class to read sentences from stdin.
    """
    def __init__(self):
        with sys.stdin as f : #open stdin as a file
            lines = f.readlines()
            self.sentences = []
            for line in lines: # convert each line to a python object
                line = line.rstrip()
                self.sentences.append(eval(line))
            result = []
            for s in self.sentences: # convert to CNF form
                t = Tree(SentencesReader.process_sentence(s))
                t.convertCNF()
                #t.represent()
                result += SentencesReader.get_disjunctions(t.root)
            self.sentences = result

    def simplify(self):
        result = []
        for element in self.sentences:
            if element is not None:
                element = list(set(element)) # remove repeated
                l = element
                for e in element:
                    if SentencesReader.negate_literal(e) in element:
                        l = []
                        break
                add = True
                if l:
                    for e in result:
                        if set(l) == set(e):
                            add = False
                            break
                    if add:
                        result.append(l)
        self.sentences = result

    def print_sentences(self):
        for e in self.sentences:
            if len(e) == 1:
                if type(e[0]) is str:
                    print("\'" + e[0] +  "\'")
                else:
                    print(e[0])
            else:
                print(e)

    @staticmethod
    def negate_literal(literal):
        if type(literal) is str:
            return ('not',literal)
        else:
            return literal[1]

    @staticmethod
    def process_sentence(s):
        if type(s) is str:
            return TreeNode(s)
        elif type(s) is tuple:
            if s[0] == 'not':
                if type(s[1]) is str:
                    return TreeNode(s)
                elif type(s[1]) is tuple:
                    if s[1][0] == 'and':
                        # not(A ^ B)
                        # not(A) V not(B)
                        C = SentencesReader.process_sentence(('not',s[1][1]))
                        D = SentencesReader.process_sentence(('not',s[1][2]))
                        return TreeNode('or',C,D)
                    elif s[1][0] == 'or':
                        # not(A V B)
                        # not(A) ^ not(B)
                        C = SentencesReader.process_sentence(('not',s[1][1]))
                        D = SentencesReader.process_sentence(('not',s[1][2]))
                        return TreeNode('and',C,D)
                    elif s[1][0] == '=>':
                        # not(A => B)
                        # A ^ not(B)
                        C = SentencesReader.process_sentence(s[1][1])
                        D = SentencesReader.process_sentence(('not',s[1][2]))
                        return TreeNode('and',C,D)
                    elif s[1][0] == '<=>':
                        # not(A <=> B)
                        # (A V B) ^ (not(B) V A)
                        # (C V D) ^ (E V F)
                        # G ^ H
                        C = SentencesReader.process_sentence(s[1][1])
                        D = SentencesReader.process_sentence(s[1][2])
                        E = SentencesReader.process_sentence(('not',s[1][1]))
                        F = SentencesReader.process_sentence(('not',s[1][2]))

                        G = TreeNode('or',C,D)
                        H = TreeNode('or',E,F)
                        return TreeNode('and',G,H)
                    elif s[1][0] == 'not':
                        # (not(not(A))) == A
                        return SentencesReader.process_sentence(s[1][1])
            elif s[0] == 'and':
                A = SentencesReader.process_sentence(s[1])
                B = SentencesReader.process_sentence(s[2])
                return TreeNode(s[0],A,B)
            elif s[0] == 'or':
                A = SentencesReader.process_sentence(s[1])
                B = SentencesReader.process_sentence(s[2])
                return TreeNode(s[0],A,B)
            elif s[0] == '=>':
                # A => B == not(A) or B
                # C V D
                C = SentencesReader.process_sentence(('not',s[1]))
                D = SentencesReader.process_sentence(s[2])
                return TreeNode('or',C,D)
            elif s[0] == '<=>':
                # A <=> B == (not(A) V B) ^ (not(B) V A)
                # (C v D) ^ (E v F)
                # G ^ h
                C = SentencesReader.process_sentence(('not',s[1]))
                D = SentencesReader.process_sentence(s[2])
                E = SentencesReader.process_sentence(('not',s[2]))
                F = SentencesReader.process_sentence(s[1])
                G = TreeNode('or',C,D)
                H = TreeNode('or',E,F)
                return TreeNode('and',G,H)
            else:
                raise IOError
        else:
            raise IOError

    @staticmethod
    def get_disjunctions(node):
        land = []
        land.append(SentencesReader._get_disjunctions_rec(node,land))
        return land

    @staticmethod
    def _get_disjunctions_rec(node,land):

        if node.value == 'and':
            r = SentencesReader._get_disjunctions_rec(node.left,land)
            if r is not None:
                land.append(r)
            r = SentencesReader._get_disjunctions_rec(node.right,land)
            if r is not None:
                land.append(r)
            return None
        elif node.value == 'or':
            return SentencesReader._get_disjunctions_rec(node.left,land) + SentencesReader._get_disjunctions_rec(node.right,land)
        else:
            return [node.value]
