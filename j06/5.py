dataset = ["ali", 10, "reza", 20, "babak", 5]

str_list = []
num_list = []
final_list = []

for _ in dataset:
    if type(_) == int or type(_) == float:
        num_list.append(_)
    elif type(_) == str:
        str_list.append(_)

num_list.sort(reverse=True)
str_list.sort(reverse=True)

num_list.extend(str_list)
