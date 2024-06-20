
# Taking input from the user
text = input("Enter some text to write to a file: ")

# File path where the text will be saved
file_path = "user_text.txt"

# Writing the input text to a file
with open(file_path, 'w') as file:
    file.write(text)

print(f"Text has been written to {file_path}")











