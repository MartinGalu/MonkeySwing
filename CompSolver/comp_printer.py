from ortools.sat.python import cp_model


class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, num_toons, num_roles, comp, limit):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__num_toons = num_toons
        self.__num_roles = num_roles
        self.__solutions = []
        self.__comp = comp
        self.__solution_count = 0
        self.__limit = limit

    def on_solution_callback(self):
        self.__solution_count += 1
        """Collect a new combination."""
        new_comp = []
        for t in range(self.__num_toons):
            for r in range(self.__num_roles):
                if self.BooleanValue(self.__comp[t, r]):
                    new_comp.append([t, r])

        self.__solutions.append(new_comp)
        if self.__solution_count >= self.__limit:
            self.StopSearch()

    def combinations(self):
        """Returns all collected combinations."""
        return self.__solutions

    def number_of_solutions(self):
        """Returns all collected combinations."""
        return self.__solution_count
