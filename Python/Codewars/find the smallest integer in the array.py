array = [34, 15, 88, 2]
def find_smallest_int(arr):
    smallest = sorted(arr)[0]

    return smallest

print(find_smallest_int(array))