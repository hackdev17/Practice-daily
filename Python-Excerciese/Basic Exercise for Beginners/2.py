# Exercise 2: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

n=input("Enter the number:\n> ")
y=n[::-1]
k=" ".join(y)
print(k)
