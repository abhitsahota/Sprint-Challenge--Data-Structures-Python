import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
### Original 
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

### Solution


# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):

#         if value >= self.value:
#             if self.right is not None:
#                 self.right.insert(value)
#             else:
#                 self.right = BinarySearchTree(value)

#         elif value < self.value:
#             if self.left is not None:
#                 self.left.insert(value)
#             else:
#                 self.left = BinarySearchTree(value)

#     def contains(self, target):
#         if self.value == target:
#             return True

#         if target > self.value:
#             if self.right is not None:
#                 return self.right.contains(target)

#         elif target < self.value:
#             if self.left is not None:
#                 return self.left.contains(target)

#         else:
#             return False

# btree = BinarySearchTree('names')

# for names in names_1:
#     btree.insert(names)

# for name in names_2:
#     if btree.contains(name):
#         duplicates.append(name)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

duplicates =  set(names_1).intersection(names_2)