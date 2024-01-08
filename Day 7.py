def main():
    my_dict = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 0
    }

    # Update value for key "Sunday" to 7
    my_dict["Sunday"] = 7

    # Adding another item with key "Default" having value 0
    my_dict["Default"] = 0

    # Print the sorted dictionary
    for i in sorted(my_dict):
        print("('" + i + "',", str(my_dict[i]) + ")")

    return 0

if __name__ == '__main__':
    main()
