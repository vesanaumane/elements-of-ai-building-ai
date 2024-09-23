import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    fiveOnesCount = 0
    currentStreak = 0
    for byte in seq:
        if byte == 1:
            currentStreak += 1
            if currentStreak >= 5:
                fiveOnesCount += 1
        else:
            currentStreak = 0 

    return fiveOnesCount

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))