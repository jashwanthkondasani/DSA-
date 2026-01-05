# n=4
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

# n = 5
# for i in range( 1,n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# n=5
# for i in range( n,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# n=4
# for i in range(n):
#     if i==0 or i==n-1:
#         print("* " * n)
#     else:
#         print("*" + "  " * (n-2) + "*")

# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
# n=7
# for i in range(1,n + 1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

n=4
for i in range(1,n + 1):
    for j in range(i):
        print(chr(65+j),end="")
    print()