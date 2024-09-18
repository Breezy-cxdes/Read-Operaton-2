# Program to copy odd lines from 'Codingal.txt' to 'Codingalidated.txt'

# Open the original file in read mode
file1 = open('Codingal.txt', 'r')

# Open a new file in write mode
file2 = open('Codingalidated.txt', 'w')

# Read the content of the original file line by line
lines = file1.readlines()

# Loop through the lines and copy odd-numbered lines to the new file
for i in range(len(lines)):
    if i % 2 == 0:  # This checks for odd-numbered lines (0-based index)
        file2.write(lines[i])

# Close both files
file1.close()
file2.close()

# Optional: reopen the new file and print its contents
file2 = open('Codingalidated.txt', 'r')
content = file2.read()
print(content)
file2.close()
