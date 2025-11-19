# --------------------
# EXAMPLE 1
# --------------------
word = "apple"

letter = input("Guess a letter in the secret word: ").lower()

if letter in word:
   print(f"There is a {letter}")
else:
   print(f"{letter} was not found")

# --------------------
# EXAMPLE 2
# --------------------

grades = {
   "Sandy": 'A',
   "Squidward": 'B',
   "Spongebob": 'C',
   "Patrick": 'D'
}

student = input("Enter the name of a student: ").capitalize()

if student in grades:
   print(f"{student}'s grade is {grades[student]}.")
else:
   print(f"{student} is not in the dictionary")

# --------------------
# EXAMPLE 3
# --------------------
email = "BroCode@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

#-------------------
#LIST COMPREHENSIONS
#-------------------
fruits = ["apple", "orange", "banana", "coconut"]
drinks = ["apple juice","orange juice","banana shake","coconut milk"]
fruit_chars = [fruit for fruit in fruits if len(fruit)>5]
print(fruit_chars)