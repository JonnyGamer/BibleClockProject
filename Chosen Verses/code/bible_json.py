import json
import re

# Open the text file for reading
with open('bible_json.json', 'r') as file:
    data = json.load(file)


def check_string(s, word):
    pattern = rf"^({word.capitalize()})|( {word})"
    return True if re.search(pattern, s) else False
def entitle(book, c, v):
    return f"{book} {c}:{v}"
def time(h, m):
    if m < 10:
        return f"{h}:0{m}"
    return f"{h}:{m}"


clock = {}
for h in range(1, 12+1):
    for m in range(0, 60):
        clock[time(h, m)] = []

o = input("Find verses with a specific word? Y/n\n :")
required_word = ''
if o == 'Y':
    required_word = input("Type word\n :")

possible_verses = 0
for d in data:
    book = d['book']
    c = d['chapter']
    v = d['verse']
    text = d['text']
    t = time(c, v)
    bt = time(v, c)
    if required_word == '':
        require = True
    else:
        required_word = check_string(text, 'lov')

    if require:
        possible_verses += 1

    if (t not in clock) and (bt not in clock): continue    


    if c > 0 and c <= 12 and require:# check_string(text, 'lov'):
        clock[t].append((entitle(book, c, v), text))
        #smaller_data.append( {book, c, v, text} )
    #if c > 12 and require:
    #    clock[bt].append((entitle(book, c, v), text))

for i in clock:
    if clock[i] != []: continue
    print("Missing -", i)
    for j in clock[i]:
        print('    -', j[0], j[1])


found = 0
for i in clock:
    if clock[i] != []:
        found += 1

print("Possible Verses:", possible_verses)
print("Clock filled:", found, '/', len(clock))

end = input("Print all available verses? Y/n\n :")

if end == 'Y':
    for i in clock:
        if clock[i] == []: continue
        print(i)
        for j in clock[i]:
            print(' -', '(' + j[0] + ')', j[1])
        print()


#def check_string(s, word):
#    return s.startswith(word.capitalize()) or ' ' + word in s:

# # There are 31102 Bible verses
# # There are 14090 Bible verses within 1:01 and 12:59
# # There are 22005 Bible verses within 1:01 and 23:59

# Missing Times!!!
# 4:55 - 4:59
# 5:49 - 5:59
# 10:53 - 10:59
# 11:58 - 11:59




