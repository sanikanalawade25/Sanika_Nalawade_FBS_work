# python program to detet if two string are Anagram
# Without method-
str1=input('Enter String1:')
str2=input('Enter String2:')
countstr1=0
countstr2=0
if(len(str1)!=len(str2)):
    print('Not Anagram')
else:
    for ch in str1:
        for i in str1:
            if(ch==i):
                countstr1+=1
        for j in str2:
            if(ch==j):
                countstr2+=1
    if(countstr1==countstr2):
        print('Anagram')
    else:
        print('Not Anagram')

# with method-

# str1=input('Enter String 1:')
# str2=input('Enter String 2:')
# if sorted(str1)==sorted(str2):
#     print("Armstrong")
# else:
#     print("Not Armstrong")

