import pulp
import numpy as np


P = 138.2

def heur_optimal(left_weight,lauches):
    max = [22.8, 22.8, 140, 70, 22.8, 250, 22.8, 22.8, 23, 115]
    cf = [62, 62, 90, 85, 62, 132, 49, 49, 32, 86]
    cv = [0.4, 0.4, 1.8, 1.2, 1.2, 1.6, 0.4, 0.4, 1, 1.2]
    p = []
    y = []
    prob = pulp.LpProblem("test1", pulp.LpMinimize)
    for i in range(len(cf)):
        k = pulp.LpVariable('p'+str(i), lowBound=0, cat='Continuous')
        p.append(k)

    for i in range(len(cf)):
        k = pulp.LpVariable('y'+str(i), cat='Binary')
        y.append(k)



    l=0
    for i in range(len(cf)):
        l += y[i]*cf[i] + cv[i]*p[i]

    prob += l

    l = 0

    for i in range(len(cf)):
        l += p[i]
    prob += l == P

    for i in range(len(cf)):
        prob += p[i] <= max[i] * y[i]
    '''
    print(prob)
    print(prob.solve())
    print(LpStatus[prob.status])
    
    for variable in prob.variables():
        print("{} = {}".format(variable.name, variable.varValue))
    
    print(value(prob.objective))
    '''
    return pulp.value(prob.objective)