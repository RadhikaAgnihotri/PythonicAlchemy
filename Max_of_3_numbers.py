def max(num1,num2,num3):  #function max takes 3 input as num1,num2,num3
    if num1>num2 and num1>num3: 
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
    
num1 = (int)(input("Enter the first number"))   #taking input from the user
num2 = (int)(input("Enter the second number"))    
num3 = (int)(input("Enter the third number"))
Largest = max(num1,num2,num3) #calling the max function and passing the user inputs
print(Largest, "is the maximum of the three numbers")  #prints the output 