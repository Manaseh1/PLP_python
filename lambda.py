# Lambda function is a special type of function without a name.That is why it's referred to as an anonymous function.
#They can be assigned to variables
yes = lambda:print('Yes')
yes()

#Also accept arguements
# sq = lambda num :num**2
# num =int(input('num:'))
# print("Square of num is :",sq(num))


def ispalindrome(word):
    if(word == word[::-1]):
        return "A palindrome"
    else:
        return "Not a palindrome"

#word =input("Enter word:")
#print(ispalindrome(word))    

#palindrome in lambda

palin =lambda word:"Palindrome" if word == word[::-1] else "not palindrome."
word = input("Enter the word: ")
print(palin(word))
 