num_input = int(input("Enter Number to find sum of all numbers from 1 to it (n): "))
#Set start of sum of numbers to 0
sum = 0

#The Math way to solve this problem, starts here
ans = num_input*(num_input+1)/2
print("Quick Sum of all the numbers between 1 and your input is: ",ans)

#The Slow less intelegent programmer way to solve this problem, starts here
if num_input <= 0: 
   print("{!} INVALID INPUT. Enter a positive number.") 
else: 
   while num_input > 0:
        sum = sum + num_input
        num_input = num_input - 1;

print("Slow Sum of all the numbers between 1 and your input is: ", sum)
