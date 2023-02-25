nums =[4, -11, 69, 53, -65]
doubled =[]# a new variable is created 
#for every item/num in nums array
for num in nums:
    #append means put new items in a list     
    doubled.append(num*2)

print(doubled)

#list comprehension new_list =[<expression> for <element> in <collection>]

quad = [num*4 for num in nums]
print(quad)