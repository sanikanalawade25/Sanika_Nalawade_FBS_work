# Q9.Python Program to calculate Number of Words and Number of Charater present string
# Withot Method-
    
s=input("Enter String:")
countCh=0
countWt=1
for i in s:
    if(i!=' '):
        countCh=countCh+1
    if(i==' '):
        countWt=countWt+1
print('Number of countCh',countCh)
print('Number of countWt',countWt)

# with method-

# s=input("Enter String:")
# word=s.split()
# charaters=len(s.replace(' ',''))
# print('Number of Words',len(word))
# print('Number of Charater',charaters)