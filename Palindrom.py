
print('program begun')
x = input()
x = x.casefold()
y = reversed(x)
print(x)
print(y)
if list(x) == list(y): 
     print('Yes ! The given String is a Palindrome')
else:
     print('Nope ! It is not a Plindrome')