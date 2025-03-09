# #sample function
# def sample():
#     print("hello python life")
# sample()

# #addition function
# def add():
#     num1=10
#     num2=20
#     result = num1 + num2
#     print(f"the num1 is {num1} and num2 is  {num2} performing the addition operation the result is {result}")
# add()

# #user detailes
# def details():
#     user = "mohan"
#     dept = "python"
#     print(f"the user is {user} in the department of {dept}")
# details()

# #multiplications
# def mul():
#     num1 = 10
#     num2 = 10
#     print(f"the num1 is {num1}and num2 is {num2} and performimg multiplication the resultant is {num1*num2}")
# mul()

# #multiplication
# def mul(num1 , num2):
#     result = num1*num2
#     print(result)
# mul(1,2)
# mul(20 , 30)

# #orbitary argument
# def my_self(*a):
#     print(a)
# my_self("mohan" , 12 ,234 , 1234)

# #keyword argument
# def my_self(**a):
#     print(a)
# my_self(a = 1 , b = 2 , c = 3)

# #return statement using addition
# def add(a ,b):
#     return a+b
# obj = add(4 , 5)
# print(obj)

# #return statement using multiplication
# def mul(a , b , c):
#     return a*b*c
# obj = mul(1 , 2 , 3)
# print(obj)

# #default parameters
# def my_self(name , age = None , dept = None):
#     return name , age , dept
# print(my_self('mohan',22 ,'python'))
# print(my_self("mohan"))

# # #default parameters in addition 
# def add(num1 , num2 , num3= 0):
#     return num1+num2+num3
# print(add(1 , 2 , 3))
# print(add(1 ,2))

# #power function
# def power(base , exponential = 2):
#     return base**exponential
# print(power(2,3))
# print(power(2))

# #calculations
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def expo(a,b):
#     return a**b
# print(add(2,4))
# print(sub(2,4))
# print(mul(2,4))
# print(expo(2,4))

# #balance crediting
# balance = 1000
# def credited(amount):
#     global balance
#     balance += amount
#     print(balance)
# credited(200)
# print(balance)

#math function in built in modules
import math
print(math.cos(45))











