import openpyxl
import re

# Open the workbook and the worksheet
wb = openpyxl.Workbook()
ws = wb.active

# Open the file in read mode
with open('/Users/paul/Desktop/openEAR-0.1.0/smile.log', 'r') as f:
    # Get the last 23 lines of the file
    last_25_lines = f.readlines()[-25:]
    input=str(last_25_lines)
    
    result=re.findall(r'[\d\.\d]+', input)
    
    print(result)
    
    oxl = openpyxl.load_workbook('/Users/paul/Desktop/output.xlsx')
    xl = oxl.sheet

    x=0
    col = "A"
    row = x

    while (row <= 100):
        y = str(row)
        cell = col + row
        xl[cell] = x
        row = row + 1
        x = x + 1   
    
    # Extract the double numbers and write them to the worksheet
    for line in result:
        numbers = []
        # Split the line into words
        words = line.split()
        for word in words:
            # Try to convert the word to a double number
            try:
                number = float(word)
                numbers.append(number)
            except ValueError:
                # If the word is not a number, skip it
                pass
        # Write the numbers to the worksheet
        ws.append(numbers)

# Save the workbook
wb.save("/Users/paul/Desktop/output.xlsx")