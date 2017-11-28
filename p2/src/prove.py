import sys
def main(args):
    sentences = []
    with sys.stdin as f : #open stdin as a file
        for line in lines: # convert each line to a python object
            line = line.rstrip()
            sentences.append(tupple(eval(line)))

    print(sentences)


if __name__ == '__main__':
    print(main(sys.argv))
