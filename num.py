def read_and_modify_file(input_filename, output_filename):
    try:
        # Read the content of the input file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (e.g., convert to uppercase for demonstration)
        modified_content = content.upper()

        # Write the modified content to the output file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"File '{input_filename}' has been read and modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")

def main():
    input_filename = input("Enter the name of the input file: ")
    output_filename = input("Enter the name of the output file: ")
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
