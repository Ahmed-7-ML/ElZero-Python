# Recurision => Function can call it self
# Recurision => common mathematical and programming concept


#--Factorial Example--#


def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

# print(fact(5))

# By Recurision

def fact1(n):
    if(n!=0):
        count=n
        if(count > 0):
            f= n * fact(n-1)
            count-=1
        else:
            return
        return f
    else:
        return 1

print(fact1(0))

def fact2(n):
    if(n > 0):
        return n * fact(n-1)
    else:
        return 1

print(fact2(4))


# def tri_recursion(k):
# 	if(k > 0):
# 	    result = k + tri_recursion(k - 1)
# 	    print(result)
# 	else:
# 	    result = 0
# 	return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# Example From Elzero
def clean_word(word):
    if (len(word)==1):
        return word
    else:
        if(word[0]==word[1]):
            return clean_word(word[1:])
        else:
            return word[0]+clean_word(word[1:])

print(clean_word("AAAAAHHHHHHMMMMMEEEEEDDDDDD"))
