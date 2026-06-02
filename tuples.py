dimensions=(43,77)
print(dimensions[0])
print(dimensions[1])
#dimensions[0]=200     # which will show error because in python we can't change the value of tupple
# but we can rewrite the whole value of the the dimension
dimensions=(40,70)
# using loop to print the value of the dimension
print('After changing the value of the tuple-dimension printing it by using the for loop :')
for dimension in dimensions:
    print(dimension)