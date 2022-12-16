# Sort an array with 3 elements in ascending order.
array=[10,5,1]
temp=0

print("Original array: ",array)

#ascending order of array
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if(array[i]>array[j]):
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
            
print("ascending order: ",array)


