# PROJECT 1


## In orbit assembly of large structures
The International Space Station (ISS) is the most complex and the largest structure humans ever placed in orbit. Its assembly, in orbit, started in 1998 and has been continuously inhabited for more than 16 years. Its total mass is about 420 tons and consists of 32 modules (see figure 1).

The assembly of such a structure requires multiple rocket launches, since the payload of a single launch vehicle is limited. Moreover, launches are expensive and require extensive preparation. Therefore, the choice of which components to manifest in each launch, that is, to include in the payload of a launch vehicle, has to be carefully done.

This mini-project addresses the problem of scheduling the launch of components for the in orbit assembly of a large structure. Given a set of components to be launched, a launch timeline and costs, and a construction plan, the goal is to determine the assignment of components to launches, such as the total cost is minimized. In the next section the problem will be formally specified.

Usage:
```
python3 solver.py [-u,-i] graphFile
-u uniformed search
-i informed search
```
