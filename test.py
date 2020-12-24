class Base:
    pass

class Child(Base):
    string = ""

child = Child()
print(isinstance(child, list))