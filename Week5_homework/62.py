# -*- coding: utf-8 -*-
"""
@author: TaiT_
"""

from gurobipy import Model,GRB

m = Model("hw62")

p1m1 = m.addVar(lb = 0, vtype=GRB.INTEGER, name = 'No. of units sent from P1 to M1')
p1m2 = m.addVar(lb = 0, vtype=GRB.INTEGER, name = 'No. of units sent from P1 to M2')
p1m3 = m.addVar(lb = 0, vtype=GRB.INTEGER, name = 'No. of units sent from P1 to M3')

p2m1 = m.addVar(lb = 0, vtype=GRB.INTEGER, name = 'No. of units sent from P2 to M1')
p2m2 = m.addVar(lb = 0, vtype=GRB.INTEGER, name = 'No. of units sent from P2 to M2')
p2m3 = m.addVar(lb = 0, vtype=GRB.INTEGER, name = 'No. of units sent from P2 to M3')

m.update()

m.setObjective((3*p1m1 + 4*p1m2 + 6*p1m3 + 5*p2m1 + 7 *p2m2 + 5*p2m3),GRB.MINIMIZE)

m.addConstr(p1m1 + p2m1 >= 17)
m.addConstr(p1m2 + p2m2 >= 8)
m.addConstr(p1m3 + p2m3 >= 10)

m.addConstr(p1m1 + p1m2 + p1m3 <= 15)
m.addConstr(p2m1 + p2m2 + p2m3 <= 20)

m.optimize()

for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))

print('Obj: %f' % m.objVal)