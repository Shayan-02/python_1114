l1 = ["ali", "reza", "ahmad"]
l2 = ["sara", "mina", "anita"]
l1.append("mohammad")
l1.insert(0, "saeed")
print(len(l1))
# l1.append(l2)
# print(len(l1))


# way1
# i = 0
# while i < len(l2):
#     l1.append(l2[i])
#     i += 1

# way2
# for _ in range(len(l2)):
#     l1.append(l2[_])

# way3
# for _ in l2:
#     l1.append(_)

# way4
# l1.extend(l2)

print(len(l1))