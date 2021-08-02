f = open('rosalind_revc.txt', 'r')
S = f.read()

S_complement = ''
for c in reversed(S):
    if c == 'A':
        S_complement += 'T'
    elif c == 'C':
        S_complement += 'G'
    elif c == 'G':
        S_complement += 'C'
    elif c == 'T':
        S_complement += 'A'

f = open('output.txt', 'w')
print(S_complement, file=f)

