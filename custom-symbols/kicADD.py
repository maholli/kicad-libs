import os, sys

dirname = os.path.dirname(__file__)
# print(dirname)
part = []

fileToAdd = sys.argv[1]
# print(fileToAdd)

libraryFile = os.path.join(dirname, 'symbols.lib')

with open(fileToAdd) as symbol:    
    part = symbol.readlines()
    part = [i.replace('SamacSys ECAD Model','') for i in part]
    part[3] = '#\n'

library= []
with open(libraryFile) as file:
    library = file.readlines()

temp = library[:2] +['#\n']+ part[2:-2] + library[2:]

with open(libraryFile, 'w') as file:
	for line in temp:
		file.write(line)