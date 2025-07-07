class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def __del__(self):
        print(f"farewell {self.name}")

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")