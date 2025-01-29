# While Codition:
#    Block Of Code
# else:
#    Block Of Code


# Training 1

My_Book1=['C++','OOP','Java','Data Structure','Algorithms']
My_Book2=('Python','Sql','MySql','PowerPi','Excel','Tableau')

a=0 # For List

while a<(len(My_Book1)) :
    print(f"#{str (a + 1).zfill( 3 )} {My_Book1[ a ]}")
    a+=1

print("="*40)

b=0 # For Tuple

while b<(len(My_Book2)) :
    print(f"#{str(b + 1).zfill( 3 )} {My_Book2[ b ]}")
    b+=1

print("="*40)

s="Ahmed"
for x in s:
    print(x)

