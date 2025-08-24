def main():
    x = 0
    y = 0 
    z = 0
    scoopslist = list(map(int, input().strip().split()))# Get your food items and map them into a list [5, 6, 9]
    zerocount = 0
    while zerocount < 2:
        zerocount = 0 
        smallestindex = scoopslist.index(min(scoopslist)) # Get the index of the smallest item e.g. index = 0
        smallestvalue = scoopslist.pop(smallestindex) # Remove the smallest value [6, 9]
        if smallestindex == 0:  # Add x if rice and veg
            x += 1 
        elif smallestindex == 1:
            y += 1   # Add y if curry and veg
        else:
            z += 1 # Add z if curry and rice
        for i in enumerate(scoopslist): # (0, 6) (1, 9)
            number = scoopslist.pop(i[0]) - 1
            scoopslist.insert(i[0], number)
        scoopslist.insert(smallestindex, smallestvalue)
        for i in scoopslist:
            if i == 0:
                zerocount += 1

    print(str(x), str(y), str(z))
    
    


    
main()

