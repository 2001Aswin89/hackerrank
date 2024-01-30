if __name__ == '__main__':
    lis=[]
    for _ in range(int(input())):
        l=[]
        name = input()
        score = float(input())
        l.append(name)
        l.append(score)
        lis.append(l)
    smallest=lis[0][1]
    second=lis[0][1]
    for i in range(0, len(lis)):
        if lis[i][1] == smallest:
            continue
        if lis[i][1] < smallest:
            second=smallest
            smallest=lis[i][1]
        elif lis[i][1] < second:
            second=lis[i][1]
        elif smallest== second:
            second=lis[i][1]
    list2=[]     
    for i in range(0, len(lis)):
        if lis[i][1] == second:
            list2.append(lis[i][0])
    list2.sort()
    for i in list2:
        print(i)

