for value in range(1,21):
    print(value)
    
#numbers=[value for value in range(1,1000001)]
#for no in range(1,1000000):
 #   print(numbers[no])
#print('counting is Ended')

numbers=[value for value in range(1,1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers=[value for value in range(1,1000001,2)]
for no in range(0,500000):
    print(odd_numbers[no])
print('All odd numbers are counted')


multiple_3=[value*3 for value in range(1,11)]
for no in range(0,10):
    print(multiple_3[no])
print('All the multiple of 3 are printed')

cubes=[value**3 for value in range(1,11)]
for no in range(0,10):
       print(cubes[no])
print('All the cubes upto 10 are printed')


cubes=list(value**3 for value in range(1,11))
print(cubes)