# Given N numbers. Count how many of these values are even, odd, positive and negative.

# Input
# First line contains one number N (1 ≤ N ≤ 103) number of values.

# Example
# input 
# 5
# -5 0 -3 -4 12
# output 
# Even: 3
# Odd: 2
# Positive: 1
# Negative: 3
# Note
# First Example :

# Even Numbers are : 0, -4 , 12

# Odd Numbers are : -5 , -3

# Positive Numbers are : 12

# Negative Numbers are : -5 , -3 , -4


N=int(input())
#Counters
even=0; odd=0; pve=0; nve=0

for i in range(N):
    L=int(input())

    if L%2==0: # Even
        even+=1
    else: # Odd
        odd+=1

    if L>0: #Positive
        pve+=1
    elif L<0: #Negative
        nve+=1


print('Even: '+str(even))
print('Odd: '+str(odd))
print('Positive: '+str(pve))
print('Negative: '+str(nve))