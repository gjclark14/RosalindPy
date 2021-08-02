f = open('rosalind_prot.txt', 'r')
lines = f.readlines()

# Samples
S = lines[0]
t = lines[1]

S = '-' + S
i = 0
len_t = len(t)
while i < len(S):
    # upper limit non-inclusive
    comparison_string = S[i:len_t + i]
    if comparison_string == t:
        print(i)
    i += 1
