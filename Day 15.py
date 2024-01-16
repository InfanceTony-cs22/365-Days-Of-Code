from functools import reduce

def main():
    # Use map to print the square of each number
    my_ints = [4, 6, 3, 9, 2, 8, 12]
    map_result = list(map(lambda x: x**2, my_ints))
    print(map_result)

    # Use filter to print only the names that are less than or equal to seven letters
    my_names = ["scaler", "interviewbit", "rishabh", "student", "course"]
    filter_result = list(filter(lambda name: len(name) <= 7, my_names))
    print(filter_result)

    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]
    reduce_result = reduce(lambda x, y: x * y, my_numbers, 1)
    print(reduce_result)

    return 0

if __name__ == '__main__':
    main()
