#WAP using loop to print first 10 even numbers in the reverse order

# method 1:
num = 20
while(num>=0):
    print(num)
    num-=2

# method 2:
for i in range(20,0,-2):
    print(i)