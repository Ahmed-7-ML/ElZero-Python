# IsSuperSet() => Compare Second List to First List
# IsSubSet() => Compare First List to Second List
#Result =>> True || False

S1={1,2,3,4,5}
S2={1,2,3}

print(S1.issuperset(S2)) # True
print(S2.issuperset(S1)) # False

print("="*40)

S3={1,2,3}
S4={1,23,2,4,3,5}

print(S3.issubset(S4)) # True
print(S4.issubset(S3)) # False

print("="*40)

# IsDisJoint() => هل هم منفصلين ولا لا؟
# يعنى لو فيهم عناصر متشابهة يبقي مش مفصولين عن بعض
# يعنى لو مفصولين => True
# يعنى لو مش مفصولين => False


S5={1,3,5,7,9,11}
S6={1,3,5}

print(S5.isdisjoint(S6))

S7={1,3,4,5}
S8={1,3,4,5}
S9={6,7,8,9}

print(S7.isdisjoint(S8))
print(S7.isdisjoint(S9))

print("="*40)
