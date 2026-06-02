def findMedianSortedArrays(num1,num2):
    f_num=[]
    for no in num1:
        f_num.append(no)
    for no in num2:
        f_num.append(no)
    f_num.sort()
    length=len(f_num)
    if length % 2 != 0:
        n=int((length+1)/2)
        print(f_num[n-1])
    else:
        n=int(length/2)
        s=(f_num[n-1] + f_num[n])/2
        print(s)

list1=[]
n1=int(input('Enter the Size of the List :'))
for no in range(0,n1):
    list1.append(int(input('Enter the Number :')))
list2=[]
n2=int(input('Enter the Size of the List :'))
for no in range(0,n2):
    list2.append(int(input('Enter the NUmber :')))
findMedianSortedArrays(list1,list2)