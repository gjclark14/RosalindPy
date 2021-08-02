
def wabbits(n, k):
    rabbits = [1, 1 + k]
    for i in range(2, n):
        rabbits.append(rabbits[i - 1] + k * rabbits[i - 2])
    return rabbits[-2]


f = open('rosalind_fib.txt', 'r')
S = f.read()
print(wabbits(int(S.split(' ')[0]), int(S.split(' ')[1])), file=open('output.txt', 'w'))
