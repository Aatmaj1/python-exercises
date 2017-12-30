#!/usr/bin/python
#commad line-> calculator --op add 1 2 
import click

@click.command()
@click.option('--op', nargs=3, type=click.Tuple([unicode, int, int]))

def cal(op):
    choice =op[0]
    num1 = op[1]
    num2 = op[2]
 
    if choice == 'add':
        print(num1,"+",num2,"=", add(num1,num2))
 
    elif choice == 'sub':
        print(num1,"-",num2,"=",subtract(num1,num2))  
 
    elif choice == 'mul':
        print(num1,"*",num2,"=", multiply(num1,num2))
 
    elif choice == 'div':
        print(num1,"/",num2,"=", divide(num1,num2))
    else:
        print("Invalid input")

def add(x, y):
   return x + y
 
def subtract(x, y):
   return x - y
 
def multiply(x, y):
   return x * y
 
def divide(x, y):
   return x / y
 

if __name__ == '__main__':
    cal()

