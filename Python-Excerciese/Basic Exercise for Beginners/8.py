# Excercise 8: Write a program that will check whether the number is armstrong number or not.
# An Armstrong number is one whose sum of digits raised to the power three equals the number itself.
# 371, for example, is an Armstrong number because 3**3 + 7**3 + 1**3 = 371.

n=int(input("Enter three digit number:\n> "))
a=n%10
 #3
num=n//10
 #12
b=num%10
 #2
c=num//10
 #1
if (a**3 + b**3 + c**3)==n:
    print("\nThe number is armstrong number")
else:
    print("\nThe number is not armstrong number")
