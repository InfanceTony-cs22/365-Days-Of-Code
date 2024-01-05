def main():
    S = input()

    # Check if S has any alphanumeric characters
    print(any(char.isalnum() for char in S))

    # Check if S has any alphabetical characters
    print(any(char.isalpha() for char in S))

    # Check if S has any digits
    print(any(char.isdigit() for char in S))

    # Check if S has any lowercase characters
    print(any(char.islower() for char in S))

    # Check if S has any uppercase characters
    print(any(char.isupper() for char in S))

if __name__ == '__main__':
    main()
