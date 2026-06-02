# function for length calculation of list
def len_calc(demo):
    print(len(demo))
    return len(demo)
# calling the function
list=['Sumit','Sumant','Pratyush','Aashish','Chandu']
len_calc(list)

# function for printing all the elements of the list in one line
def list_print(object):
    lenght=len(object)
    for no in object:
        print(no,end=" ")
# calling the function
list_print(list)
print("\n")

# function for factorial of 'n'
def factorial(number):
    fact=1
    for no in range(1,number+1):
        fact=fact*no
    print(fact)
    return fact
# calling the function
factorial(5)

# function for converting currency
def us_ind(amount):
    amount_in_INR=amount*92
    print(amount_in_INR)
    return amount_in_INR
# calling the function
us_ind(float(input("Entre the amount :")))

# function for odd/even
def odd_even(nos):
    if nos%2 == 0:
        result='EVEN'
        print(result)
    else:
        result='ODD'
        print(result)
    return result
# calling the function
odd_even(int(input('Enter the Number :')))