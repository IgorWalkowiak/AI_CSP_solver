import copy
import operator


class Backtracking_search:
    def __init__(self, problem):
        self.problem = problem
        self.solutions = []
    def rec_backtracking_search(self, assignments):

        #("rec_backtracking_search")
        if len(assignments) == len(self.problem.variables):
            return assignments

        var = self._get_next_variable(assignments)
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

    def _get_next_variable(self, assignemnts):
        used_vars = assignemnts.keys()
        print(used_vars)
        unused = set(self.problem.variables) - set(used_vars)
        return self._degree_heuristic(used_vars, unused)
        #return list(unused)[0]

    # Najbardziej ograniCZONA zmienna
    def _minimum_remaining_values(self, used, unused):
        vars_rank = {key: 0 for key in unused}
        for X, Y in self.problem.connections:
            if X in used and Y in unused:
                vars_rank[Y] = vars_rank[Y]+1
            elif Y in used and X in unused:
                vars_rank[X] = vars_rank[X]+1
        #key with max value
        return max(vars_rank.items(), key=operator.itemgetter(1))[0]

    # Najbardziej ograniczaJĄCA zmienna
    def _degree_heuristic(self, used, unused):
        vars_rank = {key: 0 for key in unused}
        for X, Y in self.problem.connections:
            if Y in unused:
                vars_rank[Y] = vars_rank[Y]+1
            if X in unused:
                vars_rank[X] = vars_rank[X]+1

        return max(vars_rank.items(), key=operator.itemgetter(1))[0]


