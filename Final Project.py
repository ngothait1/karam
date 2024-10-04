#Final Project
import time

print("Hello, This is my final project")
user = input("What is your name? ") #user name input
print("Hi " + user + ", nice to meet you" )  #appreciate comment to user
print("This is a special calculator, I would need two numbers from you")  #define comment to user'this is a calculator
first_num = int(input("First number: "))  #first number input by user
second_num = int(input("Second number: "))  #second number input by user
print("Thank you for putting in your numbers, " + str(first_num) + " " + "and " + str(second_num)) #output for chosen two numbers
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
print("I can see that the first number is " + str_num1 + " And the second is " + str_num2)    #output types of two numbers(even or odd)     
if is_even_1 != is_even_2:
    print("So one of them is " + str_num1 + ", and one is " + str_num2)
else:
    if is_even_1 == is_even_2 :
        print("So both of them are " + str_num1)
operator = input("Operator (+, -, *, /): ")     # input for operator type by user
if (operator !=  "/") and (operator != "+") and (operator != "-") and (operator != "*") : 
    print("Error: Operator " + operator + " is not supported")  #error comment if chosed a wrong operator
    print("An error had occured, please try again")
else:
    if operator == "/" :
       str_div = input("You chose division, should the result be integer? (y/n) ")  #input integer or float result if choosed division operator by user
       if str_div == "y" :
           result = first_num // second_num
       else :
           result = first_num / second_num 
    elif operator == "+" :
        result = first_num + second_num  # if th user input is + the result is sum two numbers
    elif operator == "-" :
        result = first_num - second_num  # if th user input is - the result is abstract two numbers
    elif operator == "*" :
        result = first_num * second_num  # if th user input is * the result is multiply  two numbers
    print(str(first_num) + " " + operator + " " + str(second_num) + " = " + str(result))  #output the caclulation result
print("Thank you " + user + " for using the calculator on  " + str(time.ctime()))  #output thanks,time and date for using


