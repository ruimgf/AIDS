import sys

class SentencesReader():
    @staticmethod
    def readstdin():
        with sys.stdin as f :
            lines = f.readlines()
            sentences = []
            for line in lines:
                line = line.rstrip()
                sentences.append(eval(line))
        return sentences
