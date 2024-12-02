file_name = 'paper.bib'
output_file = 'paper_title_case.bib'
minor_words = ['for', 'the', 'and', 'to', 'with', 'on', 'from', 'in', 'of', 'by', 'at', 'a']
replace = {'q': 'Q', 'w': 'W', 'e': 'E', 'r':'R', 't':'T','y':'Y','u':'U','i':'I','o':'O','p':'P','a':'A','s':'S','d':'D','f':'F','g':'G','h':'H','j':'J','k':'K','l':'L','z':'Z','x':'X','c':'C','v':'V','b':'B','n':'N','m':'M'}
with open(file_name, 'r', encoding='utf-8') as file1:
    lines = file1.readlines()
with open(output_file, 'w', encoding='utf-8') as file1:
    for line in lines:
        if line[0:11] == "  title = {":
            #print(line)
            title = line[11:-3].split(' ')
            #print(title)
            for index, word in enumerate(title):
                if word not in minor_words:
                    if len(word) > 0:
                        first_letter = word[0]
                        if first_letter != '{':
                            #print(first_letter)
                            #title[index] = word[1:]
                            for key in replace:
                                if first_letter == key:
                                    #print(replace[key])
                                    title[index] = replace[key] + title[index][1:]
            #for word in title:
            #print(' '.join(title))
            file1.write('  title = {' + ' '.join(title) + '},\n')
        else:
            file1.write(line)
