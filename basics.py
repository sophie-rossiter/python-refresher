def sum_list_of_numbers(numbers):
    """Returns the sum of all numbers in a list"""
    total = 0
    for number in numbers:
        total += number
    return total

def reverse_word(word):
    """Returns the reverse of a given string"""
    return word[::-1]

def get_highest_scorer(scores):
    """Returns the name of the highest scorer in a dictionary of name/score pairs"""
    highest_score = 0
    highest_name = ""
    for name, score in scores.items():
        if score > highest_score:
            highest_score = score
            highest_name = name
    return highest_name

def find_multiples_to_ten(num):
    """Returns a list of the multiples of a number which are less than 10"""
    multiples_list = [num]
    current_number = num
    while current_number < 10:
        current_number = current_number + num
        if current_number < 10:
            multiples_list.append(current_number)
    return multiples_list

def greeting(name):
    """Returns a personalised greeting string for the given name"""
    return f"Hello, {name}! Welcome."

def read_file(file):
    """Reads and returns the contents of a file. Returns None if the file is not found."""
    try:
        with open(file, "r") as f:
            contents = f.read()
        return contents
    except FileNotFoundError:
        print("File not found")
        return None

# These are basic functions which are not built to handle all cases