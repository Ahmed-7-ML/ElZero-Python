
# f=[(x,y,z) for x in [1,2,3,4,5] for y in [6,7,8,9,10] for z in [11,12,13,14,15] if (x!=y ) ]
# print (f)

# # Check Difference:
# S1="Ahmed Love Python"
# for x in S1:
#     print(x)

# print("="*40)

# for x in range(len(S1)):
#     print(S1[x])

# print("="*40)

# # Print in reversed way:
# for x in range(len(S1)):
#     print(S1[len(S1)-x-1])

# print("="*40)

# for x in range(len(S1)):
#     print(S1[-x-1])


# print("="*40)

# for x in reversed(S1):
#     print(x)

for x in range (2,20,2):
    if x%5==0:
        continue
    print(x)

print("="*40)


for x in range (2,10):
    if x%2==0 or x%3==0:
        continue
    print(x)


print("="*40)


for x in range (2,10):
    if x%2==0:
        print("Even Number:"+str(x))
        continue
    print("Odd Number:",x)

for x in {1,2,3,4,5}:
    if x==2:
        break
    print(x)


