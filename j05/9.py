n=int(input())
# print(str(n) == str(n)[::-1])
str_n = str(n)
reversed_n = ""
for i in range(len(str_n) -1, -1, -1):
    reversed_n += str_n[i]

print("yes" if reversed_n == str_n else "no")