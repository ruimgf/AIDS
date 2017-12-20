import sys
import os
if __name__ == '__main__':
    ignore_list = ['c','p','%','0']
    l = os.listdir(sys.argv[1])
    for name in l:
        if name=='.DS_Store':
            continue
        with open(sys.argv[1]+name) as f : #open stdin as a file
            print(sys.argv[1]+name)
            f2 = open('out/'+name+'.out','w')
            lines = f.readlines()
            sentences = []
            for line in lines: # convert each line to a python object
                line = line.rstrip()
                if not line:
                    continue
                if line[0] not in ignore_list:
                    result = []
                    l = line.split()
                    for x in l:
                        if(int(x)==0):
                            continue
                        if(int(x)<0):
                            result.append(('not',str(abs(int(x)))))
                        else:
                            result.append(x)

                    f2.write(str(result) + '\n')
