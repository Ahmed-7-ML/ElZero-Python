# Given a number N. Print all even numbers between 1 and N inclusive in separate lines.

# Input
# Only one line containing a number N (1 ≤ N ≤ 103).

# Output
# Print the answer according to the required above. If there are no even numbers print -1



N=int(input())
if N!=1 and N!=0:
    for i in range(1,N+1):
        if i%2==0:
            print(i)
        
else:
    print(-1)
