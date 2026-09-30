variables = ["Maths", "Python", "DBMS", "AI"]

domains = {
    "Maths": ["9:00 AM", "11:00 AM", "2:00 PM"],
    "Python": ["9:00 AM", "11:00 AM", "2:00 PM"],
    "DBMS": ["9:00 AM", "11:00 AM", "2:00 PM"],
    "AI": ["9:00 AM", "11:00 AM", "2:00 PM"],
}

constraints = [
    ("Maths", "Python"),
    ("DBMS", "AI"),
]


def is_consistent(variable, value, assignment):
    for a, b in constraints:
        if variable == a and b in assignment and assignment[b] == value:
            return False
        if variable == b and a in assignment and assignment[a] == value:
            return False
    return True


def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    unassigned = [v for v in variables if v not in assignment]
    variable = unassigned[0]

    for value in domains[variable]:
        if is_consistent(variable, value, assignment):
            assignment[variable] = value
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[variable]

    return None


def verify(solution):
    all_assigned = all(v in solution for v in variables)
    no_conflicts = all(solution[a] != solution[b] for a, b in constraints)
    return all_assigned and no_conflicts


solution = backtrack({})

if solution:
    print("Final Timetable")
    print("-" * 25)
    for subject in variables:
        print(f"{subject:<8} -> {solution[subject]}")
    print("-" * 25)
    for a, b in constraints:
        print(f"{a} ({solution[a]}) != {b} ({solution[b]})  ->  {solution[a] != solution[b]}")
    print("All constraints satisfied:", verify(solution))
else:
    print("No valid timetable found")