import operator


# Najbardziej ograniCZONA zmienna
def _minimum_remaining_values(csp, used, unused):
    vars_rank = {key: 0 for key in unused}
    for X, Y in csp.connections:
        if X in used and Y in unused:
            vars_rank[Y] = vars_rank[Y] + 1
        elif Y in used and X in unused:
            vars_rank[X] = vars_rank[X] + 1
    # key with max value
    return max(vars_rank.items(), key=operator.itemgetter(1))[0]


# Najbardziej ograniczaJĄCA zmienna
def _degree_heuristic(csp, used, unused):
    vars_rank = {key: 0 for key in unused}
    for X, Y in csp.connections:
        if Y in unused:
            vars_rank[Y] = vars_rank[Y] + 1
        if X in unused:
            vars_rank[X] = vars_rank[X] + 1

    return max(vars_rank.items(), key=operator.itemgetter(1))[0]