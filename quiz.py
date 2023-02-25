def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)



def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)

x = 0
for i in range(3):
    x = x + i
print(x)    