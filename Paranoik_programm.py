New_text = ''
a=0
line = ''
abc = 'abcdefghijklmnopqrstuvwuxyz'
with open('TEXTn.txt') as text:
    for iline in text:
        a += 1
        for j in iline:
            for k in abc:
                if k == j:
                    if a == 27:
                        a = 0
                    line = line + (abc[abc.index(k)+a])


        print(line)
        with open('Ne_text.txt','a') as ne_text:
            ne_text.write(f'{line} \n')
        line = ''
