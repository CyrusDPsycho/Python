alphabets = ['abcdefghijklmnopqrstuvwxyz']
alphabets = list(str(alphabets))
checker = 0
sentence = raw_input().lower()
for j in sentence:
    if(j not in alphabets):
        checker+=1
    else:
       alphabets.remove(j) 

if(checker and alphabets==['[', "'", "'", ']']):
    print 'pangram'
else:
    print 'not pangram'
