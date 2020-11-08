# 입력 받기
A = input()
B = input()

A = int(A)
B = int(B)

# 385 -> 5
B1 = int(B%10)
# 385 -> 8
B10 = int((B/10)%10)
# 385 -> 3
B100 = int(B/100)

# print(B1, B10, B100)

print(A * B1)
C = A * B1

print(A * B10)
D = A * B10

print(A * B100)
E = A * B100

print(C + 10*D + 100*E)