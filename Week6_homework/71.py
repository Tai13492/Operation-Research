from gurobipy import Model, GRB
import BBNode as bn


def logStatus(m):
    status = m.getAttr('Status')
    if status == 2:
        print('Obj: %f' % m.objVal)
        for v in m.getVars():
            print('%s: %f' % (v.varName, v.x))
    else:
        print "Infeasible"
            
m = Model("hw71")

x1 = m.addVar(vtype=GRB.CONTINUOUS, name='x1', obj=8)
x2 = m.addVar(vtype=GRB.CONTINUOUS, name='x2', obj=5)

m.setAttr('ModelSense', GRB.MAXIMIZE)

m.update()

m.addConstr(x1 + x2 <= 6, "c0")
m.addConstr(9*x1 + 5*x2 <= 45, "c1")
m.setParam( 'OutputFlag', False )
m.optimize()

logStatus(m)

root = bn.BBNode(None, '', '', 0)

node1 = bn.BBNode(root,'x1','ub',3)
m1 = m.copy()
m1.addConstr(m1.getVars()[0] <= 3, "node1")
m1.optimize()
logStatus(m1)

node2 = bn.BBNode(root,'x1','lb',4)
m2 = m.copy()
m2.addConstr(m2.getVars()[0] >= 4, "node2")
m2.optimize()
logStatus(m2)

node21 = bn.BBNode(node2,'x2','ub', 1)
m21 = m2.copy()
m21.addConstr(m21.getVars()[1] <= 1,"node21")
m21.optimize()
logStatus(m21)

node22 = bn.BBNode(node2,'x2','lb', 2)
m22 = m2.copy()
m22.addConstr(m22.getVars()[1] >= 2,"node22")
m22.optimize()
logStatus(m22)

node211 = bn.BBNode(node21,'x1','ub', 4)
m211 = m21.copy()
m211.addConstr(m211.getVars()[0] <= 4,"node211")
m211.optimize()
logStatus(m211)

node212 = bn.BBNode(node21,'x1','lb', 5)
m212 = m21.copy()
m212.addConstr(m212.getVars()[0] >= 5,"node212")
m212.optimize()
logStatus(m212)

dvNode = node212
print "Showing bounds from node 212 to root"
while dvNode != root:
    print dvNode.dv, dvNode.boundSense, dvNode.bound
    dvNode = dvNode.parent
