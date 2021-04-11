


class Backtracking_search:
    def __init__(self, problem):
        self.problem = problem

    def rec_backtracking_search(self, assignments):
        if len(assignments) == len(self.problem.variables):
            return assignments

        var = self._get_unasigned_variable(assignments)
        #print(var)
        for domain_value in self.problem.domain:
            assignments[var] = domain_value
            #print(assignments)
            if self.problem.constrains_function(assignments):
                result = self.rec_backtracking_search(assignments)
                if result != None:
                    return result
                del assignments[var]
            else:
                del assignments[var]
        return None

    def solve(self):
        return self.rec_backtracking_search({})

    def _get_unasigned_variable(self, assignemnts):
        used_vars = assignemnts.keys()
        unused = set(self.problem.variables) - set(used_vars)
        return list(unused)[0]
