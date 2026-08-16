# Q8 Python Program to Count The Frequenc of Words Appening in string using a dictionary
s=input('Enter String:')
words=s.split()
d={}
for word in words:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1
print('word frequency',d)