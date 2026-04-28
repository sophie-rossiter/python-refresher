def sum_list_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def reverse_word(word):
    return word[::-1]

def get_highest_scorer(scores):
    highest_score = 0
    highest_name = ""
    for name, score in scores.items():
        if score > highest_score:
            highest_score = score
            highest_name = name
    return highest_name

def find_multiples_to_ten(num):
    multiples_list = [num]
    current_number = num
    while current_number < 10:
        current_number = current_number + num
        if current_number < 10:
            multiples_list.append(current_number)
    return multiples_list

def greeting(name):
    return f"Hello, {name}! Welcome."

def read_file(file):
    try:
        with open(file, "r") as f:
            contents = f.read()
        return contents
    except FileNotFoundError:
        print("File not found")
        return None

# These are basic functions which are not built to handle all cases