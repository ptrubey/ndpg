import glob, csv, re
from collections import defaultdict

loweralphabet = 'abcdefghijklmnopqrstuvwxyz'
upperalphabet = loweralphabet.upper()
alphabetset = set(loweralphabet + upperalphabet)

def wordcount(fstring, wordsdict):
    cleaned_fstring = re.sub(r"[,.;@#?!&$\}\{]+\ *", " ", fstring)
    
    for word in cleaned_fstring.split():
        if len(set(word).difference(alphabetset)) == 0:
            if len(word) >= 5:
                wordsdict[word] += 1
    pass

if __name__ == '__main__':
    files = glob.glob('*.tex')
    words = defaultdict(int)
    for file in files:
        with open(file, 'r') as fstring:
            wordcount(fstring.read(), words)
    lout = [(k,v) for k, v in words.items()]
    with open('wordcount.csv', 'w') as fout:
        csv_out = csv.writer(fout)
        csv_out.writerow(['word','count'])
        for row in lout:
            csv_out.writerow(row)
    pass

# EOF

