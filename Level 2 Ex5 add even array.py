#Separate all even and odd numbers in one array into two different arrays. 
# Find the max and min from each array. Do not use any built in functions. 
numbers=[15,14,9,12,15,56,89,84]
even=[]
odd=[]

#store the value in odd and even list
for index in range(0,len(numbers)):
    if(numbers[index]%2==0):
        even.append(numbers[index])
    else:
        odd.append(numbers[index])
        
print("Even number ",even)
print("odd number ",odd)
 
#set the max and minimum value in first index
max_even=min_even=even[0]
max_odd=min_odd=odd[0]

#find the max and mimimum value in even list
for index in range(0,len(even)):
    if(min_even>even[index]):
        even_min=even[index]
    if(max_even<even[index]):
        even_max=even[index]
 
#find the max and minimum value in odd list   
for index in range(0,len(odd)):
    if(min_odd>odd[index]):
        odd_min=odd[index]
    if(max_odd<odd[index]):
        odd_max=odd[index]

print("Even minimum: ",even_min)
print("Even max: ",even_max)
print("odd Maximum ",odd_max)
print("odd minimum ",odd_min)