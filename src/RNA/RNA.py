f = open('rosalind_rna.txt', 'r')
print(f.read().replace('T', 'U'), file=open('output.txt', 'w'))
