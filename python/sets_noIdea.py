x, y = input("").split()
# print(x,y)
n=list(map(int, input("").split()))
for _ in range(int(y)):
    a = set(map(int, input("").split()))
    # a.append(numbers)
# a=set(map(int, input("").split()))
b=set(map(int, input("").split()))
# print(n,a,b)
happiness=0
# for i in a:
#     if i in n:
#         happiness+=1
# for i in b:
#     if i in n:
#         happiness-=1
# for i in n:
#     if i in a:
#         happiness+=1
#         a.remove(i)
#     if i in b:
#         happiness-=1
#         b.remove(i)
# print(happiness)
# print(" this is the sighn you are looking for")
print(n,a,b)