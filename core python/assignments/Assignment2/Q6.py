# WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.
# take input
basic=int(input("Enter basic salary :"))
#perfrom operation
da=basic*10/100
ta=basic*12/100
hra=basic*15/100
total_salary=basic+da+ta+hra
print(f'total_salary of employee is :{total_salary} and basic salary is :{basic} and da is :{da} and ta is:{ta}and hra is :{hra}')