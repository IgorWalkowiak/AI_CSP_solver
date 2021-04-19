import map_problem
import einstein_problem
import backtracking_search as BTA

#problem = einstein_problem.Einstein_problem()
problem = map_problem.Map_problem(3)
solver = BTA.Backtracking_search(problem, False, False, True)
solver.solve()

print("DONE!")

print(len(solver.solutions))
print(solver.node_visited)