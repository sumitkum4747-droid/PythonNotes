def addTwoNumbers(l1,l2):
    f_list=[]
    lengthl1=len(l1)
    lengthl2=len(l2)
    sum1=0
    sum2=0
    for no in range(0,lengthl1):
        sum1= sum1+(l1[no] * (10**no))
    for no in range(0,lengthl2):
        sum2= sum2+(l2[no] * (10**no))
    sum=sum1+sum2
    print(sum)
    def final(s):
        x=s%10
        f_list.append(x)
        if x == s:
            return
        else:
            vari=s-x
            s =int(vari/10)
            return final(s)
    final(sum)
    print(f_list)

n1=int(input('Enter the Size of first list :'))
list1=[]
for no in range(0,n1):
    list1.append(int(input('Enter the Number :')))
n2=int(input('Enter the size of Second list :'))
list2=[]
for no in range(0,n2):
    list2.append(int(input('Enter the Number :')))

addTwoNumbers(list1,list2)