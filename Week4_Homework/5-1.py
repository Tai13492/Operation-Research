from gurobipy import Model,GRB

m = Model("hw51")

x1 = m.addVar(name = "x1")
x2 = m.addVar(name = "x2")

m.update()

m.setObjective(5*x1 + 4*x2,GRB.MAXIMIZE)

m.addConstr(6*x1 + 4*x2 <= 24, 'constraint1')
m.addConstr(x1 + 2*x2 <= 6,'constraint2')
m.addConstr(-x1 + x2 <= 1, 'constraint3')
m.addConstr(x2 <=2,' constraint4')

m.optimize()

for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
    
print('Obj: %f' % m.objVal)

print 'reduced costs: '
print ' ', m.getAttr('rc', m.getVars())
print 'shadow prices: '
print ' ', m.getAttr('pi', m.getConstrs())