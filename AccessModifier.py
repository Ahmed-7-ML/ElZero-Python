# control access modifiers:
#  which are used to restrict access to the variables and methods of the class

#  there are four types of access modifiers in python
#  1. public
#  2. private
#  3. protected
#  4. default

#  public: public variables and methods can be accessed from any where in the program
class PublicAccessModifier:
    def __init__(self):
        self.public_variable = 10
    def public_method(self):
        return self.public_variable


#  private: private variables and methods can be accessed only within the class
# declared private by adding a double underscore ‘__’ symbol
class PrivateAccessModifier:
    def __init__(self):
        self.__private_variable = 10
    def private_method(self):
            return self.__private_variable
    def public_method(self):
            return self.__private_variable

#  protected: protected variables and methods can be accessed within the class 
# and its child classes # declared protected by adding a single underscore ‘_’ symbo
class ProtectedAccessModifier:
    def __init__(self):
        self._protected_variable = 10
    def protected_method(self):
        return self._protected_variable
    def public_method(self):
        return self._protected_variable

#  default: default variables and methods can be accessed within the class and its child classes
class DefaultAccessModifier:
    def __init__(self):
        self.default_variable = 10
    def default_method(self):
            return self.default_variable


#  in python we use double underscore to make a variable or method private or protected
#  but in python we can still access private and protected variables and methods using name mangling
#  name mangling is a process of changing the name of the variable or method to make it
#  inaccessible from outside the class

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        #  here __name and __salary are private variables
        #  we can access them using name mangling

        #  here we are accessing private variables using name mangling
        #  but this is not recommended as it can lead to bugs in the program
        #  if the name of the variable is changed in the class then the name mangling will
        #  not work as expected
    def display(self):
        print(self.__name)
        print(self.__salary)
#  here we are creating an object of the class Employee
emp = Employee("John", 5000)
#  here we are accessing private variables using name mangling
print(emp._Employee__name)  #  John
print(emp._Employee__salary)  #  5000


