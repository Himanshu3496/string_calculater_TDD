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
    

print(add(""))
