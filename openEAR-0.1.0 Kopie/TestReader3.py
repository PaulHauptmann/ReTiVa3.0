import openpyxl

# Open the workbook and the worksheet
wb = openpyxl.Workbook()
ws = wb.active

# Open the file in read mode
with open('/Users/paul/Desktop/openEAR-0.1.0/smile.log', 'r') as f:
    # Set the file pointer to the end of the file
    f.seek(0, 2)
    
    while True:
        # Wait for a new line to be added to the file
        line = f.readline()
        if line:
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
        wb.save("/User/paul/Desktop/output.xlsx")
