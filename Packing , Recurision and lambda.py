# Assignment 1
def get_score(**Skills):
    for skill_key , skill_value in Skills.items():
        print(f"- {skill_key} => {skill_value}")

# Tests
get_score(Math=90, Science=80, Language=70)

# Output
"Math => 90"
"Science => 80"
"Language => 70"

print("="*30)

# Tests
get_score(Logic=70, Problems=60)

# Output
"Logic => 70"
"Problems => 60"

print("="*30)

# Assignment 2

scores_list={
    "Logic":"70",
    "problems":"60",
    "language":'50'
}

def get_people_scores(name='',**Skills):
    if len(name)!=0 and len(Skills)!=0:
        print(f"Hello {name} \nThis Is Your Score Table:")
    if len(Skills)!=0:
        for key,value in Skills.items():
            print(f"- {key} => {value}")
    else:
        print(f"Hello {name} You Have No Scores To Show")


# # Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

print("="*30)

# # Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)

# Output
"Hello Mahmoud This Is Your Score Table:"
"Logic => 70"
"Problems => 60"

print("="*30)

# # Test 3
get_people_scores(Logic=70, Problems=60)

# Output
"Logic => 70"
"Problems => 60"

print("="*30)

# # Test 4
get_people_scores("Ahmed")

# Output
"Hello Ahmed You Have No Scores To Show"

print("="*30)

get_people_scores(**scores_list)