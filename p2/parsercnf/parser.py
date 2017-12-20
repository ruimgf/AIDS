import sys

if __name__ == '__main__':
    file=sys.stdin
    ignore_list = ['c','p','%','0']

    with file as f : #open stdin as a file
        lines = f.readlines()
        sentences = []
        for line in lines: # convert each line to a python object
            line = line.rstrip()
            if not line:
                continue
            if line[0] not in ignore_list:
                result = []
                for x in line.split():
                    if(int(x)==0):
                        continue
                    if(int(x)<0):
                        result.append(('not',x[1]))
                    else:
                        result.append(x)
                print(result)
