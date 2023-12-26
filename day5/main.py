# doc_strings

def square(a):
    #this is an example of a doc string
    """
    This function returns the square of the number passed to it.
    """
    return a*a

print(square(5))
print(square.__doc__) # this prints the doc string of the function
#fibonacci series

def printFoboncciSeries(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
       return  printFoboncciSeries(n-1)+ printFoboncciSeries(n-2)
print(printFoboncciSeries(7))
# 0 1 1 2 3 5 8 13

#sets
# A set is initialized using curly braces
a={1,2,3,4,4,5,6}
# In this set 4 is entered twice but whe printed only one 4 will be displayed
print(a)
# a set does not maintain order

b={1,2,3,4,5,6,7,8,9,10}
print(type(a))
#set methods

#union
print(a.union(b))
#intersection
print(a.intersection(b))

#update: changes the set to the union of two sets
print(a.update(b))

#update intersection:changes the set to instersection of two sets
print(a.intersection_update(b))

#symmetric Difference is the union of two sets minus the intersection of two sets. 
print(a.symmetric_difference(b))

#difference: a-b =>a-a intersection b
print(a.difference(b))
#disjoint returns boolean if two sets have no intersection
#issuperset => returns boolean if a.issuperset(b) a is superset of b
#issubset => returns boolean if b.issubset(a) b is subset if a
#remove/discard("item") are used to remove elements from a set

#Dictionaries
#Dictionaries store objects in a key-value pair just like objects in js

dict = {"name":"Manjot", "occupation": "Waana be Developer"}
print(dict["name"])
print(dict.get("name"))

dict2={1:1,2:2,3:3}
dict.update(dict2) # joins two dictionaries
print(dict)

#clear a dictionary using 
dict2.clear()

#pop deletes  a key:value pair

#popitem() pops last item of the dictionary
print(dict.popitem())
