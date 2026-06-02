def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

print(sum(int(input('Enter the Number :'))))


def printer(list,n):
    if n < 1:
        return
    else:
        print(list[n-1])
        return printer(list,n-1)

names=['Sumit','Pratyush','Sumant','Aashish','Chandu']
printer(names,len(names))