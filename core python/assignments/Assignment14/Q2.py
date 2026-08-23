# Q2.Write Python Proram to remove the intersection second set with first set
s1={10,20,30,40}
s2={30,40,50,60}
print('set 1',s1)
print('set 2',s2)
s1.difference_update(s2)
print('remove the intersection of set 1',s1)