def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} x {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} by {b}")
    return a / b


print("let's do some math with just functions.")

age = add(30, 5)
height = subtract(76, 4)
weight = multiply(90, 2)
iq = divide(300, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for extra credit.  Type it in anyway
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 4))))
print(f"That becomes: {what} Can you do it by hand?")
