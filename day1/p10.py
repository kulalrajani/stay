# Program to check if a number is prime or not

num = int(input("Enter a number to check if a number is prime or not : "))
flag = 1
for i in range(2,(num//2)+1):
    if num % i == 0:
        flag = 0
        break

if flag == 1:
    print(num," is prime number")
else:
    print(num," is not a prime number")
