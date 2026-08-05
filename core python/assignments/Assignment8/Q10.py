# Q10 Wap check if enterd year is leap year or not
def checkYear(year):
    if(year%400==0 or year%4==0 and year%100!=0):
        return 'Leap Year'
    else:
        return 'Not Leap Year'
year=int(input("Enter Year :"))
res=checkYear(year)
print(res)