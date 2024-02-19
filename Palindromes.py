#Palindrome Number

number = (int)(input("Enter a number :"))
duplicate = number #so that the original number is saved for comparison later, and its copy can be used for performing digit extraction and reversing
reversed_number = 0 
while number!=0:
    d = number % 10
    reversed_number = reversed_number * 10 + d
    number = number // 10
if(reversed_number == duplicate):
    print("Yes the number", duplicate, "is a palindrome!") #using duplicate, since number = 0 due to while loop operations
else:
    print("No the number", duplicate, "is not a palindrome!")
    
#Palindrome String

string = input(("Enter a string :"))
if(string == string[::-1]):
    print("The string is a palindrome")
else:
    print("Not a palindrome")  
    
