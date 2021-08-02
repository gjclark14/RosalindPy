# nucleotides = [countA, countC, countG, countT]
nucleotides = [0, 0, 0, 0]
A = 0
C = 1
G = 2
T = 3

f = open('rosalind_dna.txt', 'r')
S = f.read()
for c in S:
    if c == 'A':
        nucleotides[A] += 1
    elif c == 'C':
        nucleotides[C] += 1
    elif c == 'G':
        nucleotides[G] += 1
    else:
        nucleotides[T] += 1

f = open('output.txt', 'w')
print(*nucleotides, sep=' ', file=f)
