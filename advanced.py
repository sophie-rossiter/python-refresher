# words = ["cat", "horse", "crocodile"]
# longer_than_four = [n for n in words if len(n) > 4]

def multiply_all(*args):
    total = 1
    for n in args:
        total = total * n
    return total

def build_profile(**kwargs):
    parts = [f"{key}: {value}" for key, value in kwargs.items()]
    return ", ".join(parts)

