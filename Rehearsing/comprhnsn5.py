numbers = [1, 2, 3, 4, 5]
parity = {x: ("even" if x % 2 == 0 else "odd") for x in numbers}
print(parity)