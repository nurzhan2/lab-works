# Booleans
print("Boolean Comparisons:")
print(10 > 9)       # True
print(10 == 9)      # False
print(10 < 9)       # False

a = 200
b = 33
print("\nBoolean in Conditional:")
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print("\nBoolean Values:")
print(bool("Hello"))    # True
print(bool(15))         # True
print(bool([]))         # False
print(bool(0))          # False

class MyClass:
    def __len__(self):
        return 0

myobj = MyClass()
print("\nClass Boolean:")
print(bool(myobj))      # False

def my_function():
    return True

print("\nFunction Return:")
print(my_function())    # True

if my_function():
    print("YES!")       # YES!
else:
    print("NO!")

print("\nType Check:")
x = 200
print(isinstance(x, int))  # True

# Operators
print("\nOperators:")
print(10 + 5)           # 15
print((6 + 3) - (6 + 3)) # 0
print(100 + 5 * 3)      # 115

# Lists
print("\nList Operations:")
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)
print("Length:", len(fruits))

fruits[1] = "blackcurrant"
print("Modified List:", fruits)

fruits.append("orange")
print("After Append:", fruits)

fruits.insert(1, "mango")
print("After Insert:", fruits)

fruits.remove("blackcurrant")
print("After Remove:", fruits)

print("\nList Comprehension:")
newlist = [x.upper() for x in fruits if "a" in x]
print(newlist)

fruits.sort()
print("\nSorted List:", fruits)

# Tuples
print("\nTuple Operations:")
thistuple = ("apple", "banana", "cherry")
print("Original Tuple:", thistuple)
print("Tuple Length:", len(thistuple))

print("\nTuple Unpacking:")
(green, yellow, red) = thistuple
print(green, yellow, red)

# Sets
print("\nSet Operations:")
thisset = {"apple", "banana", "cherry"}
print("Original Set:", thisset)
thisset.add("orange")
print("After Add:", thisset)

# Dictionaries
print("\nDictionary Operations:")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Original Dictionary:", car)
print("Dictionary Keys:", car.keys())

car["year"] = 2020
print("\nUpdated Dictionary:", car)

# Control Flow
print("\nControl Flow:")
for i in range(5):
    if i == 3:
        continue
    print(i, end=' ')
print()

# Error Handling Example (commented out)
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)  # This will raise an error

print("\nLoop Through Dictionary:")
for key, value in car.items():
    print(f"{key}: {value}")

print("\nFinal Combined List:")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)