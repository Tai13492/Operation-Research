from gurobipy import Model,GRB, multidict, quicksum

m = Model("hw61")

nodes = ['A','B','C','D','E','Home']

cost = {
    ('A','B'): 2429,
    ('A','C'): 1967,
    ('A','D'): 1497,
    ('A','E'): 1650,
    ('A','Home'): 2392,
    ('B','A'): 2429,
    ('B','C'): 1105,
    ('B','D'): 1674,
    ('B','E'): 1320,
    ('B','Home'): 5566,
    ('C','A'): 1967,
    ('C','B'): 1105,
    ('C','D'): 2023,
    ('C','E'): 9527,
    ('C','Home'): 560,
    ('D','A'): 1497,
    ('D','B'): 1674,
    ('D','C'): 2023,
    ('D','E'): 1999,
    ('D','Home'): 1273,
    ('E','A'): 1650,
    ('E','B'): 1320,
    ('E','C'): 9527,
    ('E','D'): 1999,
    ('E','Home'): 778,
    ('Home','A'): 2392,
    ('Home','B'): 5566,
    ('Home','C'): 560,
    ('Home','D'): 1273,
    ('Home','E'): 778,
}

arcs, cost = multidict(cost)


x = {}
u = {}

#print arcs
#print cost

for i,j in arcs:
    x[i,j] = m.addVar(obj=cost[i,j], vtype = 'B',
    name='x_%s%s' % (i, j))
   
N = len(nodes)
for i in nodes:
    if i != nodes[N-1]:
        u[i] = m.addVar(obj=0, name='u_%s' % i)

m.update()


for j in nodes:
    m.addConstr(quicksum(x[i,j] for i in nodes if i != j) == 1,'incom_%s' % (j))
for i in nodes:
    m.addConstr(quicksum(x[i,j] for j in nodes if i != j) == 1,'outgo_%s' % (i))
    
for i,j in arcs:
    if i != nodes[N-1] and j != nodes[N-1]:
        m.addConstr(u[i] - u[j] + N*x[i,j] <= N-1,'subtour_%s_%s' % (i, j))
        
m.optimize()

if m.status == GRB.Status.OPTIMAL:
    print 'objective: %f' % m.ObjVal
    solution = m.getAttr('x', x)
    for i,j in arcs:
        if solution[i,j] > 0:
            print('%s -> %s: %g' % (i, j, solution[i,j]))






