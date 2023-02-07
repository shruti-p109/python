values = [10, 20, 30, 40]

print(values)

print(type(values)) # datatype of variable 'values'

print(type(values[0])) # datatype of 1st value of collection variable 'values'

print(len(values)) # size of collection

print(values[0]) # accessing elements by index
print(values[1])
print(values[2])
print(values[3])

# add new element
# values[4] = 50 # IndexError: list assignment index out of range
values.append(50)
print(values)

# remove element, list as whole editable (mutable) (add/remove element) - but can not change data / value of a element - int here (int is immutable, change value, memory itself changes)
values.remove(20)
print(values)

# what about duplicates
values.append(50)
print(values)
# ans - [10, 30, 40, 50, 50] - so yes duplicates allowed

# add float value - check for heterogenuity
values.append(90.89)
print(values)
# yes allowed -> lists are heterogeneous

# add value in somewhere in middle - google - only for syntax/how to call or use - dont copy
values.insert(3, 45)
print(values)
# [10, 30, 40, 45, 50, 50, 90.89]

# insert at index thats out of bound i.e. larger than length
values.insert(15, 89)
print(values) # [10, 30, 40, 45, 50, 50, 90.89, 89]
print(len(values)) # 8
# No Error, worked like append, it inserted element at the end
