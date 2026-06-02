players=['Virat','Dhoni','Rohit','Jaiswal','Ruturaj']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[-3:])
print(players)
# after printing the players we can see that list is not permanently sliced

# looping through a slice
print('Here are the first three players')
for player in players[:3]:
    print(player.title())

# copying the list
my_food=['Rasmalai','Gulabjamun','Kachori','Jalebi','Barfi']
friend_food=my_food[:]
print(friend_food)
friend_food=my_food[0:4]
print(friend_food)

# if someone want to copy this way
friend_food=my_food
# then both list represent to same list which means that we add any value to one list it will also appear in another list
my_food.append('Chola bhatura')
print(my_food)
print(friend_food)