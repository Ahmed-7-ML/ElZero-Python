
class User:

    @classmethod
    def greet_user(cls):
        print("Hello to our System")
    
    @staticmethod
    def get_user(username):
        print(f"User name : {username}")

u1 = User()
u1.get_user("A7med")
u1.greet_user()
