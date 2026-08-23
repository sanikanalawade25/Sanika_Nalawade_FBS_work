# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.
string=['eat','tea','tan','ate','bat','aab','nat','aba']
groups=[]
for word in string:
    found=False
    for group in groups:
        if(len(word)==len(group[0])):
            is_anagrams=True
            for ch in set(word):
                if(word.count(ch)!=group[0].count(ch)):
                    is_anagrams=False
                    break
            if is_anagrams:
                group.append(word)
                found=True
                break
    if not found:
        groups.append([word])
print('List',string)
print('Grouped Anagrams:')
for group in groups:
    print(group)
