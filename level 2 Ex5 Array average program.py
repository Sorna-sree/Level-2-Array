#1. Find the average of numbers in an array.

my_list=[2,3,4,5,6,7,5,6,8,10]
total=0

#total calculation
for index in range(0,len(my_list)):
    total+=my_list[index]

  
print(total) 
#calculate the average   
average=total/len(my_list)
print(average)