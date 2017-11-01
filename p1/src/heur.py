import numpy as np
from scipy.optimize import minimize


def func(p):
    totalCost = 0
    for i in range(len(p)):
        if abs(p[i]) > 10**(-1):
            totalCost += cf[i] + p[i] * cv[i]
    return totalCost

def func_deriv(p):
    return cv

cons = ({'type': 'eq',
          'fun' : lambda x: -sum(x) + P,
          'jac' : lambda x: np.array([1,1,1,1,1,1,1,1,1,1])},
        {'type': 'ineq',
          'fun' : lambda x: np.array(x[0]),
          'jac' : lambda x: np.array([1,0,0,0,0,0,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(max[0]-x[0]),
          'jac' : lambda x: np.array([-1,0,0,0,0,0,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(x[1]),
          'jac' : lambda x: np.array([0,1,0,0,0,0,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(max[1]-x[1]),
          'jac' : lambda x: np.array([0,-1,0,0,0,0,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(x[2]),
          'jac' : lambda x: np.array([0,0,1,0,0,0,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(max[2]-x[2]),
          'jac' : lambda x: np.array([0,0,-1,0,0,0,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(x[3]),
          'jac' : lambda x: np.array([0,0,0,1,0,0,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(max[3]-x[3]),
          'jac' : lambda x: np.array([0,0,0,-1,0,0,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(x[4]),
          'jac' : lambda x: np.array([0,0,0,0,1,0,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(max[4]-x[4]),
          'jac' : lambda x: np.array([0,0,0,0,-1,0,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(x[5]),
          'jac' : lambda x: np.array([0,0,0,0,0,1,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(max[5]-x[5]),
          'jac' : lambda x: np.array([0,0,0,0,0,-1,0,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(x[6]),
          'jac' : lambda x: np.array([0,0,0,0,0,0,1,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(max[6]-x[6]),
          'jac' : lambda x: np.array([0,0,0,0,0,0,-1,0,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(x[7]),
          'jac' : lambda x: np.array([0,0,0,0,0,0,0,1,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(max[7]-x[7]),
          'jac' : lambda x: np.array([0,0,0,0,0,0,0,-1,0,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(x[8]),
          'jac' : lambda x: np.array([0,0,0,0,0,0,0,0,1,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(max[8]-x[8]),
          'jac' : lambda x: np.array([0,0,0,0,0,0,0,0,-1,0])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(x[9]),
          'jac' : lambda x: np.array([0,0,0,0,0,0,0,0,0,1])
        },
        {'type': 'ineq',
          'fun' : lambda x: np.array(max[9]-x[9]),
          'jac' : lambda x: np.array([0,0,0,0,0,0,0,0,0,-1])
        }
        )
x0=[20,20,30,20,50,20,20,20,20,20]
res = minimize(func, x0, jac=func_deriv,
               constraints=cons, method='SLSQP', options={'disp': True})
print(res.x)
print(func(res.x))
print(sum(res.x))