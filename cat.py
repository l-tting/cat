#(A) Suppose a, b and c are integer variables assigned the value a =8, b=3 and c= 5. 
# Write a python program to determine the value for the expression.  a*(c%b)+c                      
# a = 8;
# b = 3;
# c = 5;
# result = a * (c%b) + c;
# print(result);

# (B)In a scientific application the function f(t) is computed as follows                                [3 marks]   
#                 f (t) =  -3t2+5      if t>=0
#                            -3t2-5         if t<0                                                                          
# Write a python program to input t through the keyboard and then compute and output f (t). 

# t = int(input("Enter t: "))
# if t >= 0:
#     ft= -3*t**2 +5
# else:
#     ft = -3*t**2 -5
# print(ft)


# (C) Assume a float – type variable m has a value 5, while another float-type variable n has a value 3.
#  Assume you want to write statements to output the sum of m and n using the format shown below.
# Using Python programming language ,write down appropriate statements 
# in each case that will out the sum as shown below.
# The sum of 5.0 and 3.0 is 8.0.                                                                          [2 marks]
m = float(5)
n = float(3)
sum = m + n
print(f"The sum of {m} and {n} is {sum}")

# 8.0 is the sum of 5.0 and 3 .0                                                                           [2 marks]
print(f"{sum} is the sum of {m} and {n}")


# (D)Question Two                                                                                 
# Consider a used car yard in downtown Nairobi called Olemuya car sales that needs to
# store details of vehicles they have in stock. 
# For each vehicle they need to store the following;
# Registration number(string) 	    Make (string)
# Distance traveled in Km(int)	    Buying Price in Kshs (float)
# Selling Price in Kshs	 (float)	               Name of previous owner(string)
# Required:
# Write a python program  to  perform the following actions:
# Insert a new vehicle record into the database                                  [4 marks] 
# Registration_number = input("Enter registration number: ")
# Make = input("Enter make: ")
# Name_of_previous_owner = input("Enter name of previous owner: ")
# Distance_travelled = int(input("Enter distance travelled in km: "))
# Buying_price = float(input("Enter buying price: "))
# Selling_price = float(input("Enter selling price: "))

# Computes the profit (if any) and display “You made a profit of Kshs. xxxx”, if no profit, the program should display, 
# “You  made a loss of Kshs. xxxx” 
#                                                                          [4 marks]
# profit = Selling_price - Buying_price
# if profit > 0:
#     result = f'You made a profit of Ksh. {profit}'
# else:
#     result = f'You made a loss of Ksh. {profit}'

# # Display all the details of the  new vehicle including
# # whether a profit was made or not                                                                                    [4 marks]
# print("OLEMUYA CAR SALES")
# print("____________________")
# print(f"The registration number: {Registration_number}")
# print(f'The car make is: {Make}')
# print(f"The name of the previous owner is {Name_of_previous_owner}")
# print(f"The distance travelled by the car in km: {Distance_travelled}")
# print(f"Car buying price: {Buying_price}")
# print(f"Car selling price: {Selling_price}")
# print(result)


# Question Three
# Assume that you have been appointed consultant with MICUSA Cooperative Bank. Most of the operations are manual.
#  The management would like to automate the operations. At the moment, the management knows very little about 
#  the power of Python. 
# The management would like a program that can be used to input the following details:
# Employees names(string)
# Personnel number(int)
# Department(string)
# Basic salary(float)
# House allowance(float)
# Required:
# Write the appropriate python program  to input and output the details of an employee. 
# The output should include all the details of an employee, the gross salary (basic salary + house allowance) , 
# tax to pay (30% of the gross salary) and net salary (gross pay - tax)	  	     [8 marks]

Employee_names = input("Enter employee names: ")
Personnel_number = int(input("Enter personnel number: "))
Department = input("Enter department: ")
Basic_salary = float(input("Enter basic salary: "))
House_allowance = float(input("Enter house allowance: "))

gross_salary = Basic_salary + House_allowance
tax = 0.3 * gross_salary
net_salary = gross_salary - tax

print("MICUSA Cooperative Bank ")
print('Employee Details')
print("__________________________________________")
print(f"Employee name: {Employee_names}")
print(f"Personnel number: {Personnel_number}")
print(f"Department: {Department}")
print(f"Basic salary is KSH: {Basic_salary}")
print(f"House allowance is KSH: {House_allowance}")
print(f"Gross salary is KSH: {gross_salary}")
print(f"Tax paid is KSH: {tax}")
print(f"Employee net salary: KSH.{net_salary}")

