#2. Find the longest and shortest word in an array of words.

words=["cat","lion","rabbit","donkey","cheetah","zebra","elephant"]

small=large=words[0] #set the first index is small and large word

#find the small and large word

for index in range(0,len(words)):
    if(len(large)<len(words[index])): #largest word find
        large=words[index]
    if(len(small)>len(words[index])): #smallest word find
        small=words[index]
        
print("largest word ",large)
print("Smallest word ",small)
    