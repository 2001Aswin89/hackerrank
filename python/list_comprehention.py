if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # print("[",end="")
    lis=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range (0,z+1):
                l=[]
                if i+j+k != n:
                    # print("[",i ,",",j , ",", k, "]",end="" )
                    l.append(i)
                    l.append(j)
                    l.append(k)
                    lis.append(l)
    print(lis)
