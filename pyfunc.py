# functions are blocks of code which are executed when called 
def myname():
    print('Manaseh njoroge')
myname()
#adding
#a and b are local scope 
def adding(a,b):
    add = a + b
    return add
#what ever is inside the brackets after function call is an arguement
sum = adding(12,23)

print("Total :",sum)
#  Arbitrary arguements = number of arguement is unknown
def adder(*nums):
    summ = 0
    for num in nums:
        summ +=num
    return summ
print("Total:", adder(2,3,4,5,7,10))
# Arbitrary Keyword Arguements 
def add_ages(**ages):
    sum = 0 
    for k,v in ages.items():
        sum+= v
    return sum
print("Total:",add_ages(me =23,fill=22,din=21))

#Enclosing scope refers to a function inside another function or what is commonly called a nested function 
v = 'mbuthia'
def name1():
    s='Manaseh'
    def names12():
        t= 'Njoroge'
        u = print(t +' '+' '+s+' '+v)
        return u
    return names12()
name1()