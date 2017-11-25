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
                        TreeNode('or',('not',SentencesReader.process_sentence(s[1])),('not',SentencesReader.process_sentence(s[2])))
                    elif s[1][0] == 'or':
                        TreeNode('and',('not',SentencesReader.process_sentence(s[1])),('not',SentencesReader.process_sentence(s[2])))
                    elif s[1][0] == '=>':
                        TreeNode('and',SentencesReader.process_sentence(s[1]),('not',SentencesReader.process_sentence(s[2])))
                    elif s[1][0] == '<=>':
            elif s[0] == 'and':
                return TreeNode(s[0],SentencesReader.process_sentence(s[1]),SentencesReader.process_sentence(s[2]))
            elif s[0] == 'or':
                return TreeNode(s[0],SentencesReader.process_sentence(s[1]),SentencesReader.process_sentence(s[2]))
            elif s[0] == '=>':
                return TreeNode('or',SentencesReader.process_sentence(('not',s[1])),SentencesReader.process_sentence(s[2]))
            elif s[0] == '<=>':
                return TreeNode('and',TreeNode('or',SentencesReader.process_sentence(('not',s[1])),SentencesReader.process_sentence(s[2])),TreeNode('or',SentencesReader.process_sentence(('not',s[2])),SentencesReader.process_sentence(s[1])))
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
