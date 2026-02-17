run = 1
sumNumbers = 0
length = 0

while run:
    a = int(input())
    if a == 0:
        run = 0
    else:
        sumNumbers += a
        length += 1

avg = sumNumbers/length

if avg == int(avg):
    print(int(avg))
else:
    print(avg)