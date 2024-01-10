def printset(setx):
    li = list(setx)
    li.sort()
    print(li)

def main():
    # Below are the three sets
    X = set([1, 3, 7, 5, 6, 10, 20, 21, 22, 23, 55, 51, 2, 19, 9, 17, 27, 26, 25, 35])
    Y = set([2, 10, 13, 18, 17, 22, 28, 27, 5, 49, 46, 43, 3])
    Z = set([21, 1, 32, 25, 12, 11, 8, 10, 26, 16, 31, 20, 30, 14])

    # 'set1' contains the student who loves to play all three sports
    set1 = X.intersection(Y).intersection(Z)

    print("Set 1 (Football, Cricket, Basketball):")
    printset(set1)

    # 'set2' contains the student who loves to play both Football and Cricket, but don't play Basketball
    set2 = X.intersection(Y).difference(Z)

    print("\nSet 2 (Football and Cricket, not Basketball):")
    printset(set2)

    # 'set3' contains the student who loves to play Cricket, but don't love any other sport
    set3 = Y.difference(X.union(Z))

    print("\nSet 3 (Cricket only, not Football or Basketball):")
    printset(set3)

    return 0

if __name__ == '__main__':
    main()
