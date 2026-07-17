#tuples
#     these are immutable lists, meaning they cannot be changed after creation
#     Tuples have a fixed size and cannot be modified, which makes them useful for storing data that should not change throughout the program.
#     have curly braces and are defined using parentheses () instead of square brackets [].

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
print(5 in my_tuple)
print(my_tuple)

x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(z)

print(my_tuple.count(5))
print(my_tuple.index(5))