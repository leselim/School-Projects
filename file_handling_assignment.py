# Task 1: File Creation
# Create a new text file named "my_file.txt" in write mode ('w')
with open("my_file.txt", "w") as file:
    # Write at least three lines of text to the file, including a mix of strings and numbers
    file.write("This is the first line.\n")
    file.write("12345 is a number.\n")
    file.write("Third line with more text.\n")

# Task 2: File Reading and Display
# Open the file in read mode ('r') and display the contents on the console
with open("my_file.txt", "r") as file:
    content = file.read()
    print("Contents of 'my_file.txt':")
    print(content)

# Task 3: File Appending
# Open the file in append mode ('a') and append three additional lines of text
with open("my_file.txt", "a") as file:
    file.write("This is an appended line.\n")
    file.write("Appending some more numbers: 67890.\n")
    file.write("Final appended line in the file.\n")

# Display the final contents after appending
with open("my_file.txt", "r") as file:
    final_content = file.read()
    print("Final contents of 'my_file.txt' after appending:")
    print(final_content)
