import os

def compare_folders(folder1, folder2):
    files_only_in_folder1 = []
    files_only_in_folder2 = []

    for file in os.listdir(folder1):
        if os.path.isfile(os.path.join(folder1, file)):
            if file not in os.listdir(folder2):
                files_only_in_folder1.append(file)

    for file in os.listdir(folder2):
        if os.path.isfile(os.path.join(folder2, file)):
            if file not in os.listdir(folder1):
                files_only_in_folder2.append(file)

    return files_only_in_folder1, files_only_in_folder2

# Specify the folder paths for comparison
folder1_path = 'file name'
folder2_path = 'file name'

# Compare the folders
folder1_files, folder2_files = compare_folders(folder1_path, folder2_path)

# Print the results
print(f'Files only in {folder1_path}:')
for file in folder1_files:
    print(file)

print(f'\nFiles only in {folder2_path}:')
for file in folder2_files:
    print(file)

# Prepare the output string
output_string = f'Files only in {folder1_path}:\n'
output_string += '\n'.join(folder1_files)
output_string += f'\n\nFiles only in {folder2_path}:\n'
output_string += '\n'.join(folder2_files)

# Save the output to a text file
output_file_path = 'folder_comparison.txt'
with open(output_file_path, 'w') as file:
    file.write(output_string)

print(f"Comparison results saved to '{output_file_path}'.")