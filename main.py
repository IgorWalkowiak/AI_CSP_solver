import map_problem


problem = map_problem.Map_problem(4)
asignm = {'WA':1, 'SA':3, 'T':2}
result = problem.constrains_function(asignm)
print(result)