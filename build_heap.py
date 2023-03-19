# python3
def had(data,swaps,n,i):
    m = (i << 1) + 1
    l = (i << 1) + 2
    maz = i
    if m < n and data[m] < data[maz]:
        maz = m
    if l < n and data[l] < data[maz]:
        maz = l
    if maz !=i:
        swaps.append((i, maz))
        data[i], data[maz] = data[maz],data[i]
        had(data,swaps,n,maz)



def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range (n // 2 -1,-1,-1):
        had(data,swaps,n,i)
    


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    c = input()
    if "F" in c:
        d = input()
        with open("tests/" + d, 'r') as file:
                r = int(file.readline())
                izv = list(map(int, file.readline().split()))
                
    if "I" in c:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))


    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
