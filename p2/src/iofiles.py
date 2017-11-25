import sys
from tree import *

class SentencesReader():
    """
        Class to read sentences from stdin.
    """
    @staticmethod
    def readstdin():
        with sys.stdin as f : #open stdin as a file
            lines = f.readlines()
            sentences = []
            for line in lines: # convert each line to a python object
                line = line.rstrip()
                sentences.append(eval(line))
        return sentences

    @staticmethod
    def process_sentences(sentences):
        for s in sentences:
            t = Tree(SentencesReader.process_sentence(s))
            t.convertCNF()
            t.convertCNF()
            t.represent()
            land = []
            lor = []
            r = SentencesReader.get_disjunctions(t.root,land,lor,0)
            for e in land:
                print(e)

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
                        D = SentencesReader.process_sentence(('not',s[1][2])))
                        return TreeNode('and',C,D)
                    elif s[1][0] == '<=>':
                        # not(A <=> B)
                        # (A V B) ^ (not(B) V A)
                        # (C V D) ^ (E V F)
                        # G ^ H
                        C = SentencesReader.process_sentence(s[1][1])
                        D = SentencesReader.process_sentence(s[1][2])
                        E = SentencesReader.process_sentence(('not',s[1][1]))
                        F = SentencesReader.process_sentence(('not',s[1][2])

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
    def get_disjunctions(node,land,lor,findor):

        if node.value == 'and':
            lor = []
            SentencesReader.get_disjunctions(node.left,land,lor,findor)
            if lor:
                land.append(lor)
            lor = []
            SentencesReader.get_disjunctions(node.right,land,lor,findor)
            if lor:
                land.append(lor)

        elif node.value == 'or':
            SentencesReader.get_disjunctions(node.left,land,lor,1)
            SentencesReader.get_disjunctions(node.right,land,lor,1)
            return
        else:
            lor.append(node.value)
