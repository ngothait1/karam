# Final Project
import time

print("Hello, This is my final project")
user = input("What is your name? ")
print("Hi " + user + ", nice to meet you" )  
print("This is a special calculator, I would need two numbers from you")  
first_num = int(input("First number: "))  # first number input by user
second_num = int(input("Second number: "))  # second number input by user
print("Thank you for putting in your numbers, " + str(first_num) + " " + "and " + str(second_num)) 
is_even_1 = first_num % 2 == 0  #check if first number is even ?
is_even_2 = second_num % 2 == 0 #check if second number is even ?
if is_even_1 :
   str_num1 = "even"
else :
    str_num1 = "odd"
if is_even_2 :
   str_num2 = "even"
else :
    str_num2 = "odd"
print("I can see that the first number is " + str_num1 + " And the second is " + str_num2)        
if is_even_1 != is_even_2:
    print("So one of them is " + str_num1 + ", and one is " + str_num2)
else:
    print("So both of them are " + str_num1)
operator = input("Operator (+, -, *, /): ")     # input for operator type by user


if operator == "/" :
       str_div = input("You chose division, should the result be integer? (y/n) ")  
       if str_div == "y" and second_num != 0 :
           result = first_num // second_num
       elif str_div == "n" and second_num != 0 :
           result = first_num / second_num 
       else:
            print("Error: num_2 is zero")
            print("An error had occured, please try again")    
elif operator == "+" :
        result = first_num + second_num  
elif operator == "-" :
        result = first_num - second_num  
elif operator == "*" :
        result = first_num * second_num  
print(str(first_num) + " " + operator + " " + str(second_num) + " = " + str(result))
    
else:
    print("Error: Operator " + operator + " is not supported")  #error comment if chosed a wrong operator
    print("An error had occured, please try again")

print("Thank you " + user + " for using the calculator on  " + str(time.ctime()))
 
