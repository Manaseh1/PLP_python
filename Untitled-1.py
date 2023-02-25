#Ask user and year of service for salary
print('Hello, Please enter your salary')
salary=int(input("salary: "))
print('Please enter your years of service')
serv = int(input())
#5% increase
if(serv >= 5):
    net = 105/100 *salary 
    print("Hello your new net bonusis:",net)
else:
    print("You are not qualified for increase")
x ={}    
x[2] =10
x[1] =[20,30,40]
print[x[1][2]]