class Member(object):

    not_allowed_names = ["Shit", "Hell", "Blooot"]
    user_count = 0

    @classmethod
    def show_no_of_users(cls):
        return f"Hello From Class Method , No. of users = {cls.user_count}"
    
    @staticmethod
    def say_hello():
        print("Hello From Static Method")

    def __init__(self,fname, mname, lname, gender):
        self.firstname =fname
        self.middlename = mname
        self.lastname = lname
        self.sex = gender
        Member.user_count += 1

    def name_with_title(self):
        if self.sex == 'Male':
            return f"Hello Mr {self.firstname}"
        elif self.sex == 'Female':
            return f"Hello Miss {self.firstname}"
        else:
            return f"Hello {self.firstname}"
    
    def full_name(self):
        if self.firstname in Member.not_allowed_names:
            raise ValueError("Name Not Allowed")
        else:
            return f"Full Name is {self.firstname} {self.middlename} {self.lastname}"
    
    def delete_user(self):

        Member.user_count -= 1
        return f"User {self.firstname} {self.lastname} deleted"


print(Member.user_count)

m1 = Member("Ahmed", "Akram", "Kamel", "Male")
print(m1.firstname)
print(m1.middlename)
print(m1.lastname)
print(m1.sex)

print(m1.full_name())
print(m1.name_with_title())

print("=" * 50)

print(Member.user_count)

m2 = Member("Shimaa", "Mohamed", "Wahba", "Female")
print(m2.firstname)
print(m2.middlename)
print(m2.lastname)
print(m2.sex)

print(m2.full_name())
print(m2.name_with_title())

print("=" * 50)

print(Member.user_count)

print("=" * 50)

print(Member.user_count)

m3 = Member("Shit", "Hell", "Wass", "Female")

print(Member.user_count)

print(m3.delete_user())

print(Member.user_count)


print(Member.show_no_of_users())
Member.say_hello()














