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
