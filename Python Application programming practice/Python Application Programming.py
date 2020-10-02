# opening , writing, reading, closing a file
# writing
##fp = open('a.txt','w')
##fp.write('hey there, this is an example of file writing \n')
##fp.writelines(['See you soon\n', 'over and out '])
##fp.close()
##
###reading
##fp = open('a.txt','r')
###print(fp.read(3))  # reads the first 3 bytes of the file
##print(fp.read())   # reads the rest of the content of the file
##for line in fp.readlines():
##    print(line)


# regular expressions in python
##import re    #python uses 're' package to deal with regular expressions
##pattern = 'for'
##text = 'information'
##if re.search(pattern, text):
##    print('Yes')
##else:
##    print('No')

#find all the text portions contained between - or *
##zenPython = '''
##The Zen of Python, by Tim Peters
##
##Beautiful is better than ugly.
##Explicit is better than implicit.
##Simple is better than complex.
##Complex is better than complicated.
##Flat is better than nested.
##Sparse is better than dense.
##Readability counts.
##Special cases aren't special enough to break the rules.
##Although practicality beats purity.
##Errors should never pass silently.
##Unless explicitly silenced.
##In the face of ambiguity, refuse the temptation to guess.
##There should be one-- and preferably only one --obvious way to do it.
##Although that way may not be obvious at first unless you're Dutch.
##Now is better than never.
##Although never is often better than *right* now.
##If the implementation is hard to explain, it's a bad idea.
##If the implementation is easy to explain, it may be a good idea.
##Namespaces are one honking great idea -- let's do more of those!
##'''
##
##import re
##
##portions=re.findall("[-*] ?([^-*].*?) ?[-*]",zenPython)
##print(portions)

#replace all the words ROAD with RD.
import re
def subst(pattern, replace_str, string):
    #susbstitute pattern and return it
    addr1 = re.sub(pattern, replace_str, string)
    return addr1

addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']
            
#Create pattern Implementation here 
pattern = r'\bROAD\b'
replace_str = 'RD.'
    
#Use subst function to replace 'ROAD' to 'RD.',Store as new_address
new_address = [subst(pattern, replace_str, line) for line in addr]

print(new_address)





