import re

def is_valid_mobile_number(number):
    # Define a regular expression pattern for a valid mobile number
    pattern = re.compile(r'^[6789]\d{9}$')
    
    # Check if the number matches the pattern
    if pattern.match(number):
        return "YES"
    else:
        return "NO"

def main():
    # Input the number of test cases
    N = int(input().strip())

    # Process each test case
    for _ in range(N):
        # Input the mobile number
        mobile_number = input().strip()
        
        # Check if it's a valid mobile number and print the result
        result = is_valid_mobile_number(mobile_number)
        print(result)

if __name__ == '__main__':
    main()

