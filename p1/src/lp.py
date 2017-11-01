from pulp import *

max = [22.8,22.8,140,70,22.8,250,22.8,22.8,23,115]
cf = [62,62,90,85,62,132,49,49,32,86]
cv = [0.4,0.4,1.8,1.2,1.2,1.6,0.4,0.4,1,1.2]
P = 138.2

prob = LpProblem("test1", LpMinimize)




p1 = LpVariable('p1', lowBound=0, cat='Continuous')
p2 = LpVariable('p2', lowBound=0, cat='Continuous')
p3 = LpVariable('p3', lowBound=0, cat='Continuous')
p4 = LpVariable('p4', lowBound=0, cat='Continuous')
p5 = LpVariable('p5', lowBound=0, cat='Continuous')
p6 = LpVariable('p6', lowBound=0, cat='Continuous')
p7 = LpVariable('p7', lowBound=0, cat='Continuous')
p8 = LpVariable('p8', lowBound=0, cat='Continuous')
p9 = LpVariable('p9', lowBound=0, cat='Continuous')
p10 = LpVariable('p10', lowBound=0, cat='Continuous')

y1 = LpVariable('y1', cat='Binary')
y2 = LpVariable('y2', cat='Binary')
y3 = LpVariable('y3', cat='Binary')
y4 = LpVariable('y4',cat='Binary')
y5 = LpVariable('y5',cat='Binary')
y6 = LpVariable('y6',cat='Binary')
y7 = LpVariable('y7', cat='Binary')
y8 = LpVariable('y8',cat='Binary')
y9 = LpVariable('y9',cat='Binary')
y10 = LpVariable('y10',cat='Binary')


prob += y1*cf[0] + cv[0]*p1 + y2*cf[1] + cv[1]*p2  + y3*cf[2] + cv[2]*p3  + y4*cf[3] + cv[3]*p4  + y5*cf[4] + cv[4]*p5 + y6 * cf[5] + cv[5] * p6  + y7*cf[6] + cv[6]*p7  + y8*cf[7] + cv[7]*p8  + y9*cf[8] + cv[8]*p9 + y10*cf[9] + cv[9]*10

prob += p1 <= max[0] * y1
prob += p2 <= max[1] * y2
prob += p3 <= max[2] * y3
prob += p4 <= max[3] * y4
prob += p5 <= max[4] * y5
prob += p6 <= max[5] * y6
prob += p7 <= max[6] * y7
prob += p8 <= max[7] * y8
prob += p9 <= max[8] * y9
prob += p10 <= max[9] * y10

prob += p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 == P

print(prob.solve())
print(LpStatus[prob.status])

for variable in prob.variables():
    print("{} = {}".format(variable.name, variable.varValue))

print(value(prob.objective))