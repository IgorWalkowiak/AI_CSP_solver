import map_problem
import einstein_problem
import backtracking_search as BTA

#problem = einstein_problem.Einstein_problem()
problem = map_problem.Map_problem(3)
solver = BTA.Backtracking_search(problem)
solver.solve()
#for solution in solver.solutions:
    #print(solution)