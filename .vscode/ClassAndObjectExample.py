class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is \n" + self.name)
    print("Hello my age is \n" + self.age)

name=input("please enter your name for creating candidate:-\n")
age=input("please enter your candidate age\n")
p1 = Person(name, age)
p1.myfunc()
p1.name="Bhanu Chandra"
print(p1.name)
p1.age=90
print(p1.age)
del p1
try:
  print(p1)
except NameError:
  print("object is deleted")