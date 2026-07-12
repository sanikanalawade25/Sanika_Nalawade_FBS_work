# 11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
#take input
amount=int(input("Enter amount:"))
#perfrom operation
notes_500=amount//500
amount=amount%500
notes_100=amount//100
amount=amount%100
notes_50=amount//50
amount=amount%50
notes_20=amount//20
amount=amount%20
notes_10=amount//10
amount=amount%10
notes_5=amount//5
amount=amount%5
notes_2=amount//2
amount=amount%2
notes_1=amount

print(notes_500)
print(notes_100)
print(notes_50)
print(notes_20)
print(notes_10)
print(notes_5)
print(notes_2)
print(notes_1)