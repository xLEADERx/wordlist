from progress.bar import Bar

maxlen = int(input('Maxlength: '))
prefix = input('Prefix: ')
myrange = int(input('Upper limit: ')) + 1
print('Creating Wordlist...')
with open('wordlist.txt', 'w') as myfile:
    with Bar('Processing', max=myrange, suffix='%(percent)d%%') as bar:  
        for i in range(myrange):
            myfile.write(f'{prefix}{i:0{maxlen}d}\n')
            bar.next()
print('[+]Wordlist Created Succesfully..')
