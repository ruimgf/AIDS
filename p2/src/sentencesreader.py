import sys
from tree import *

class SentencesReader():
    """
        Class to read sentences from stdin.
    """
    def __init__(self,file=sys.stdin):
        self.t = None
        with file as f : #open stdin as a file
            lines = f.readlines()
            self.sentences = []
            for line in lines: # convert each line to a python object
                line = line.rstrip()
                self.sentences.append(eval(line))
            result = []
            for s in self.sentences: # convert to CNF form
                if self.t is None:
                    self.t = Tree(SentencesReader.process_sentence(s))
                else:
                    self.t.root = TreeNode('and',self.t.root,SentencesReader.process_sentence(s))

            self.t.convertCNF()
            #t.represent()
            r = SentencesReader.get_disjunctions(self.t.root)
            result += r
            self.sentences = result

    def simplify(self):
        result = []
        for element in self.sentences:
            if element is not None:
                element = list(set(element)) # remove repeated
                l = element
                for e in element:
                    if SentencesReader.negate_literal(e) in element:
                        break
                else:
                    for e in result:
                        if set(l) == set(e):
                            break
                    else:
                        if len(l) == 1:
                            result.append(l[0])
                        else:
                            result.append(l)
        self.sentences = result

    def print_sentences(self):
        for e in self.sentences:
            if type(e) is not list:
                if type(e) is str:
                    print("\'" + e[0] +  "\'")
                else:
                    print(e)
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
        print(s)
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
            elif s[0] == 'and' or s[0] == 'or':
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
                # G ^ H
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
        """
            encontra todas as frases numa só bfs pela arvore
        """
        sentencesQueue = Queue()
        bfsQueue = Queue()
        if node.value != 'and': # only one sentence
            sentencesQueue.put(node)
        else:
            bfsQueue.put(node)

        while not bfsQueue.empty():
            node = bfsQueue.get()
            if node.left is not None:
                if node.left.value != 'and': #each sub tree that we find is a sentence
                    sentencesQueue.put(node.left)
                else:
                    bfsQueue.put(node.left)
            if node.right is not None:
                if node.right.value != 'and': #each sub tree that we find is a sentence
                    sentencesQueue.put(node.right)
                else:
                    bfsQueue.put(node.right)
        sentences = []
        while not sentencesQueue.empty():
            node = sentencesQueue.get()
            s = []
            bfsQueue = Queue()
            bfsQueue.put(node)
            while not bfsQueue.empty():
                node2 = bfsQueue.get()
                if node2.value != 'or':
                    s.append(node2.value)
                else:
                    if node2.left is not None:
                        bfsQueue.put(node2.left)
                    if node2.right is not None:
                        bfsQueue.put(node2.right)
            sentences.append(s)
        return sentences
