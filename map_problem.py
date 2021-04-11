



class Map_problem:
    def __init__(self, color_number):
        self._color_number = color_number
        self.domain = list(range(1, color_number+1))
        self.variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
        print(self.domain)

    def constrains_function(self, assignments):
        connections = [ ('WA', 'NT'), ('WA','SA'),
                        ('NT','Q'), ('NT','SA'),
                        ('SA', 'Q'), ('SA', 'V'),
                        ('SA', 'NSW'), ('V','NSW'),
                        ('NSW', 'Q')
                      ]
        for connection in connections:
            try:
                if assignments[connection[0]] == assignments[connection[1]]:
                    return False
            except:
                pass

        return True


