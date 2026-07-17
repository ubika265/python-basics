# The walrus operator := assigns values to variables as a part of larger expression
a = 'helllloooooooo'
if ((n := (len(a))) > 10):
    print(f'list is too long , {n} elements present ')

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]
print(a)    