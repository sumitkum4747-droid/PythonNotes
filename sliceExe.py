names=['Chandu','Mandal','Mahto','Nandan','Mandan']
print('The First three elements of list are :')
print(names[0:3])
print('The Three elements from the middle of the list are :')
print(names[1:4])
print('The Last three elements of the list are:')
print(names[-3:])
friend_names=names[:]
names.append('Madan')
friend_names.append('Chadan')
print(names)
print(friend_names)
