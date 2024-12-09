# halflife machine learning project
# Michael Song, songmichael11@gmail.com

import matplotlib

# reads half life file and returns a 2d array of the values, where each row is a molecule
def read_text_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    output = []
    for line in lines:
        row = line.strip().split()
        if "-" in row[1]: #if half life is a range, averages the two numbers
            new = row[1].split("-")
            row[1] = (float(new[0]) + float(new[1])) / 2

        output.append(row)

    return output

filename = 'thalf.txt'  

# Create the 2D array from the text file
two_d_array = read_text_file(filename)

# Print the resulting array
for row in two_d_array:
    print(row)