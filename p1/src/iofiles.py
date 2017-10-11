class Launch():
    def __init__(self,date,max_payload,fixed_cost,variable_cost):
        self.date = date
        self.max_payload = max_payload
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost
    def __repr__(self):
        return ("%s,%s,%s,%s"%(self.date,self.max_payload,self.fixed_cost,self.variable_cost))
    def computeCost(self):
        return (self.fixed_cost + self.variable_cost * totalWeight)
    def 
