from __future__ import print_function
from ortools.sat.python import cp_model
from CompSolverDemoData.hard_coded_info import hardcodedinfo
from CompSolver.comp_printer import SolutionPrinter


def main():
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()
    # comp_dao = CompDAO()
    data = hardcodedinfo()

    raider_to_toon = []
    j = 0
    for p in range(len(data.toons)):
        j += len(data.toons[p][1])
        for t in range(len(data.toons[p][1])):
            raider_to_toon.append(data.raiders[p])

    num_roles = len(data.roles)
    num_raiders = len(data.raiders)
    num_toons = len(raider_to_toon)

    mallowed_groups = []
    for player in range(num_raiders):
        group = []
        n = len(data.toons[player][1])
        s = 0
        for toon in range(n):
            subset = []
            for g in range(n):
                if g == s:
                    subset.append(1)
                else:
                    subset.append(0)

            group.append(subset)
            s += 1
        mallowed_groups.append(group)

    comp = {}
    for toon in range(num_toons):
        for role in range(num_roles):
            comp[toon, role] = model.NewBoolVar(f'comp[{toon},{role}]')

    for role in range(num_roles):
        model.Add(sum(comp[toon, role] for toon in range(num_toons)) == data.role_amount_req[role])

    # if selected - affinity above 0
    for t in range(num_toons):
        for r in range(num_roles):
            model.Add(comp[t, r] * data.task_affinity[t][r] > 0).OnlyEnforceIf(comp[t, r])

    selected_toon = {}
    for toon in range(num_toons):
        selected_toon[toon] = model.NewBoolVar(f'toon[{toon}]')

    for toon in range(num_toons):
        for role in range(num_roles):
            model.Add(selected_toon[toon] > 0).OnlyEnforceIf(comp[toon, role])

    toon = 0
    for raider in range(num_raiders):
        toons = len(mallowed_groups[raider])
        meow = []
        for build in range(toons):
            meow.append(selected_toon[toon])
            toon += 1
        model.AddAllowedAssignments(meow, mallowed_groups[raider])

    # Maximize role affinity
    [model.Maximize(sum(
        comp[t, r] * data.task_capacity[t][r] * data.task_affinity[t][r] for t in range(num_toons)
        for r in range(num_roles)))]

    # Minimize distribution
    model.Minimize(sum(selected_toon[t] for t in range(num_toons)))

    solver.parameters.enumerate_all_solutions = True
    callback = SolutionPrinter(num_toons, num_roles, comp, 5)
    status = solver.Solve(model, callback)

    print('status:' + solver.StatusName())
    # print('branches: %i' % solver.NumBranches())
    # print(solver.ObjectiveValue())
    # print('conflicts: %c' % solver.NumConflicts())
    print('time: %f' % solver.WallTime())

    comp_result = []
    solutions = callback.combinations()

    for solution in range(callback.number_of_solutions()):
        print('Solution %i' % (solution + 1))
        for assigned in range(len(solutions[solution])):
            toon = solutions[solution][assigned][0]
            role = solutions[solution][assigned][1]
            comp_result.append(
                [{raider_to_toon[toon], data.roles[role], data.affinity[data.task_affinity[toon][role]]}])
            print(raider_to_toon[toon], 'assigned to task', data.roles[role], ',affinity =',
                  data.affinity[data.task_affinity[toon][role]])

    return comp_result


if __name__ == '__main__':
    result = main()
