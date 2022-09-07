T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print("#" +  str(test_case), end=" ")
    for _ in range(N):
        print(str(1) + "/" + str(N), end= " ")
    print("")
