

class Skill(object):
    def __init__(self):
        self.skills = ["C++", "Python", "C#"]

    def __str__(self):
        return f"This is my skills {self.skills}"
    
    def __len__(self):
        return len(self.skills)


profile = Skill()
print(profile)
print(len(profile))

profile.skills.append("Sql-Server")
profile.skills.append("DB Design")

print(profile)
print(len(profile))

print(profile.__class__)
