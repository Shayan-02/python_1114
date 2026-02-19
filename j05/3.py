n = int(input("enter rows: "))
m = int(input("enter columns: "))

print("===================== way1 ========================")

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(i*j, end="\t")
    print("\n")

print("===================== way2 ========================")

k = 1

while k < n + 1:
    l = 1
    while l < m + 1:
        print(k * l, end="\t")
        l += 1
    print("\n")
    k += 1