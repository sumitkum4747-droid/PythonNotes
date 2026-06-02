squares=[]
for value in range(1,6):
    square=value**2
    squares.append(square)

print(squares)

# simple way to do this
squares=[]
for value in range(1,6):
    squares.append(value**2)

print(squares) 

# more simple way to do this
squares=[value**2 for value in range(1,6)]
print(squares)