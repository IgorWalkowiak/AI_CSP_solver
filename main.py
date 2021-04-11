import map_problem
import backtracking_search as BTA

problem = map_problem.Map_problem(3)
solver = BTA.Backtracking_search(problem)
print(solver.solve())
for solution in solver.solutions:
    print(solution)