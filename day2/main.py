import time;
time = time.strftime("%H:%M:%S");
print("Current time: ", time);
if(12>int(time.split(":")[0]) >=0):
    print("Good Morning")
else:
    print("Good Afternoon")
match  int(time.split(":")[0]):
    case 12:
        print("Good Noon")
    case 0:
        print("Good Midnight")


colors =["red", "blue", "yellow", "green", "orange", "purple", "black", "white", "grey", "pink"];
for color in colors:
    for letter in color:
        print(letter, end="");
    print()

for i in range(10):
    print(i, end="")
i=0
while i< 20 :
    print(i, end="")
