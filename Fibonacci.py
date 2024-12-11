# Write a fibonacci sequence till n digits 

def fibo(n):
    if(n == 1):
        return 0
    elif(n == 2):
        return 0,1
    var1 = 0
    var2 = 1
    print(var1)
    print(var2)
    for i in range(1,n):
        res = var1 + var2
        print(res)
        var1 = var2
        var2 = res

# Search for an element in a list linearly (using a single for loop)
x = [1,34,23,0,334,221,56]
element = 34

for index, value in enumerate(x):
    if(value == element):
        print("Found at position ", index)

#Without enumerate we will need a counter 
index = 0
for value in x:
    if(value == element):
        print("Found at position ", index)
    index = index + 1