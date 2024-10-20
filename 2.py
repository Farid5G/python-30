# Write a code using a while loop that adds all odd numbers from 1 to 50
# Ans: 625

a = 1
total = 0
while a <= 50:
    if a % 2 != 0:
        total += a
    a += 1
print(total)

# Writing similar code logic without using if-else
# ans: 625

a = 1
ttl = 0

while(a <= 50):
    ttl += a
    a += 2
    
print(ttl)