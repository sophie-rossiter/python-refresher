def multiply_all(*args):
    """Returns the product of any given number of numbers"""
    total = 1
    for n in args:
        total = total * n
    return total

def build_profile(**kwargs):
    """Returns a comma separated string of the key: values in a dictionary"""
    parts = [f"{key}: {value}" for key, value in kwargs.items()]
    return ", ".join(parts)

