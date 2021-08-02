from src.utils.FastaParser import parse

fastas = parse('rosalind_gc.txt')


def get_frequencies(fastas):
    frequencies = []
    for f in fastas:
        frequencies.append((f.get_TAG(), f.get_GC_content()))
    return frequencies


frequencies = get_frequencies(fastas)

max = 0
max_frequency = ()
for f in frequencies:
    if f[1] > max:
        max = max
        max_frequency = f

print(f'{max_frequency[0]}\n{max_frequency[1]:.6f}', file=open('output.txt', 'w'))
