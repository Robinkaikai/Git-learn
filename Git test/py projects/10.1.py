class Person:
    def __init__(self,name,element,sex):
        self.name = name
        self.element = element
        self.sex = sex

    def IfLike(self):
        if self.sex == "Male":
            print("No!Get out!")
        else:
            print("Yes!My favorite feature is "+self.name)

    def PrintPerson(self):
        print(self.name)
        print(self.element)

Yae = Person("Yae Miko",'electro',"Female")
Yae.IfLike()
Yae.PrintPerson()