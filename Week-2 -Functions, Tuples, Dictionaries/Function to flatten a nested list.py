nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
def flatten(list):
    flat = [item for sublist in nested for item in sublist]
    print(flat)
flatten(nested)
