import json

# Open the text file for reading
with open('Bible.txt', 'r') as file:
    # Read the entire file contents into a string
    bible = file.read()

# [ (Book: str, Ch: int, V: int, line: str) ]

b = []

lines = bible.split("\n")
chapter = ''
count = 0
# Print each line
for line in lines:
    if len(line.strip()) == 0:
        chapter = ''
        continue
    if chapter == '':
        chapter = line
        continue
    
    chnum = chapter.split(' ')[-1]
    book = chapter[:-len(chnum)-1]
    verse = line.split(' ')[0]
    line = line[len(verse)+1:]
    
    #if int(chnum) <= 12 and int(verse) < 60:
    if True: # "bap" in line:
        print(book, chnum + ":" + verse, line)
        count += 1
        b.append( {'book':book, 'chapter':int(chnum), 'verse':int(verse), 'text':line} )
print(count, 'References')

with open('bibjson.josn', 'w') as file:
    json.dump(b, file, indent=4)


# There are 31102 Bible verses
# There are 14090 Bible verses within 1:01 and 12:59
# There are 22005 Bible verses within 1:01 and 23:59

