for x in range(151):
    print(x)
#########################################################
for x in range(0,1001,5):
    print(x)
#########################################################
for x in range(1,101):
    if x % 5 == 0 and x % 10 == 0:
        print("Coding-Dojo")
        continue
    elif x % 5 == 0:
        print("Coding")
        continue
    print(x)
#########################################################
odds = []
for x in range(0,500000):
    if x%2 == 1:
        odds.append(x)
oddtotal = sum(odds)
print(oddtotal)

sum = 0
for x in range(0,500000):
    if x%2 != 0:
        sum += x
print(sum)

#########################################################

start = 2018
while start > 0:
    print(start)
    start -= 4
#########################################################
lowNumber = 2
highNumber = 20
mult = 3

for x in range(lowNumber, highNumber):
    if x%mult == 0:
        print(x)

