from itertools import permutations

def main():
    # Input
    input_str, k = input().split()
    k = int(k)

    # Generating permutations and printing them
    for perm in sorted(permutations(input_str, k)):
        print(''.join(perm))

if __name__ == '__main__':
    main()
