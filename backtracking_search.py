import copy
import value_heuristic
import variable_heuristic

class Backtracking_search:
    def __init__(self, problem, mvc, lcv, forward):
        self.problem = problem
        self.solutions = []
        self.mvc = mvc
        self.lcv = lcv
        self.forward = forward
        self.node_visited = 0

    def rec_backtracking_search(self, assignments, temp_domains):
        if len(assignments) == len(self.problem.variables):
            return assignments

        var = self._get_next_variable(assignments)
        if self.mvc:
            domain = value_heuristic.get_next_least_constraining_value(self.problem, assignments, var, temp_domains)
        else:
            print("assignments",assignments)
            print("temp_domains",temp_domains)
            domain = value_heuristic.get_next_value(var, temp_domains)

        for val in domain:
            assignments[var] = val
            self.node_visited = self.node_visited + 1
            if self.problem.constrains_function(assignments):
                if self.forward:
                    buf = copy.deepcopy(temp_domains) # Chyba lepsze dla procesora, ale gorsze dla pamięci pod względem wydajności
                    self._forward_check(temp_domains, var, val)
                result = self.rec_backtracking_search(copy.deepcopy(assignments), copy.deepcopy(temp_domains))
                if result != None:
                    self.solutions.append(copy.deepcopy(result))
                del assignments[var]
                if self.forward:
                    temp_domains = buf
            else:
                del assignments[var]
        return None

    def solve(self):
        temp_domains = {x: copy.deepcopy(self.problem.domain) for x in self.problem.variables}
        return self.rec_backtracking_search({}, temp_domains)

    def _get_next_variable(self, assignemnts):
        used_vars = assignemnts.keys()
        unused = set(self.problem.variables) - set(used_vars)
        if self.lcv:
            return variable_heuristic._degree_heuristic(self.problem, used_vars, unused)
        else:
            return list(unused)[0]


    # Musiałem inaczej to rozwiązać niż opisuje internet ze względu na chęć zachowania wszystkich
    # możliwych rozwiązań, a nie tylko jednego, przez co pojawia się nowa zmienna 'temp_domains'
    def _forward_check(self, temp_domains, var, val):
        for X, Y in self.problem.connections:
            try:
                if X == var:
                    temp_domains[Y].remove(val)
                elif Y == var:
                    temp_domains[X].remove(val)
            except:
                pass




