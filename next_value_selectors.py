import copy


def get_next_value_random(csp, assignments, var):
    return csp.domain


# Wartość najmniej ograniczająca, czyli dająca najwięcej możliwości do eksploracji
def get_next_least_constraining_value(csp, assignments, var):
    used_vars = assignments.keys()
    unused_neighbors = []
    for X, Y in csp.connections:
        if X == var and Y not in used_vars:
            unused_neighbors.append(Y)
        elif Y == var and X not in used_vars:
            unused_neighbors.append(X)
    values_of_neighbs = [(x, copy.deepcopy(csp.domain)) for x in unused_neighbors]
    for variable, available_values in values_of_neighbs:
        for X, Y in csp.connections:
            if X == variable and Y in used_vars:
                available_values.remove(assignments[Y])
            elif Y == variable and X in used_vars:
                available_values.remove(assignments[X])

    values_to_return = {key: 0 for key in csp.domain}
    for value in csp.domain:
        for variable, available_values in values_of_neighbs:
            if value in available_values:
                values_to_return[value] = values_to_return[value] + 1

    x = sorted(values_to_return.items(), key=lambda item: item[1])
    return [y[0] for y in x]


