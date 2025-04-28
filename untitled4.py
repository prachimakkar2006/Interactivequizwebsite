
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")

# lst = (20 ,20, 30)
# print (lst)

# list=[]
# print(type(list))
# print(list)

# x=(1,2,3,4,5,)
# z=x
# y=x
# print(id(x))
# print(id(y))
# print(id(z))

# x=[1,2,3,4]
# y=[5,6]
# x.append(y)
# print(x)

# x=[1,2,3,4]
# y=[5,6]
# x.extend(y)
# print(x)

# lst=[1,2,3,4]
# lst[2]=5
# print(lst)

# lst=[1,2,3,4]
# del lst[1]
# print(lst)
 

# c_height=[3,4,7,9]
# x=max(c_height)
# print(x)


# c_height=[3,4,7,9]
# x=max(c_height)

# count=0
# for i in c_height:
#     if i== x:
#         count+=1
# print(count)

# age = int(input)
# c_height=[]

# for i in range(age):
#     x=int(input)
#     c_height.append(x)

# x=max(c_height)
# count=0
# for i in c_height:
#     if i==x:
#         count+=1
# print(count)

# l=[1,2,3,4,]
# #identify index
# #position using item
# l.index(2)

# l=[1,2,3,4,5,6,7,8,9]     
# print(l[3:-1])
# print(l[-4:-5])


# l=[1,2,3,4,5,6,7,8,9] 
# print(l[-3:-5])
# print(l[-2:-1])          


# l=[2,4,7,32,6,255,5,42]
# l.reverse()
# print(l)

# l=[1]
# l1=l*3
# print(l)

# l=[2,3,4,5,2,2,3,223,2,323,23,23,2,3233,2]
# print(l.count(2))

# l=[1,3,67,45,98,3,5,7]
# l.sort()
# print(l)

# l=[1,2,5,7,8,96,5,4,3,7,8,55,75,656,46,5,6]
# x=sorted(l)
# print(x)

# l=['apple','banana','cherry']
# l[1:2]=['blackcurrent','watermelon']
# print(l)

# write a code to swap the numbers with temporary variable
# x = 5
# y = 10

# r=x
# x=y
# y=r
# print("x=",x)
# print("y=",y)

# write a code to swap the numbers without temporary variable
# x=5
# y=10

# x,y=y,x
# print("x=",x)
# print("y=",y)

# from functools import reduce
# li=[5,8,90,45,83,29,45]
# sum = reduce((lambda x,y:x+y),li)
# print(sum)

# age=int(input())
# c_height= list(map(int,input().split)[:age])
# print(c_height)
# x=max(c_height)
# print(c_height.count(x))

# def mul(i):
#     return i*i
# l={3,5,7,9,6}
# x=map(mul,l)
# y=list(x)

# print(x)
# print(y)

# l={"apple","banana","cherry"}
# print(id(l))

# x=list(l)

# print(x)
# print(id(x))

# l=[1,2,4,6,7,5]
# list=[l*2 for l in l]
# print(list)

 
# fruits=["apple","pear","plum"]
# list=[fruits for fruits in fruits if 'a'in fruits]
# print(list)

# list=[1,2,3,4,5,7,8,9]
# l=[list*5 for list in list]
# print (l)
 
# x="abc"
# for x in range (3,0,-2):
#     print (x,end="")
# print()



# m={"a","b","c","d","f","g"}
# m.add("h")
# print(m)


# m={"a","b","c","d","f","g"}
# m.update("h","r","t")
# print(m)


# m={"a","b","c","d","f","g"}
# m.remove("c")
# print(m)


# m={"a","b","c","d","f","g"}
# m.pop()
# print(m)


# m={"a","b","c","d","f","g"}
# n={1,2,3,4,5,7,8,9}
# print(m|n)

# x="prachi"
# print(x.upper())
# print(help(str.upper))


# a={1,2,3,4,5,6,7,8,9}
# b={4,5,7,8,9}
# print(a^b)


# a=str(input("enter your name:"))
# print("length of your name",len(a))


# str="my  ame is $ and my hobby is $."
# print(str.count("$"))


# def even_odd(n):
#     x = int(n)
#     if(x %2 == 0):
#             print("The number is even")
#     else:
#             print("The number is odd")
# n = input()
# if n.isdigit():
#     even_odd(n)
# elif n[0] == "-" and n[1:].isdigit():
#     even_odd(n)
# else:
#     print("Invalid Input")


# list={"Chitkara","university","Punjab"}
# x = lambda lst: ", ".join(lst)
# output = x(list)
# print(output)



# a = int (input("enter the no."))
# b = int (input("enter the no."))
# c = a*b/2
# print("Area of triangle",c)
# print(type(c))


# a = 1,2,3
# print(type(a))


# a = [1,2,3,4,5,5,6,7,5,4,3,5,6,4,3,5,6,4]
# s = a.count(5)
# print(s)


# n = int(input("Enter the no."))
# if n % 2==0:
#     print("the no. is Even")
# elif n % 2!=0:
#     print("the no. is odd")



# # Function to check if the number is an Armstrong number
# def is_armstrong(number):
#     # Convert the number to a string to find the number of digits
#     num_str = str(number)
#     num_digits = len(num_str)
    
#     # Calculate the sum of each digit raised to the power of the number of digits
#     sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
#     # Check if the sum is equal to the original number
#     if sum_of_powers == number:
#         return True
#     else:
#         return False

# # Input from the user
# n = int(input("Enter a number: "))

# # Check if the number is an Armstrong number
# if is_armstrong(n):
#     print(f"{n} is an Armstrong number.")
# else:
#     print(f"{n} is not an Armstrong number.")


# i = 1
# while i<6:
#     i += 1
#     if i == 3:
#        continue
#     print(i)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# number = int(input("Enter a number: "))

# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print(f"The factorial of {number} is {factorial(number)}")

    


# # Function to convert Celsius to Fahrenheit
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# # Taking user input for Celsius
# celsius = float(input("Enter temperature in Celsius: "))

# # Converting and printing the temperature in Fahrenheit
# fahrenheit = celsius_to_fahrenheit(celsius)
# print(f"{celsius}°C is equal to {fahrenheit}°F")



# # Function to check if a number is Armstrong
# def is_armstrong(number):
#     # Convert number to string to easily access each digit
#     num_str = str(number)
#     num_digits = len(num_str)
#     sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
#     return sum_of_powers == number

# # Taking user input
# start = int(input("Enter the starting range: "))
# end = int(input("Enter the ending range: "))

# # Printing Armstrong numbers in the given range
# print(f"Armstrong numbers between {start} and {end}:")
# for num in range(start, end + 1):
#     if is_armstrong(num):
#         print(num)


# def print_pyramid(n):
#     for i in range(1, n + 1):
#         # Print leading stars
#         for j in range(n - i):
#             print("*", end="")
        
#         # Print numbers in decreasing order
#         for j in range(i, 0, -1):
#             print(j, end="")
        
#         # Move to the next line after each row
#         print()

# # Example usage: Get the value of n from the user
# n = int(input("Enter the number of rows for the pyramid: "))
# print_pyramid(n)


# n = int(input("enter the number:"))
# for i in range (1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print (j,end="")
#     for j in range(i-1,0,-1):
#         print(j,end="")
#     print()



# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     print()