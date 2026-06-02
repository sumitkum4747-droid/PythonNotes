ini_1=0
ini_2=1
end_no=int(input("Enter the number no. terms you want :"))
#"end_no=int(end_no)"" you can do this also if you forgot put to write int before taking input 
for no in range(0,end_no):
    no_term=ini_1 + ini_2
    print(f"{no_term} ")
    ini_1=ini_2
    ini_2=no_term
print(f'Fibbonaci series is ended upto {end_no}th term' )