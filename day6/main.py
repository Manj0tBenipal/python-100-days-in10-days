a = input("Enter a number:")
print(f"The table of {a} is:")
try: 
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except Exception as e:
    print(e)
finally:
    print("The end")