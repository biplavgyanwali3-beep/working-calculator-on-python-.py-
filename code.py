#python program to create a simple calculator

#to build calculator program 
# functions for operations 
#user input 
#print result 

# functions to add two numbers D
def add(num1,num2):
 return (num1 + num2)

# functions to substract two numbers 
def sub(num1,num2):
  return num1 - num2

# functions to multiply two numbers 
def multiply (num1,num2):
 return (num1 * num2)

# functions to divide two numbers 
def divide (num1,num2):
 return (num1 / num2)


# functions to divide two numbers 
def Avg (num1,num2):
 return (num1 + num2)/2

#user input 
print("please select operator: \n " \
      "1. Addition \n " \
        "2. Substraction \n" \
            "3. multiplication \n" \
                "4.Division \n"  \
                "5.Average\n")
                  
select = int(input ("select a operation from 1,2,3,4,5 : "))

number1 = int(input("enter first number : "))
number2 = int(input("enter second number: "))

if select == 1:
    print(number1, "+", number2, "=", add(number1, number2))

if select == 2:
    print(number1, "-", number2, "=", sub(number1, number2))


if select == 3:
    print(number1, "*", number2, "=", multiply(number1, number2))

if select == 4:
    print(number1, "/", number2, "=", divide(number1, number2))

if select == 5:
    print("(",number1, "+", number2,")", "/", "2", "=", \
 average (number1, number2)) 
else:
 print("Invalid operation pls select again ")




