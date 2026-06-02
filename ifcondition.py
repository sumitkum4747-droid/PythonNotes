names=['Chandan','Mandan','Chandu','Fandu','Gogoi']
for name in names:
    if name == 'Chandan':   # here you can see that I didn't ignore the case in "Chandan"
        print(name.upper())
    else:
        print(name)

print('Same thing but now the condition is notEqual to')

names=['Chandan','Mandan','Chandu','Fandu','Gogoi']
for name in names:
    if name != 'Chandan':   # here you can see that I didn't ignore the case in "Chandan"
        print(name.upper())
    else:
        print(name)

# checking whether the element is in the list or not
print('Chandan' in names)   # answer will be True
print('Sumit' in names)     # answer will be False

# checking whether the element is not in a list
banned_names=['andrew', 'carolina', 'david']
user='marie'
if user not in banned_names:     # this checks or make sure that the user is not in list 
    print(f"{user.title()} can post letter officially")


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age_0=25
age_1=43
if age_0 >= 20 and age_1 >= 25:
    print('You are alligible to make the document verify')
