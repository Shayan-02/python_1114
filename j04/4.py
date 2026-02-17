s = int(input("enter start number: "))
end = int(input("enter end number: "))

start = s

if end < start:
    end, start = start, end
while start <= end:
    if start % 15 == 0:
        print("fizzbazz")
    elif start % 5 == 0:
        print("bazz")
    elif start % 3 == 0:
        print("fizz")
    else:
        print(start)
    start += 1