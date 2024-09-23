
# Standard library that handles files
import csv
import os
import webbrowser

names = []

# Open file to read, similar to the use statement in C#
# (while we have context or scope):
# If the file doesn't exist, it will create it.
# When adding append, it will continue adding more data to the current file.

try:
    with open('grades.csv', 'r') as data_file:
        csv_data = csv.reader(data_file)

        next(csv_data)  # Skip the header row
        for row in csv_data:
            row[1] = row[1].replace('"', '')
            names.append(f'{row[1].strip()} {row[0].strip()}')
            print(names)

except OSError as ex:
    print(ex)

# Sort the names if any were found
if len(names) > 0:
    names.sort()

# Generate HTML output
html_output = f'<p>Total Students: {len(names)}</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

# Write the HTML output to a file
filename = 'list.html'

with open(filename, 'w') as file:
    file.write(html_output)

# Print the full path of the HTML file
full_path = os.path.realpath(filename)
print(full_path)

# Open the HTML file in the default web browser
webbrowser.open(f'file://{full_path}')
