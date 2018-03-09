def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        count = 0
        for i in zip(strand_a, strand_b):
            if i[0] != i[1]:
                count += 1
    else:
        raise ValueError("Input strands are not of equal length")
    
    return count