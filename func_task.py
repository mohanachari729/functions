# #Task 1: Add Function
# def add(a,b):
#     return a+b
# obj = add(4,3)
# print(obj)

# #Task 2: Square Function
# def square(x):
#     return x**2
# obj = square(5)
# print(obj)

# # Task 3: Factorial Function
# import math
# print(math.factorial(4))

# #Task 3: Factorial Function
# def factorial(n):
#     return n*(n-1)
# obj = factorial(2)
# print(obj)

# #Task 4: Maximum Function
# list = [1,3,5,76,8,9]
# print(max(list))

# # Task 5: Reverse Function
# def reverse(list):
#     return list[ : : -1]
# list = [1,2,3,4,5]
# reverse = reverse(list)
# print(reverse)

# # Task 6: Check Prime Function
# def is_prime(n):
#     for i in range(2 , n):
#         if not(n%i):
#             return False
#     return True
# for n in range(1 , 20):
#     if is_prime(n):
#         print(n)

# #Task 7: Fibonacci Function
# def Fibonacci(n):
#     if n <=1 :
#         return n
#     else :
#         return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(23)) 

# # Task 8: Palindrome Function
# def isPalindrome(n):
#     return n == n[: : -1]
# print(isPalindrome('dad'))
# print(isPalindrome('mom'))

# #Task 9: Sum of Squares Function
# n = int(input('n:'))
# def sum_square(n):
#     sum =0
#     for i in range(1,n+1):
#         sum=sum+(i+i)
#     print(sum)
# sum_square(n)

# Task 10: Average Function
def Average(numbers):
    return sum(numbers)/len(numbers)
numbers = [1,2,3,4,5]
obj = Average(numbers)
print(obj)

    
