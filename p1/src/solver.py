import argparse
import sys

def readFile(filename):

    with open(filename, 'r')  as f:
        lines = f.readlines()

        for line in lines:
            data = line.split()
            if(line[0]=='V'): #vertice
                vId,weight = data[0],data[1]
                print("Vertice Id: %s Weight: %s" %(vId,weight))
            elif(line[0]=='E'): #edge
                vId1,vId2 = data[1],data[2]
                print("Vertice Id1: %s Vertice Id2: %s" %(vId1,vId2))
            elif(line[0]=='L'): #launch
                date,max_payload,fixed_cost,variable_cost = data[1],data[2],data[3],data[4]
                print("date: %s max_payload: %s fixed_cost: %s variable_cost: %s" %(date,max_payload,fixed_cost,variable_cost))
            else:
                print("Invalid File Format")
                #raise



def main(args):
    readFile(args[1])

def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('SearchType',type=str, help='SearchType that should be use can be uninformed search method or informed search method')

    return parser.parse_args(argv)


if __name__ == '__main__':
    main(sys.argv[1:])
