def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    start = 0
    while True:
        pos = dna_string1.find(dna_string2, start)
        print(f"pos: {pos}, start: {start}")
        if pos == -1:
            break
        positions.append(pos + 1)
        start = pos + 1
    return tuple(positions)