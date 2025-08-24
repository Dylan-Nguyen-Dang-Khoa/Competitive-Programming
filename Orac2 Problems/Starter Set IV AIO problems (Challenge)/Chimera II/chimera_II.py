import sys
 
def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    dna_sequence1 = data[1]
    dna_sequence2 = data[2]
    required_sequence = data[3]
    validity = is_valid(dna_sequence1, dna_sequence2, required_sequence)
    if validity:
        print("SUCCESS")
        print(splices_num(dna_sequence1, dna_sequence2, required_sequence))
    else:
        print("PLAN FOILED")
 
 
def is_valid(sequence1, sequence2, requirement):
    for index, letter in enumerate(requirement):
        if letter not in [sequence1[index], sequence2[index]]:
            return False
    return True
 
def splices_num(sequence1, sequence2, requirement):
    splices1 = 0
    splices2 = 0
    current_sequence = -1
    for index, letter in enumerate(requirement):
        if letter == sequence1[index] == sequence2[index]:
            sequence = current_sequence if current_sequence != -1 else 0
        elif letter == sequence1[index]:
            sequence = 0
        elif letter == sequence2[index]:
            sequence = 1
        if sequence != current_sequence and current_sequence != -1:
            splices1 += 1
        current_sequence = sequence
    current_sequence = -1
    for index, letter in enumerate(requirement):
        if letter == sequence1[index] == sequence2[index]:
            sequence = current_sequence if current_sequence != -1 else 1
        elif letter == sequence1[index]:
            sequence = 0
        elif letter == sequence2[index]:
            sequence = 1
        if sequence != current_sequence and current_sequence != -1:
            splices2 += 1
        current_sequence = sequence
    return min(splices1, splices2)
            
 
        
 
if __name__ == "__main__":
    main()
