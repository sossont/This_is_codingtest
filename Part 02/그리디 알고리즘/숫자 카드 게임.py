n, m = map(int,input().split())
max_card = 0
for i in range(0,n):
    input_data = list(map(int,input().split()))
    min_data = min(input_data)
    if max_card < min_data:
        max_card = min_data
print(max_card)