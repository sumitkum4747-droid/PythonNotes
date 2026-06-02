friends=['pratyush','Sumant','Aashish','Kishant']
print(friends)
print(friends[0])
print(friends[0].title())
# to get the last element simply write the index no.:- [-1] , print(variable_name[-1])
print(friends[-1])
message=f"{friends[0].title()} is my best friend"
print(message)
# manuplating or changing one of the value in List.
friends[0]='PK'
print(friends)
# adding new value to the List by Using "append" command
friends.append('Niraj')
print(friends)
# adding new elements at any position you want using "insert" command
friends.insert(0,'pratyush')
print(friends)
# delete any element you want 
del friends[5]
del friends[0]
print(friends)
# deleting the element using remove('Value')
friends.remove('Kishant')
print(friends)
# removing the element by giving the reason
# 1. firstly we add kishant
# 2. then revome it by giving reason
friends.append('kishant')
not_good='kishant'
friends.remove(not_good)
print(friends)
print(f"{not_good} is not a good freind of mine")