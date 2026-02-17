a = 1
while a <= 20:
    if a % 15 == 0:
        break
    elif a == 7 or a == 13:
        a += 1
        continue
    print(a)
    a += 1
