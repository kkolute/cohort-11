def find_max_min (numbers):
    if min(numbers)== max(numbers):
        return [len(numbers)]
    return [min(numbers),max(numbers)]