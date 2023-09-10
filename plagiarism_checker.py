import difflib

# Function to read the content of a file
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Function to compare two text files and find similarities
def plagiarism_checker(file1_path, file2_path):
    text1 = read_file(file1_path)
    text2 = read_file(file2_path)

    if text1 is not None and text2 is not None:
        d = difflib.Differ()
        diff = list(d.compare(text1.splitlines(), text2.splitlines()))

        # Calculate the similarity score
        similarity = sum([1 for line in diff if line.startswith('  ')]) / len(diff) * 100

        print(f"Similarity Score: {similarity:.2f}%")

        # Print the differences (optional)
        print("\nDifferences:")
        for line in diff:
            if line.startswith('- '):
                print("Removed:", line[2:])
            elif line.startswith('+ '):
                print("Added:", line[2:])

# Example usage:
file1_path = 'file1.txt'
file2_path = 'file2.txt'
plagiarism_checker(file1_path, file2_path)
