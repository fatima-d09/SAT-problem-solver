#!/usr/bin/env python3
import sys
import itertools
from typing import List, Tuple, Dict, Optional

# Attribution: The itertools.product function is used here to generate all possible combinations
# of truth values for the atoms, which is a more efficient method than manually iterating through.
# Reference: https://docs.python.org/3/library/itertools.html#itertools.product

# In my SAT solver, I use `itertools.product` to try every possible combination of true and false for 
# the variables. This saves me from writing multiple loops and ensures that all combinations are checked, 
# no matter how many variables there are.

def parse_input() -> Tuple[List[List[Tuple[str, str]]], List[str]]: # CNF parsing
    clauses, atoms = [], set()
    for line in map(str.strip, sys.stdin):
        if line:
            clause = [(literal[0], literal[1:]) if literal.startswith('~') else ('', literal) 
                      for literal in map(str.strip, line.split(','))]
            clauses.append(clause)
            atoms.update(atom for _, atom in clause)
    return clauses, sorted(atoms)

def is_satisfied(clause: List[Tuple[str, str]], assignment: Dict[str, bool]) -> bool:
    return any(not assignment[atom] if sign == '~' else assignment[atom] for sign, atom in clause)

def find_satisfying_assignment(clauses: List[List[Tuple[str, str]]], atoms: List[str]) -> Optional[Dict[str, bool]]:
    for values in itertools.product([True, False], repeat=len(atoms)): # brute-force assignment checking
        assignment = dict(zip(atoms, values))
        if all(is_satisfied(clause, assignment) for clause in clauses):
            return assignment
    return None

def format_output(assignment: Optional[Dict[str, bool]]) -> str:
    return 'satisfiable ' + ' '.join(f'{atom}={"T" if value else "F"}' for atom, value in assignment.items()) if assignment else 'unsatisfiable'

if __name__ == '__main__':
    clauses, atoms = parse_input()
    print(format_output(find_satisfying_assignment(clauses, atoms)))
