# sort algorthms and methods for reference 
# selection_sort

# sorting an array from smallest to largest
def find_smallest(arr):
    smallest = arr[0] # store smallest value
    smallest_index = 0 # store index of smallest value
    # start from the second item
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

arr = [9,8,3,1,4,6]
print(find_smallest(arr))

def selection_sort(arr):
    new_array = []
    # start from the beginning
    for i in range(0, len(arr)):
        smallest_index = find_smallest(arr)
        # append it
        new_array.append(arr[smallest_index])
        # remove from the array
        arr.pop(smallest_index)
    return new_array

print(selection_sort(arr))

# Python built in methods

l = [9,1,8,2,7,3,6,4,5]
# sorted() works on any iterable like tuples, dictionaries
# Returns a new sorted object
sorted_l = sorted(l)
print(l)
print(sorted_l)

# sort method motifies the list-in place. Returns None
l.sort()
print(l)

# sorted can take in a reverse parameter
l = [9,1,8,2,7,3,6,4,5]
sorted(l, reverse=True)

# same with sort()
l.sort(reverse=True)

# but, sort() only works with lists
tup = (9,1,8,2,7,3,6,4,5)
tup.sort() # does not works
sorted(tup)

# what if I want to sort by the absolute value?
li_negs = [-6,-5,-4,1,2,3]

# One numpy way
import numpy as np
# get indices, apply abs on the array
indices = np.argsort(abs(np.array(li_negs)))
# li_negs, sorted by abs value
[li_negs[i] for i in indices][::-1] # descending by abs
[li_negs[i] for i in indices] # ascending by abs

# using Python sorted, it's ONE line!
# use key parameter, which takes a function to be called on each element
# prior to making comparisions!
sorted(li_negs, key=abs)

# another example
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'({self.name}, {self.age}, {self.salary})'

e1 = Employee('Carl', 37, 70_000)
e2 = Employee('Sarah', 29, 80_000)
e3 = Employee('John', 20, 90_000)

employees = [e1,e2,e3]
# in order to sort this, you have to specify what to sort by
def e_sort(emp):
    return emp.name

e_sort(e1)

sorted(employees, key=e_sort)
sorted(employees, key=lambda x: x.age) # good place to use lambda functions
sorted(employees, key=lambda x: x.salary, reverse=True)
