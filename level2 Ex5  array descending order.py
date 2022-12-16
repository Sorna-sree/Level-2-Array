
#Sort and array with 10 elements in descending order.
array=[10,5,25,6,8,9,1,22,44,90]
temp=0

print("Original array: ",array)

#ascending order of array
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if(array[i]<array[j]):
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
            
print(" descending order:",array)