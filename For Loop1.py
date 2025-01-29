#------------------------
#For Loop With Dictionary
#------------------------

My_Skills={
    "Html":"90%",
    "Css":"50%",
    "C#":"0%",
    "JS":"100%",
    "C++":"90%",
    "Python":"60%",
}

print(My_Skills.get("Python"))
print(My_Skills['C++'])

for skill in My_Skills:
    # print(f"My Progress in Language: {skill} is {My_Skills[skill]}")
    print(f"My Progress in Language: {skill} is {My_Skills.get(skill)}")
