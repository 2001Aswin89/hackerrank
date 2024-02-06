# x, y = map(int, input().split())



# n = list(map(int, input().split()))

# a = set(map(int, input().split()))

# b = set(map(int, input().split()))

# happiness=0
# # for i in a:
# #     if i in n:
# #         happiness+=1
# # for i in b:
# #     if i in n:
# #         happiness-=1
# for i in n:
#     if i in a:
#         happiness+=1
#         a.remove(i)
#     if i in b:
#         happiness-=1
#         b.remove(i)
# print(happiness)
# # print(" this is the sighn you are looking for")



def calculate_happiness(arr, liked_set, disliked_set):
    happiness = 0

    for num in arr:
        if num in liked_set:
            happiness += 1
        elif num in disliked_set:
            happiness -= 1

    return happiness

# Taking user inputs
n, m = map(int, input().split())
arr = list(map(int, input().split()))
liked_set = set(map(int, input().split()))
disliked_set = set(map(int, input().split()))

# Calculate and print the final happiness
result = calculate_happiness(arr, liked_set, disliked_set)
print( result)