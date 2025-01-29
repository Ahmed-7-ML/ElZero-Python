#Given 3 numbers A, B and C, Print the minimum and the maximum numbers.

A=int(input())
B=int(input())
C=int(input())

print(min(A,min(B,C))," ",max(A,max(B,C)))
