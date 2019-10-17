# -*- coding: utf-8 -*-
from gurobipy import Model,GRB

m = Model("hw52")

wA = m.addVar(vtype=GRB.BINARY, name = 'wA')
wB = m.addVar(vtype=GRB.BINARY, name = 'wB')
wC = m.addVar(vtype=GRB.BINARY, name = 'wC')

s1wA = m.addVar(vtype=GRB.INTEGER, name = 's1wA')
s2wA = m.addVar(vtype=GRB.INTEGER, name = 's2wA')
wAd1 = m.addVar(vtype=GRB.INTEGER, name = 'wAd1')
wAd2 = m.addVar(vtype=GRB.INTEGER, name = 'wAd2')

s1wB = m.addVar(vtype=GRB.INTEGER, name = 's1wB')
s2wB = m.addVar(vtype=GRB.INTEGER, name = 's2wB')
wBd1 = m.addVar(vtype=GRB.INTEGER, name = 'wBd1')
wBd2 = m.addVar(vtype=GRB.INTEGER, name = 'wBd2')

s1wC = m.addVar(vtype=GRB.INTEGER, name = 's1wC')
s2wC = m.addVar(vtype=GRB.INTEGER, name = 's1wC')
wCd1 = m.addVar(vtype=GRB.INTEGER, name = 'wCd1')
wCd2 = m.addVar(vtype=GRB.INTEGER, name = 'wCd2')

s1d1 = m.addVar(vtype=GRB.INTEGER, name = 's1d1')
s1d2 = m.addVar(vtype=GRB.INTEGER, name = 's1d2')
s2d1 = m.addVar(vtype=GRB.INTEGER, name = 's2d1')
s2d2 = m.addVar(vtype=GRB.INTEGER, name = 's2d2')

m.update()

m.setObjective(
        (wA*(50 + s1wA + 6*s2wA + 4*wAd1 + 6*wAd2)) + 
        (wB*(60 + 2*s1wB + 3*s2wB + 3*wBd1 + 4*wBd2)) + 
        (wC*(68 + 8*s1wC + s2wC + 5*wCd1 + 3*wCd2)) + 
        (4*s1d1 + 8*s1d2 + 7*s2d1 + 6*s2d2),
        GRB.MINIMIZE)

m.addConstr(wA + wB + wC <= 1)

m.addConstr(s1wA + s1wB + s1wC + s1d1 + s1d2 <= 50)
m.addConstr(s2wA + s2wB + s2wC + s2d1 + s2d2 <= 75)

m.addConstr(s1d1 + s2d1 + wAd1 + wBd1 + wCd1 >= 75)
m.addConstr(s1d2 + s2d2 + wAd2 + wBd2 + wCd2 >= 50)

m.addConstr(s1wA + s2wA <= 99999999 * wA)
m.addConstr(s1wB + s2wB <= 60 * wB)
m.addConstr(s1wC + s2wC <= 70 * wC)

m.addConstr(wAd1 + wAd2 <= s1wA + s2wA)
m.addConstr(wBd1 + wBd2 <= s1wB + s2wB)
m.addConstr(wCd1 + wCd2 <= s1wC + s2wC)

m.optimize()

for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
    
print('Obj: %f' % m.objVal)
