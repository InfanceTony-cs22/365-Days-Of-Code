def main():
    my_set = set([1, 3, 2, 4, 1, 3, 3, 0])
    
    # add 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 to my_set
    my_set.update([10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    
    # delete 2 and 3 from my_set
    my_set.discard(2)
    my_set.discard(3)
    
    # convert set to list and sort it
    li = list(my_set)
    li.sort()

    print(li)
    return 0

if __name__ == '__main__':
    main()
