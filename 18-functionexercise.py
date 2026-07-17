def highest_even(list):
    even = []
    for item in list:
        if item % 2 == 0:
          even.append(item)
    res = max(even)
    return res

print(highest_even([10,2,3,4,8,11,20,23]))   


          