aliens=[]
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'low'}
    aliens.append(new_alien)
for alien in aliens[0:5]:
    print(alien)
print(f'There are {len(aliens)} aliens in the list')