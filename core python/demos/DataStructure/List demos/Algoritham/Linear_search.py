def linearSearch(li,search_ele):
    for ind in range(0,len(li)):
        if (li[ind]==search_ele):
            return ind
    else:
        return -1
ele=int(input('Enter Element:'))
li=[45,37,81,77,53,34,26,82]
res=linearSearch(li,ele)
if(res!=-1):
    print(f'{ele}element is present in index{res}')
else:
    print(f'{ele} element is not present in list ')
