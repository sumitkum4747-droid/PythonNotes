def factorial(number,fact=1):
    fact=fact*number
    if number-1 == 1:
        print(fact)
        return fact
    else:
        factorial(number-1,fact) # now value of fact will not be One it will be value which after multiplying by number
# calling function
factorial(int(input('Enter the Number :')))
print('Your work is complete')
# this code fails when input is 1 or zero and it is little bit complex




# Simple way to write it
def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(int(input('Enter the Number :'))))