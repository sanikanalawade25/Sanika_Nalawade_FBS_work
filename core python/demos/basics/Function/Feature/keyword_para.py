def emp(id,name,sal,dept):
    data='ID:'+str(id)+'\n'
    data+='Name:'+(name)+'\n'
    data+='Salary:'+str(sal)+'\n'
    data+='Daparment:'+(dept)+'\n'
    return data
res=emp(name='Sanika',id=101,dept='IT',sal=30000)
print(res)