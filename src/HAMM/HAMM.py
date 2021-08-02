f = open('rosalind_hamm.txt', 'r')
lines = f.readlines()

piggy = 0
for i in range(0, len(lines[0])):
    if lines[0][i] != lines[1][i]:
        piggy += 1

print(piggy, file=open('output.txt', 'w'))
