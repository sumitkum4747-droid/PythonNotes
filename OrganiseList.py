friends=['Pratyush','Sumant','Aashish','Kishant']
print(friends)

# sorting the List of Words
friends.sort()
print(friends)
number=[4,3,7,8,2]

# sorting the List of Numbers 
print(number)
number.sort()
print(number)

# reverse sorting

cars=['toyota','suzuki','mitshubushi','bmw','ford','mercedeze']
cars.sort(reverse=True)
print(cars)

# temporary sorting using sorted()
names=['madan','kundan','chagan','pappu','aditya']

# -> If you take one word Madan here M is capital and in rest of the word starting letter are so during sorting
#    python keeps Madan with capital first letter at first.

print(sorted(names))
print('not changed the value permanently it only changes it temporarly original list\nis still same')
print(names)

# finding length of the list

letters=['a','b','c','d','e','f','g']
print(len(letters))
# output should be 6