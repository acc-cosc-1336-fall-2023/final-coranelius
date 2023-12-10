def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    start = 0
    while True:
        pos = dna_string1.find(dna_string2, start)
        if pos == -1:
            break
        positions.append(pos + 1) 
        start = pos + 1
    return tuple(positions)


def validate_input(prompt, length):
    while True:
        user_input = input(prompt)
        if len(user_input) == length:
            return user_input
        print(f"Please enter a string of length {length}.")


def main():
    while True:
        dna_string1 = validate_input("Enter the DNA string (Make sure its 8 to 16 characters): ", 8)
        dna_substring = validate_input("Enter the DNA substring (Make sure its 4 characters): ", 4)

        result = get_most_likely_ancestor_consensus(dna_string1, dna_substring)
        print("Result:", result)

        choice = input("Would you like to continue (Y/N)? ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()