import copy


class Backtracking_search:
    def __init__(self, problem):
        self.problem = problem
        self.solutions = []
    def rec_backtracking_search(self, assignments):

        #("rec_backtracking_search")
        if len(assignments) == len(self.problem.variables):
            return assignments

        var = self._get_unasigned_variable(assignments)
        #print(var)
        for domain_value in self.problem.domain:
            assignments[var] = domain_value
            #if len(assignments) >3:
                #print(assignments)
            if self.problem.constrains_function(assignments):
                result = self.rec_backtracking_search(assignments)
                if result != None:
                    self.solutions.append(copy.deepcopy(result))
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
