#Python Basics Variable

#Answer_1

# Declare and initialize variables
x = 5
y = 10

# Swap values without using a temporary variable
x = x + y
y = x - y
x = x - y

# Now, x and y have swapped values
print("After swapping:")
print("x =", x)
print("y =", y)





#Answer_2

# Take user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width

# Display the result
print("The area of the rectangle is:", area)





#Answer_3

# Take user input for temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display the result
print("Temperature in Fahrenheit:", fahrenheit)











#String Based Questions

#Answer_1

# Take user input for a string
user_input = input("Enter a string: ")

# Calculate the length of the string
string_length = len(user_input)

# Display the result
print("Length of the string:", string_length)






#Answer_2

# Take user input for a sentence
sentence = input("Enter a sentence: ")

# Convert the sentence to lowercase to make the counting case-insensitive
sentence = sentence.lower()

# Initialize a variable to count the vowels
vowel_count = 0

# Loop through each character in the sentence
for char in sentence:
    # Check if the character is a vowel
    if char in "aeiou":
        vowel_count += 1

# Display the result
print("Number of vowels in the sentence:", vowel_count)





#Answer_3

# Take user input for a string
original_string = input("Enter a string: ")

# Use string slicing to reverse the string
reversed_string = original_string[::-1]

# Display the reversed string
print("Reversed string:", reversed_string)







#Answer_4

# Take user input for a string
original_string = input("Enter a string: ")

# Remove spaces and convert the string to lowercase for case-insensitive comparison
processed_string = original_string.replace(" ", "").lower()

# Reverse the string
reversed_string = processed_string[::-1]

# Check if the original and reversed strings are the same
if processed_string == reversed_string:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")

    
    
    
    
    

    
#Answer_5

# Take user input for a string
original_string = input("Enter a string: ")

# Remove spaces from the string
modified_string = original_string.replace(" ", "")

# Display the modified string without spaces
print("Modified string without spaces:", modified_string)
