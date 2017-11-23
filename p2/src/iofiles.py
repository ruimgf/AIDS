import sys

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
            if type(s) is str:
                pass
            elif type(s) is tuple:
                if s[0] == 'not':
                    pass
                elif s[0] == 'and':
                    pass
                elif s[0] == 'or':
                    pass
                elif s[0] == '=>':
                    pass
                elif s[0] == '<=>':
                    pass
                else:
                    raise IOError
            else:
                raise IOError
