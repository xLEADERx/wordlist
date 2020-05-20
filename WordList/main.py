import itertools
from progress.bar import Bar
import math
import sys


def genreator(file_path, chars, min_length, max_length, Prefix = ''):
    with open(file_path, 'w') as file:
        with Bar('Processing', max=int(math.pow(int(len(chars)), int(max_length))), suffix='%(percent)d%%') as bar:
            if min_length == max_length:
                for w in itertools.product(chars, repeat=int(min_length)):
                    word = ''.join(w)
                    file.write(word+"\n")
                    bar.next()
            elif max_length > min_length:
                for i in range(min_length, max_length + 1):
                    for w in itertools.product(str(chars), repeat=i):
                        word = ''.join(w)
                        file.write(Prefix+word+"\n")
                        bar.next()


if __name__ == '__main__':
    if sys.argv[2] > sys.argv[3]:
        print('[-] Min length cannot be greater than Max length')
        sys.exit(1)
        
    print('Creating Wordlist...')
    if len(sys.argv) == 6: genreator(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else: genreator(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print('[+]Wordlist Created Succesfully..')
