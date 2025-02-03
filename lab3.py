import random
import itertools

# Task 1:
def grams_to_ounces():
    grams = float(input("Enter grams: "))
    print("Ounces:", grams * 28.3495231)

# Task 2: 
def fahrenheit_to_centigrade():
    fahrenheit = float(input("Enter Fahrenheit temperature: "))
    print("Centigrade:", (5 / 9) * (fahrenheit - 32))

# Task 3: 
def solve():
    num_heads = int(input("Enter number of heads: "))
    num_legs = int(input("Enter number of legs: "))
    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens
        if 2 * chickens + 4 * rabbits == num_legs:
            print("Chickens:", chickens, "Rabbits:", rabbits)
            return
    print("No solution")

# Task 4: 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Prime numbers:", [num for num in numbers if is_prime(num)])



# Task 5: 
def string_permutations():
    s = input("Enter a string: ")
    print("Permutations:", list(map("".join, itertools.permutations(s))))

# Task 6: 
def reverse_words():
    sentence = input("Enter a sentence: ")
    print("Reversed sentence:", " ".join(sentence.split()[::-1]))

# Task 7: 
def has_33():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            print(True)
            return
    print(False)

# Task 8:
def spy_game():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            print(True)
            return
    print(False)

# Task 9: 
def sphere_volume():
    radius = float(input("Enter radius of the sphere: "))
    from math import pi
    print("Volume of sphere:", (4/3) * pi * radius**3)

# Task 10: 
def unique_elements():
    lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    print("Unique elements:", unique_list)

# Task 11: 
def is_palindrome():
    s = input("Enter a word or phrase: ")
    s = s.replace(" ", "").lower()
    print("Is palindrome:", s == s[::-1])

# Task 12: 
def histogram():
    lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
    for value in lst:
        print('*' * value)

# Task 13:
def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    number_to_guess = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break


