def main():
    t = int(input().strip())
    
    for _ in range(t):
        try:
            a, b = map(int, input().split())
            result = a // b
            print(result)
        except ZeroDivisionError as e:
            print(f"Error Code: {e}")
        except ValueError as e:
            print(f"Error Code: {e}")

if __name__ == '__main__':
    main()
