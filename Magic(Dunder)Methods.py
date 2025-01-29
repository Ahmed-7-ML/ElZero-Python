
class Skill:

    def __init__(self):
        self.skills = ["C++", "C#", "Python"]
    
    def __len__(self):
        return len(self.skills)

    def __str__(self):
        return F"Skills {self.skills}"
    

profile = Skill()

print(profile)

print(type(profile))
print(profile.__class__)

print(len(profile))

profile.skills.append("Data Analysis")
profile.skills.append("Excel")

print(profile)

print(len(profile))
