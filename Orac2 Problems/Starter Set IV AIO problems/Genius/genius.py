import sys

def main():
    num_people, num_problems = map(int, sys.stdin.readline().split())
    solution_dict = {people: 0 for people in range(1, num_people + 1)}
    total_solved = 0
    solving_amount = 1
    person_solving = 1
    while total_solved + solving_amount < num_problems:
        solution_dict[person_solving] += solving_amount
        total_solved += solving_amount
        solving_amount += 1
        person_solving = max((person_solving + 1) % (num_people + 1), 1)
    solving_amount = num_problems - total_solved
    solution_dict[person_solving] += solving_amount
    biggest_solved_amount = max(solution_dict.values())
    for people in solution_dict:
        if solution_dict[people] == biggest_solved_amount:
            print(people, biggest_solved_amount)
            sys.exit()

    
    



if __name__ == "__main__":
    main()


