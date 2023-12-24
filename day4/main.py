# Lists;
a = [1,2,3,4,5,6,7,8,9,0]
print(a)
print(a[1])
print(a[1:4]) # slicing from index 1-3
print(a[1:10:2]) #slicing and printing from index 1-10 witha  jump of 2 index
print(a[-10: -1: 2]) #doing the same thing using resversed index

#List comprehension:
print([i for i in range(20)] )

# list methods
a.sort();# sorts the list in ascendin order
print (a)
a.sort(reverse=True) #sorts the list in descending order
print(a)
a.append(10) # adds element to the last of list

a.reverse() # reverses the list 
print(a)
print(a.index(1)) # returns the index of an element in the list if exists otherwise throws an error(-1 is valid index ion pyhton)
print(a.count(1)) # returns the number of occurances of element

b= a # passed by reference gonna change the original list
b=a.copy() # copies the list instead of passing by reference
b.insert(899, 2) # inserts an element at a given index in a list

a.extend(b) # extends a with b means joins ba t the ned of a

#TWo dimensional lists
points=0
questionAnswers = [["1+1", "2+3", "3+2", "5+9"], [2,5,5,14]]
options = questionAnswers[1].copy().sort();
for i in range(len(questionAnswers[0])):
    print("What is ", questionAnswers[0][i], "?")
    answer = int(input("Enter your Answer:"))
    if(answer==questionAnswers[1][i]):
        points+=1

print("You got " + str(points) +" out of " +str(len(questionAnswers[0])))