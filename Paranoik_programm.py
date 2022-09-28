def cesar(a):
    with open('TEXTn.txt') as file1:
        for iline in file1:
            new_text_line = ''
            for i in iline:
                if i == ' ':
                    new_text_line = new_text_line = (new_text_line + ' ')
                else:
                    new_text_line = (new_text_line + chr(ord(i)-int(a)))

            with open('Ne_text.txt','a') as new_file:
                new_text_line = new_text_line[:-1]
                new_file.write(('\n') + new_text_line)
                a += 1

a=1
cesar(a)
