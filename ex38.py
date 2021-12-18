# Exercise 38: Doing stuff to lists
ten_things = "Apples Oranges Crows Telephone Light Sugar"

stuff = ten_things.split(' ')

print(f"Wait, there aren't 10 things things in the list.  There are only {len(stuff)} things in the list.")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while (len(stuff) < 10):
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are now {len(stuff)} items.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # should be last element in list
print(stuff.pop())
print(' '.join(stuff)) # joins all elements of list together in a string with spaces in between each element.
print("#".join(stuff[3:5]))
