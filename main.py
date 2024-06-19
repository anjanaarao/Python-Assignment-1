#Q1
a = int(input("Enter first num : "))
b = int(input("Enter second num : "))

sum = a+b

print("sum =", sum)

#Q2
num = int(input("Enter a number : "))

if (num%2 == 0) :
  print("even")
else :
  print("odd")

#Q3
num = int(input("Enter a number : "))

if (num < 0) :
  print("Factorial not defined for negative numbers")

elif ( num == 0 or num == 1) :
  print("Factorial = 1")

else :
  factorial = 1
  i = 2

while ( i <= num )  :
  factorial = factorial*i
  i = i+1

print("Factorial =", factorial)

#Q4
name = input("Enter your name : ")

print("Hello", name)

#Q5
# Read input string from the user
input_string = input("Enter a string: ")

# Specify the file name
file_name = "output.txt"

try:
    # Open the file in write mode
    with open(file_name, 'w') as file:
        # Write the input string to the file
        file.write(input_string)
    print(f"String '{input_string}' has been written to {file_name} successfully.")
except IOError as e:
    print(f"Error: {e}")

#Q6
# Specify the file name to read
file_name = "input.txt"

try:
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read and print the content of the file
        file_contents = file.read()
        print("Contents of the file:")
        print(file_contents)
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except IOError as e:
    print(f"Error: {e}")


#Q7
str = input("Enter a string : ")

print("Length =", len(str)) 

#Q8
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

print("Concatenated string =", str1 + str2) 

#Q9

str = input("Enter a string : ")
substr = input("Enter the substring : ")

if substr in str :
  print("Substring present.")

else :
  print("Not present.") 

#Q10
str = input("Enter a string : ")

str = str.upper()
print(str) 

#Q11
n = int(input("enter a number : "))

if ( n == 0 or n == 1) :
  print("Fib no =", n)

else : 
  a = 0
  b = 1
  i = 2
  while ( i <= n ) :
    c = a+b
    a = b
    b = c
    i = i+1

print("Fib no =", b) 

#Q12
n = int(input("enter a number : "))

sum = 0

while n>0 :
  d = n%10
  sum = sum+d
  n = n//10

print(sum) 

#Q13
year = input("Enter birth year : ")

age = 2024 - int(year)
print("age =", age) 

#Q14
lines = []

print("Enter lines of text. Enter an empty line to quit.")

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("You have entered:")

for line in lines:
    print(line) 

#Q15
import csv

# Specify the CSV file name
file_name = "data.csv"

try:
    # Open the CSV file in read mode
    with open(file_name, mode='r', newline='') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Print each row to the console
            print(', '.join(row))

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except IOError as e:
    print(f"Error: {e}")


#Q16
# Read input string from the user
input_string = input("Enter a string: ")

# Initialize an empty dictionary to store character frequencies
char_freq = {}

# Count frequency of each character in the string
for char in input_string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Print the character frequencies
print("Character frequencies:")
for char, freq in char_freq.items():
    print(f"{char}: {freq}")


#Q17
str = input("enter string : ")

str = str.title()
print(str) 

#Q18
str1 = input(("enter first string : "))
str2 = input(("enter second string : "))

str1 = ''.join(str1.split()).lower()
str2 = ''.join(str2.split()).lower()

sort_str1 = sorted(str1)
sort_str2 = sorted(str2)

if sort_str1 == sort_str2 :
  print("anagram")

else :
  print("not anagram") 

#Q19
import string

str = input("enter a string : ")

translator = str.maketrans('', '', string.punctuation)

final_str = str.translate(translator)

print(final_str) 

#Q20
# Read input numbers from the user
input_string = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of numbers
numbers = list(map(float, input_string.split()))

# Calculate the sum of the numbers
total_sum = sum(numbers)

# Print the sum
print(f"The sum of the numbers is: {total_sum}")

#Q21
str = input("enter a string : ")

list = str.split()

element_to_count = input("enter the element : ")

count = list.count(element_to_count)

print(count)

#Q22 
numbers = [1,2,3,4,5]

min_value = min(numbers)
max_value = max(numbers)

print("min value =", min_value, "max value =", max_value) 

#Q23
temp = float(input("enter the temp : "))
unit = input("enter the unit : ")

if unit.upper() == 'C' :
  temp = temp*9/5 + 32
  print(temp)

elif unit.upper() == 'F' :
  temp = (temp - 32)*5/9
  print(temp) 

#Q24
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print("Result: ", result) 

#Q25
# Read file names from the user
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

try:
    # Open source file in read mode and destination file in write mode
    with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
        # Read all contents from source file and write to destination file
        contents = source.read()
        destination.write(contents)
    print("File contents copied successfully.")
except FileNotFoundError:
    print("Error: One or both files not found.")
except IOError as e:
    print(f"Error: {e}")

#Q26
# Read input string, prefix, and suffix from the user
input_string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

# Check if the string starts with the prefix
if input_string.startswith(prefix):
    print(f"The string starts with '{prefix}'.")
else:
    print(f"The string does not start with '{prefix}'.")

# Check if the string ends with the suffix
if input_string.endswith(suffix):
    print(f"The string ends with '{suffix}'.")
else:
    print(f"The string does not end with '{suffix}'.")

#Q27
# Read input string from the user
input_string = input("Enter a string: ")

# Convert the string into a list of characters
characters_list = list(input_string)

# Print the list of characters
print("List of characters:", characters_list)



