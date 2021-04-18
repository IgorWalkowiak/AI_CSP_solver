import copy
import value_heuristic
import variable_heuristic

class Backtracking_search:
    def __init__(self, problem):
        self.problem = problem
        self.solutions = []
    def rec_backtracking_search(self, assignments):
        if len(assignments) == len(self.problem.variables):
            return assignments

        var = self._get_next_variable(assignments)
        for domain_value in value_heuristic.get_next_least_constraining_value(self.problem, assignments, var):
            assignments[var] = domain_value
            if self.problem.constrains_function(assignments):
                result = self.rec_backtracking_search(copy.deepcopy(assignments))
                if result != None:
                    self.solutions.append(copy.deepcopy(result))
                del assignments[var]
            else:
                del assignments[var]
        return None

    def solve(self):
        return self.rec_backtracking_search({})

    def _get_next_variable(self, assignemnts):
        used_vars = assignemnts.keys()
        print(used_vars)
        unused = set(self.problem.variables) - set(used_vars)
        return variable_heuristic._degree_heuristic(self.problem, used_vars, unused)
        #return list(unused)[0]




