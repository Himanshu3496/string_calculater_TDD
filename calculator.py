import re

def add(numbers: str) -> int:
    print("func1 called")
    if numbers == "":
        return 0

def add(numbers: str) -> int:
    print("func2 called")
    if not numbers:
        return 0
    return int(numbers)

def add(numbers: str) -> int:
    if not numbers:
        return 0
    parts = numbers.split(",")
    return sum(int(p) for p in parts)
    

def add(numbers: str) -> int:
    if not numbers:
        return 0
    parts = re.split(',|\n', numbers)
    return sum(int(p) for p in parts if p)


def add(numbers: str) -> int:
    import re
    if not numbers:
        return 0

    delimiter = ",|\n"
    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split("\n", 1)
        delimiter = re.escape(delimiter_line[2:])

    parts = re.split(delimiter, numbers)
    return sum(int(p) for p in parts if p)

print(add("//;\n1;2"))
