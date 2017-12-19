#! /usr/bin/python

import sys

def add(x, y):
   return x + y
 
def subtract(x, y):
   return x - y
 
def multiply(x, y):
   return x * y
 
def divide(x, y):
   return x / y
 
try:
	choice =sys.argv[1]
	num1 = int(sys.argv[2])
	num2 = int(sys.argv[3])		
except IndexError:
	print("Invalid Input")
	print("Proper Sequence :")
	print("-> calculator.py operation no.1 no.2")
	exit(0)
	
if choice == 'add':
   print(num1,"+",num2,"=", add(num1,num2))
 
elif choice == 'subtract':
   print("num1","-","num2","=",subtract(num1,num2))  
 
elif choice == 'multiply':
   print(num1,"*",num2,"=", multiply(num1,num2))
 
elif choice == 'divide':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")

