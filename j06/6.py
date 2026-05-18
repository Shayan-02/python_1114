# lst = []
# for i in range(3):
#     a = int(input("number: "))
#     lst.append(a)

# a = input().split()
a = ["1", "2", "3"]

# for _ in a:
#     _ = int(_)

for _ in range(len(a)):
    a[_] = int(a[_])


print(a)