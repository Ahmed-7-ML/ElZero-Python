
# Skills Without Progress:
My_Tuple=("C++","Python","SQL")

My_Dict={
    "HTMl":"90%",
    "CSS":"60%",
    "Maths":"90%"
}

def Show_Skills(name,*Skills,**SkillsWithoutProgress):
    print("Hello {} \nSkills Without Progress:".format(name))
    for skill in Skills:
        print(f"- {skill}")
    
    print("Skills With Progress :")
    for skill_key,skill_value in SkillsWithoutProgress.items():
        print(f"- {skill_key} : {skill_value}")


Show_Skills("Ahmed",*My_Tuple,**My_Dict)
