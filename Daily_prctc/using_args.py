# variable length arguments *args
def add_numbers(*args):
    print(sum(args))
add_numbers(3,5)
add_numbers(9,6,4)

# positional arguments 
def introduce(name,age):
    print(f"my name is {name} and iam {age} years old.")
introduce("Alice",21)
introduce(21,"Hasna")

# keyword variable arguments **kwargs
