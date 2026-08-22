# def emp(**data):
#     for i in data.items():
#         print(type(i))
# emp(id=101,name='sanika',age='21',add='Satara')

# def emp(**data):
#     for i in data.items():
#         print(i)
# emp(id=101,name='sanika',age='21',add='Satara')


def emp(**data):
    for key,val in data.items():
        print(key,':',val)
emp(id=101,name='Sanika',age='21',add='Satara')