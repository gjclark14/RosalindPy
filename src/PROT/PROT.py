from src.utils import CodonTable

f = open('rosalind_prot.txt', 'r')
S = f.read()

n = 3 # chunk length
chunks = [S[i:i+n] for i in range(0, len(S), n)]

prot = ''
for chunk in chunks:
    for codon in CodonTable.codon_table:
        if chunk == codon[0] and codon[1] != 'Stop':
            prot += codon[1]

print(prot, file=open('output.txt', 'w'))

