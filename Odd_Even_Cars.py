#Check if the sum of even digits is divisible by 4 and sum of odd digits is divisible by 3, to determine if a car in Delhi (numbered N) can run on Sunday 

#ODD-EVEN Car Numbers

N = int(input("Enter the number of inputs: "))
Inputs_of_Car_Numbers = [] # Initialize an empty list to store the inputs
for i in range(N): # Use a loop to take input for the specified number of times
    user_input = (int)(input(f"Enter input {i + 1}: "))
    Inputs_of_Car_Numbers.append(user_input)
    
for user_input in Inputs_of_Car_Numbers:
    even_sum = 0 #Initialised to avoid accumulation/errors
    odd_sum = 0 #also it is base-case, i.e won't affect calculations
    while user_input > 0:
        d = user_input%10
        if d%2 == 0:
            even_sum = even_sum + d 
        else:
            odd_sum = odd_sum + d
        user_input = user_input//10
        
    if (even_sum % 6 == 0) and (odd_sum % 3 == 0):
        print("Yes")
    else:    
        print("No") 