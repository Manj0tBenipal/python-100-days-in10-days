# Lists;
a = [1,2,3,4,5,6,7,8,9,0]
print(a)
print(a[1])
print(a[1:4]) # slicing from index 1-3
print(a[1:10:2]) #slicing and printing from index 1-10 witha  jump of 2 index
print(a[-10: -1: 2]) #doing the same thing using resversed index

#List comprehension:
print([i for i in range(20)], );

# list methods
a.sort();# sorts the list in ascendin order
print (a)
a.sort(reverse=True) #sorts the list in descending order
print(a)
a.append(10) # adds element to the last of list

a.reverse() # reverses the list 
print(a)
print(a.index(19)) # returns the index of an element in the list if exists otherwise throws an error(-1 is valid index ion pyhton)