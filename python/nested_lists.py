if __name__ == '__main__':
    lis=[]
    for _ in range(int(input())):
        l=[]
        name = input()
        score = float(input())
        l.append(name)
        l.append(score)
        lis.append(l)
    # print(lis)
    largest=0
    second=0
    for i in range(0, len(lis)):
        if lis[i][1] >= second:
            if lis[i][1] >= largest:
                second=largest
                largest=lis[i][1]
            else:
                second=lis[i][1]
    # print(second, " ", largest)

    for i in range(0, len(lis)):
        if lis[i][1] == second:
            print(lis[i][0])


