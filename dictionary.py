alien_0={'color':'green','point':5}
print(alien_0['color'])
print(alien_0['point'])

# adding new key-value pairs in ictionary
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

# modifying the value in the list
print(f"The color of alien is {alien_0['color']}")
alien_0['color']='yellow'
print(f"The color of alien is now {alien_0['color']}")

# working with dictionary
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'Original position : {alien_0['x_position']}')
if alien_0['speed'] == 'slow':
    x_increment=1
elif alien_0['speed'] == 'medium':
    x_increment=2
else:
    x_increment=3
    # This must be fast alien
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0)

# deleting Key-Value from the dictionary
del alien_0['y_position']
print(alien_0)

# Using "get()" to call the Key which doesn't exist (by using we didn't get error even the Key is not available in
# the dictionary)
print(alien_0.get('points'))

# And if we directly call by using bracket "[]" it will give error
#print(alien_0['points'])

# so if you are not sure that the Key you are calling is in list or not at that time you should use get to not get
# error in your code.


# looping in dictionary
favourite_language={
    'jen': 'pyhton',
    'sarah': 'c',
    'edward':'rust',
    'phil':'python'
}
for name,language in favourite_language.items():
    print(f"{name.title()}'s favourite language is {language.title()}")


# Looping Through All the Keys in a Dictionary
for name in favourite_language.keys(): # you can also write -> "for name in favourite_language" because it is default behaviour of python for loop
    print(name.title())


friends=['phil','sarah']
for name in favourite_language.keys():
    print(f"Hi {name.title()}")
    if name in friends:
     language=favourite_language[name].title()
     print(f"{name.title()}'s favourite language is {language}")

if 'erin' not in favourite_language.keys():
    print('Erin take the poll')


# using sorted in dictionary
for name in sorted(favourite_language.keys()):
    print(f"{name.title()} thank you for taking Poll")




#Looping Through All Values in a Dictionary
print('The following language have been mentioned')
for language in favourite_language.values():
    print(language.title())

# in previous loop of values repeated values are there to trim that we use set()
print('The following language have been mentioned')
for language in set(favourite_language.values()):
    print(language.title())
