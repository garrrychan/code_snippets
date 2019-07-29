# 1) SQL - alias tables (Employee & Student)

# select e.name, m.name as manager_name
# from employees e
# join employees m
# on e.manager_id = m.id;

# 2) Object Oriented Programming
class Pets():
    def __init__(self, animal):
        self.animal = animal

    def show(self):
        print(f'Hi, I am a {self.animal}')

dog = Pets("dog")
cat = Pets("cat")
wolf = Pets("wolf")

dog.animal
cat.animal
wolf.animal

dog.show()
cat.show()
wolf.show()

# wolf becomes a dog
wolf.animal = 'dog'
wolf.show()

# 3) Strings - string manipulation
# 3A) String manipulation to find number of upper

mixed_str = 'HeLLoWOrld'
def upper_count(mixed_str):
    count = 0
    for char in mixed_str:
        if char == char.upper():
            count += 1
        else:
            continue
    return count

upper_count(mixed_str)

# 2B) Return a dictionary of the counts of uppers letters
def dict_counts(mixed_str):
    my_dict = {}
    for char in mixed_str:
        # upper and ignore spaces
        if char == char.upper() and char != ' ':
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
    return my_dict

dict_counts(mixed_str)
dict_counts('What are the UPPER letter counts')

# 4) Lists - Target sum
# Brute Force

lst = [1,2,3,4,5]
# [1,5] - index 0, 4
# [2,4] - index 1, 3

# brute, O(n^2) time complexity
# Worst case we are looping through the array twice to find a pair
def index_of_target_sum(arr, target):
    # check each element
    for i in range(0,len(arr)):
        # check every other element
        for j in range(i+1, len(arr)):
            # check if sum to target
            if arr[i] + arr[j] == target:
                print(f'values: {(arr[i], arr[j])}')
                print(f'indices: {(i, j)}')
                print(f'\n')
            else:
                continue

index_of_target_sum(lst, 6)

# optimized O(n) linear time
# each lookup and insertion is O(1) constant time
def index_of_target_sum_optimized(arr, target):
    hash_table = {}
    # check each element
    for i in range(0, len(arr)):
        # calculate delta
        delta = target - arr[i]
        # check if this number exists in hash_table
        # if True, then we found a pair of numbers that sum to target
        if delta in hash_table:
            print(f'values: {(delta, arr[i])}')
            print(f'indices: {(arr.index(delta),i)}')
            print('\n')
        # add the current number to the hash table
        hash_table[arr[i]] = arr[i]

index_of_target_sum_optimized(lst, 6)
