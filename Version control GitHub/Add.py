def add_file(filename, content):
    try:
        # Open the file in write mode ('w')
        with open(filename, 'w') as file:
            # Write content to the file
            file.write(content)
        print(f"File '{filename}' created successfully.")
    except IOError:
        print(f"Error: Unable to create or write to file '{filename}'.")

# Example usage:
filename = "example.txt"
content = "Hello, world!\nThis is a new file created using Python."

add_file(filename, content)
