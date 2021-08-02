

class Fasta:
    def __init__(self, TAG, DNA):
        self.TAG = TAG
        self.DNA = DNA

    def __repr__(self):
        return f'{self.TAG}\n{self.DNA}'

    def get_DNA(self):
        return self.DNA

    def get_TAG(self):
        return self.TAG

    def get_GC_content(self):
        gc_count = 0
        for c in self.DNA:
            if c == 'G' or c == 'C':
                gc_count += 1
        return 100 * (gc_count / len(self.DNA))



def parse(file_name):
    fastas = []
    f = open(file_name, 'r')
    lines = f.readlines()
    i = 0
    while i < len(lines):
        tag = ''
        dna = ''
        if lines[i].startswith('>'):
            tag = ''.join(lines[i].split()).strip('>')
            i += 1
            while i < len(lines) and (not lines[i].startswith('>')):
                dna += ''.join(lines[i].split())
                i += 1
        fastas.append(Fasta(tag, dna))
    return fastas
