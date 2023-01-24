def get_highest_double(a, b, c, d, e, f, g):
    # Create a dictionary to store the variable names and their values
    variables = {'Anger': a, 'Boredom': b, 'Disgust': c, 'Fear': d, 'Happiness': e, 'Neutral': f, 'Sadness': g}
    
    # Find the highest value and the corresponding variable name
    highest_value = max(variables.values())
    highest_name = [name for name, value in variables.items() if value == highest_value][0]
    
    # Return the variable name as a string
    return highest_name

a = [2.5,986713]
b = [3.0,87324]
c = [1.2,231867]
d = [4.1,927835]
e = [2.7,42376]
f = [5.0,42678]
g = [2.9,578092]

highest_double_name = get_highest_double(a[-1], b[-1], c[-1], d[-1], e[-1], f[-1], g[-1])
print(highest_double_name) # Output: 'f'
