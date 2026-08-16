# Q13.Python Program to Count Number of digits and letter in string
# Without method
s=input("Enter String:")
countNumber=0
countLetter=0
for i in s:
    if(i>='0' and i<='9'):
        countNumber=countNumber+1
    elif(i>'a',i<'z')or(i>'A',i<'Z'):
        countLetter=countLetter+1
print('count Number of digit',countNumber)
print('count Number of letter',countLetter)

# with method
# s=input("Enter string:")
# countNumber=0
# countLetter=0
# for i in s:
#     if(i.isdigit()):
#         countNumber=countNumber+1
#     elif(i.isalpha()):
#         countLetter=countLetter+1
# print('count number of digit',countNumber)
# print('count number letter',countLetter)