from src.utils.CodonTable import monoisotopic_table

f = open('rosalind_prtm.txt', 'r')
S = f.read()

sum = 0
for s in S:
    for m in monoisotopic_table:
        if s == m[0]:
            sum += m[1]

print(f'{sum:.3f}', file=open('output.txt', 'w'))
