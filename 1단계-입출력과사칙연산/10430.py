A, B, C = input().split(" ")
A = int(A)
B = int(B)
C = int(C)

print(int((A+B)%C))
print(int((int(A%C)+int(B%C))%C))
print(int((A*B)%C))
print(int((int(A%C)*int(B%C))%C))