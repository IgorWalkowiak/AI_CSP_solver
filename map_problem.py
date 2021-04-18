
class Map_problem:
    def __init__(self, color_number):
        self._color_number = color_number
        self.domain = list(range(1, color_number+1))
        self.variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
        self._make_unsigned_variables()
        self.connections = [ ('WA', 'NT'), ('WA', 'SA'),
                        ('NT', 'Q'), ('NT', 'SA'),
                        ('SA', 'Q'), ('SA', 'V'),
                        ('SA', 'NSW'), ('V', 'NSW'),
                        ('NSW', 'Q')
                      ]
    def _make_unsigned_variables(self):
        self.unsigned_variables = {}
        for var in self.variables:
            self.unsigned_variables[var] = self.domain

        #print(self.unsigned_variables)

    def constrains_function(self, assignments):
        for connection in self.connections:
            try:
                if assignments[connection[0]] == assignments[connection[1]]:
                    return False
            except:
                pass
        return True


