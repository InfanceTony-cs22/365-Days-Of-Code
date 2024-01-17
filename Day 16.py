def is_valid_email(email):
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    username, rest = parts
    rest_parts = rest.split('.')
    
    # Check if there are enough parts in the rest
    if len(rest_parts) != 2 or not rest_parts[0].isalnum() or not 1 <= len(rest_parts[1]) <= 3:
        return False
    
    # Check username
    if not username.replace('-', '').replace('_', '').isalnum():
        return False
    
    return True

def main():
    N = int(input())
    emails = [input() for _ in range(N)]
    
    valid_emails = sorted(filter(is_valid_email, emails))
    print(valid_emails)

if __name__ == '__main__':
    main()
