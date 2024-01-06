def main():
    # Build a list
    my_list = ['Robin', 'Aman', 'Rahul']

    # Access elements by index
    print(my_list)  # prints ['Robin', 'Aman', 'Rahul']

    # Access elements by index (alternative approach)
    for i in range(len(my_list)):
        print(my_list[i])

    try:
        # Accessing an index which does not exist generates an exception
        print(my_list[5])  # Raises an error
    except IndexError as e:
        print(f"Error: {e}")

    # Negative Indexing
    print(my_list[-1])  # prints 'Rahul'
    print(my_list[-2])  # prints 'Aman'

if __name__ == '__main__':
    main()

