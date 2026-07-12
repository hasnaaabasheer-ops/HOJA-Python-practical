# Global Variable
x = 10
def show():
    print("inside the function",x)
show()
print("outside the function",x)

# Local Variable
def display():
    y=5
    print("\ninside the function ",y)
display()
# There will be error because a local variable only works inside a function 
print("outside the function",y)